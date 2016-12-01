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
            user = x.format('id,username,sex,phone_number,nick,avatar,created_at,register_type')
            result.append(user)
        return cls.success_with_list_result(total_rows, result)

    @classmethod
    @get_request_params
    @admin_required
    def update(cls, admin, data):
        user_id = data.get('user_id')
        sex = data.get('sex', 0)
        phone_number = data.get('phone_number', None)
        nick = data.get('nick', None)
        avatar = data.get('avatar', None)
        if user_id:
            update_data = {'phone_number': phone_number, 'sex': sex, 'nick': nick, 'avatar': avatar, 'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            num = UserModel.update(**update_data).where(UserModel.id == user_id, UserModel.deleted_at == None).execute()
            if num:
                return cls.success_with_result({'updated_at': update_data.get('updated_at')})
            else:
                raise UserModel.NotFoundError(u'该用户不存在')
        else:
            raise UserModel.LackOfFieldError(u'请传入用户ID')
