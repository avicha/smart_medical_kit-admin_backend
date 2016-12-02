# coding=utf-8
from datetime import datetime
from flask import Blueprint

from backend_common.middlewares.login_required import admin_required
from backend_common.middlewares.request_service import get_request_params
from backend_common.models.user import User as UserModel
from backend_common.controllers.user import UserController as UserCommonController

user_blueprint = Blueprint('user', __name__)


class UserController(UserCommonController):

    @classmethod
    @get_request_params
    @admin_required
    def list(cls, admin, data):
        page_number = int(data.get('page_number', 1))
        page_size = int(data.get('page_size', 100))
        q = UserModel.select().where(UserModel.deleted_at == None)
        total_rows = q.count()
        result = []
        for x in q.order_by(UserModel.created_at.desc()).paginate(page_number, page_size):
            user = x.format('id,username,sex,phone_number,nick,avatar,register_type,created_at')
            result.append(user)
        return cls.success_with_list_result(total_rows, result)

    @classmethod
    @get_request_params('user_id', 'sex', 'phone_number', 'nick', 'avatar', allow_field_not_exists=False)
    @admin_required
    def update(cls, admin, data):
        user_id = data.get('user_id')
        if user_id:
            del data['user_id']
            data.update({'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            num = UserModel.update(**data).where(UserModel.id == user_id, UserModel.deleted_at == None).execute()
            if num:
                return cls.success_with_result({'updated_at': data.get('updated_at')})
            else:
                raise UserModel.NotFoundError(u'该用户不存在')
        else:
            raise UserModel.LackOfFieldError(u'请传入用户ID')
