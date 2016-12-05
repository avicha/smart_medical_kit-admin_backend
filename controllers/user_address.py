# coding=utf-8
from datetime import datetime
from flask import Blueprint

from backend_common.middlewares.login_required import admin_required
from backend_common.middlewares.exists_required import user_address_exists
from backend_common.middlewares.request_service import get_request_params
from backend_common.models.database import database
from backend_common.models.user_address import UserAddress as UserAddressModel
from backend_common.controllers.user_address import UserAddressController as UserAddressCommonController

user_address_blueprint = Blueprint('user_address', __name__)


class UserAddressController(UserAddressCommonController):

    @classmethod
    @get_request_params('user_id', 'region_code', 'street', 'consignee', 'contact')
    @admin_required
    def create(cls, admin, data):
        user_address = UserAddressModel.create(**data)
        return cls.success_with_result(user_address.format('id,created_at'))

    @classmethod
    @get_request_params('user_address_id', 'region_code', 'street', 'consignee', 'contact', allow_field_not_exists=False)
    @admin_required
    def update(cls, admin, data):
        user_address_id = data.get('user_address_id')
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if user_address_id:
            del data['user_address_id']
            data.update({'updated_at': now})
            UserAddressModel.update(**data).where(UserAddressModel.id == user_address_id, UserAddressModel.deleted_at == None).execute()
            return cls.success_with_result({'updated_at': now})
        else:
            raise UserAddressModel.LackOfFieldError(u'请传入用户地址ID')

    @classmethod
    @get_request_params()
    @admin_required
    def list(cls, admin, data):
        user_id = data.get('user_id')
        q = UserAddressModel.select().where(UserAddressModel.user_id == user_id, UserAddressModel.deleted_at == None)
        result = []
        for x in q.order_by(UserAddressModel.created_at.desc()):
            user_address = x.format('id,user_id,region_code,street,is_default,consignee,contact,created_at')
            result.append(user_address)
        return cls.success_with_list_result(len(result), result)

    @classmethod
    @get_request_params()
    @admin_required
    def delete(cls, admin, data):
        user_address_id = data.get('user_address_id')
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        UserAddressModel.update(deleted_at=now).where(UserAddressModel.id == user_address_id).execute()
        return cls.success_with_result({'deleted_at': now})

    @classmethod
    @user_address_exists
    @admin_required
    def set_default(cls, admin, user_address):
        with database.transaction():
            UserAddressModel.update(is_default=False).where(UserAddressModel.user_id == user_address.user_id, UserAddressModel.deleted_at == None).execute()
            user_address.is_default = True
            user_address.save()
            return cls.success_with_result(None)
