# coding=utf-8
from controllers.admin import admin_blueprint, AdminController
from controllers.user import user_blueprint, UserController
from controllers.user_address import user_address_blueprint, UserAddressController


def init_app(current_app):
    # 管理员
    admin_blueprint.add_url_rule('/login', 'login_api', AdminController.login, methods=['post'])
    admin_blueprint.add_url_rule('/logout', 'logout_api', AdminController.logout, methods=['get'])
    admin_blueprint.add_url_rule('/reset_password', 'reset_password_api', AdminController.reset_password, methods=['post'])
    current_app.register_blueprint(admin_blueprint, url_prefix='/api/admin')
    # 用户
    user_blueprint.add_url_rule('/create', 'create_api', UserController.create, methods=['post'])
    user_blueprint.add_url_rule('/update', 'update_api', UserController.update, methods=['post'])
    user_blueprint.add_url_rule('/list', 'list_api', UserController.list, methods=['get'])
    user_blueprint.add_url_rule('/delete', 'delete_api', UserController.delete, methods=['get'])
    current_app.register_blueprint(user_blueprint, url_prefix='/api/user')
    # 用户地址
    user_address_blueprint.add_url_rule('/create', 'create_api', UserAddressController.create, methods=['post'])
    user_address_blueprint.add_url_rule('/update', 'update_api', UserAddressController.update, methods=['post'])
    user_address_blueprint.add_url_rule('/list', 'list_api', UserAddressController.list, methods=['get'])
    user_address_blueprint.add_url_rule('/delete', 'delete_api', UserAddressController.delete, methods=['get'])
    user_address_blueprint.add_url_rule('/set_default', 'set_default_api', UserAddressController.set_default, methods=['post'])
    current_app.register_blueprint(user_address_blueprint, url_prefix='/api/user_address')
