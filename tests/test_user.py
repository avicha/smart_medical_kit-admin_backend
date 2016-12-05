# coding=utf-8


def test_user_create(api_post, token):
    import backend_common.constants.register_type as register_type
    data = {'phone_number': '12345678910', 'nick': 'test', 'register_type': register_type.SYSTEM, 'token': token}
    errcode, result = api_post('/api/user/create', data=data)
    assert errcode == 0
    assert 'id' in result
    assert 'created_at' in result


def test_user_update(api_post, token, user):
    if user:
        update_data = {'user_id': user.id, 'phone_number': user.phone_number, 'nick': user.nick, 'avatar': user.avatar, 'token': token}
        errcode, result = api_post('/api/user/update', data=update_data)
        assert errcode == 0
        assert 'updated_at' in result


def test_user_list(api_get_list, token):
    errcode, result, total_rows = api_get_list('/api/user/list', data={'token': token})
    assert errcode == 0
    assert total_rows >= 0
    if total_rows > 0:
        user = result[0]
        assert 'id' in user
        assert 'username' in user
        assert 'sex' in user
        assert 'phone_number' in user
        assert 'nick' in user
        assert 'avatar' in user
        assert 'register_type' in user
        assert 'created_at' in user


def test_user_delete(api_get, token, user):
    if user:
        errcode, result = api_get('/api/user/delete', data={'token': token, 'user_id': user.id})
        assert errcode == 0
        assert 'deleted_at' in result
