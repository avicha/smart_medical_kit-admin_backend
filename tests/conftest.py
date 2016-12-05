# coding=utf-8
import sys
sys.path.append('.')
import pytest
from app import current_app
from flask import json


@pytest.fixture(scope="session")
def client():
    from backend_common.models.database import database
    current_app.config['TESTING'] = True
    with database.transaction() as txn:
        yield current_app.test_client()
        txn.rollback()


@pytest.fixture(scope="session")
def token(api_post, api_get):
    from backend_common.models.admin import Admin as AdminModel
    import backend_common.constants.http_code as http_code
    errcode, result = api_post('/api/admin/login', data={'username': 'admin', 'password': '123456'})
    assert errcode == 0
    assert 'id' in result
    assert 'username' in result
    assert 'token' in result
    token = result.get('token')
    yield token
    # 退出登录
    errcode, result = api_get('/api/admin/logout', data={'token': token})
    assert errcode == 0
    # 再次退出登录会报错，因为token已经失效
    errcode, result = api_get('/api/admin/logout', data={'token': token})
    assert errcode == int(str(http_code.FORBIDDEN) + AdminModel.code)


@pytest.fixture(scope="session")
def api_post(client):
    def f(url, *args, **kwargs):
        resp = client.post(url, *args, **kwargs)
        assert resp.status_code == 200
        data = json.loads(resp.data)
        errcode = data.get('errcode')
        result = data.get('result')
        return errcode, result
    return f


@pytest.fixture(scope="session")
def api_get(client):
    def f(url, *args, **kwargs):
        resp = client.get(url, *args, **kwargs)
        assert resp.status_code == 200
        data = json.loads(resp.data)
        errcode = data.get('errcode')
        result = data.get('result')
        return errcode, result
    return f


@pytest.fixture(scope="session")
def api_get_list(client):
    def f(url, *args, **kwargs):
        resp = client.get(url, *args, **kwargs)
        assert resp.status_code == 200
        data = json.loads(resp.data)
        errcode = data.get('errcode')
        result = data.get('result')
        total_count = data.get('total_count')
        return errcode, result, total_count
    return f


@pytest.fixture
def user():
    from backend_common.models.user import User as UserModel
    user = UserModel.select().where(UserModel.deleted_at == None).order_by(UserModel.created_at.desc()).first()
    return user
