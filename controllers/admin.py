# coding=utf-8
import bcrypt
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer
from flask import Blueprint, current_app

from backend_common.controllers.base import BaseController
from backend_common.middlewares.login_required import admin_required
from backend_common.middlewares.request_service import get_request_params, load_admin
from backend_common.models.admin import Admin as AdminModel
from backend_common.models.user_token import UserToken as UserTokenModel
import backend_common.constants.user_type as user_type

admin_blueprint = Blueprint('admin', __name__)


class AdminController(BaseController):

    @classmethod
    @get_request_params()
    def login(cls, data):
        try:
            username = data['username']
            password = data['password']
            admin = AdminModel.get(AdminModel.username == username, AdminModel.deleted_at == None)
            if bcrypt.checkpw(password.encode('utf-8'), admin.password.encode('utf-8')):
                s = TimedJSONWebSignatureSerializer(current_app.secret_key, expires_in=2*60*60)
                token = s.dumps(admin.id)
                UserTokenModel.create(user_id=admin.id, user_type=user_type.ADMIN, token=token)
                result = admin.format('id,username')
                result.update({'token': token})
                return cls.success_with_result(result)
            else:
                raise AdminModel.PasswordError()
        except AdminModel.DoesNotExist, e:
            raise AdminModel.NotFoundError(u'该用户不存在')
        except KeyError, e:
            raise AdminModel.LackOfFieldError(u'请传递参数用户名和密码')

    @classmethod
    @load_admin
    def current(cls, admin):
        if admin:
            result = admin.format('id,username')
            return cls.success_with_result(result)
        else:
            return cls.success_with_result(None)

    @classmethod
    @get_request_params()
    @admin_required
    def logout(cls, admin, data):
        token = data.get('token')
        UserTokenModel.delete().where(UserTokenModel.user_id == admin.id, UserTokenModel.user_type == user_type.ADMIN, UserTokenModel.token == token).execute()
        return cls.success()

    @classmethod
    @get_request_params()
    @admin_required
    def reset_password(cls, admin, data):
        try:
            old_password = data['old_password']
            new_password = data['new_password']
            if bcrypt.checkpw(old_password.encode('utf-8'), admin.password.encode('utf-8')):
                admin.password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                admin.updated_at = datetime.now()
                admin.save()
                return cls.success()
            else:
                raise AdminModel.PasswordError()
        except KeyError, e:
            AdminModel.LackOfFieldError(u'请传递参数旧密码和新密码')
