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
    @get_request_params()
    @admin_required
    def create(cls, admin, data):
        import backend_common.constants.sex as sex
        phone_number = data.get('phone_number')
        user_data = {
            'nick': data.get('nick'),
            'sex': data.get('sex', sex.UNKNOWN),
            'avatar': data.get('avatar'),
            'register_type': data.get('register_type')
        }
        user, is_new_created = UserModel.get_or_create(phone_number=phone_number, defaults=user_data)
        return cls.success_with_result(user.format('id,created_at'))

    @classmethod
    @get_request_params('user_id', 'phone_number', 'nick', 'sex',  'avatar', allow_field_not_exists=False)
    @admin_required
    def update(cls, admin, data):
        user_id = data.get('user_id')
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if user_id:
            del data['user_id']
            data.update({'updated_at': now})
            UserModel.update(**data).where(UserModel.id == user_id, UserModel.deleted_at == None).execute()
            return cls.success_with_result({'updated_at': now})
        else:
            raise UserModel.LackOfFieldError(u'请传入用户ID')

    @classmethod
    @get_request_params()
    @admin_required
    def list(cls, admin, data):
        page_number = int(data.get('page_number', 1))
        page_size = int(data.get('page_size', 100))
        phone_number = data.get('phone_number')
        q = UserModel.select().where(UserModel.deleted_at == None)
        if phone_number:
            q = q.where(UserModel.phone_number == phone_number)
        total_rows = q.count()
        result = []
        for x in q.order_by(UserModel.created_at.desc()).paginate(page_number, page_size):
            user = x.format('id,phone_number,nick,sex,avatar,register_type,created_at')
            result.append(user)
        return cls.success_with_list_result(total_rows, result)

    @classmethod
    @get_request_params()
    @admin_required
    def delete(cls, admin, data):
        user_id = data.get('user_id')
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        UserModel.update(deleted_at=now).where(UserModel.id == user_id).execute()
        return cls.success_with_result({'deleted_at': now})
