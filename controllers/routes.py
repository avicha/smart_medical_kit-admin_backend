# coding=utf-8
from controllers.admin import admin_blueprint, AdminController
from controllers.user import user_blueprint, UserController


def init_app(current_app):
    # 管理员
    admin_blueprint.add_url_rule('/login', 'login_api', AdminController.login, methods=['post'])
    admin_blueprint.add_url_rule('/logout', 'logout_api', AdminController.logout, methods=['get'])
    admin_blueprint.add_url_rule('/reset_password', 'reset_password_api', AdminController.reset_password, methods=['post'])
    current_app.register_blueprint(admin_blueprint, url_prefix='/api/admin')
    # 用户
    user_blueprint.add_url_rule('/list', 'list_api', UserController.list, methods=['get'])
    user_blueprint.add_url_rule('/update', 'update_api', UserController.update, methods=['post'])
    current_app.register_blueprint(user_blueprint, url_prefix='/api/user')
