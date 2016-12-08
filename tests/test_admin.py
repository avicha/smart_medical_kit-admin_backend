# coding=utf-8
from backend_common.models.admin import Admin as AdminModel
import backend_common.constants.http_code as http_code


def test_login_lack_of_field(api_post):
    errcode, result = api_post('/api/admin/login', data={'username': 'admin', 'not_password': '123456'})
    assert errcode == int(str(http_code.BAD_REQUEST) + AdminModel.code)


def test_login_user_not_exists(api_post):
    errcode, result = api_post('/api/admin/login', data={'username': 'not_a_user', 'password': '123456'})
    assert errcode == int(str(http_code.NOT_FOUND) + AdminModel.code)


def test_login_password_error(api_post):
    errcode, result = api_post('/api/admin/login', data={'username': 'admin', 'password': '654321'})
    assert errcode == int(str(http_code.FORBIDDEN) + AdminModel.code)


def test_logout_without_token(api_get):
    errcode, result = api_get('/api/admin/logout')
    assert errcode == int(str(http_code.FORBIDDEN) + AdminModel.code)


def test_logout_with_error_token(api_get):
    errcode, result = api_get('/api/admin/logout', data={'token': '123456'})
    assert errcode == int(str(http_code.FORBIDDEN) + AdminModel.code)


def test_current_not_exists(api_get):
    errcode, result = api_get('/api/admin/current')
    assert errcode == 0
    assert result == None


def test_current_exists(api_get, token):
    errcode, result = api_get('/api/admin/current', data={'token': token})
    assert errcode == 0
    assert 'id' in result
    assert 'username' in result


def test_reset_password_error(api_post, token):
    errcode, result = api_post('/api/admin/reset_password', data={'old_password': '654321', 'new_password': '123456'})
    assert errcode == int(str(http_code.FORBIDDEN) + AdminModel.code)


def test_reset_password(api_post, token):
    errcode, result = api_post('/api/admin/reset_password', data={'old_password': '123456', 'new_password': '654321', 'token': token})
    assert errcode == 0
    # 旧密码失效
    errcode, result = api_post('/api/admin/login', data={'username': 'admin', 'password': '123456'})
    assert errcode == int(str(http_code.FORBIDDEN) + AdminModel.code)
    # 新密码生效
    errcode, result = api_post('/api/admin/login', data={'username': 'admin', 'password': '654321'})
    assert errcode == 0
