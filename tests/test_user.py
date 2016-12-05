# coding=utf-8


def test_user_list_api(api_get_list, token):
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


def test_user_update_api(api_post, token, user):
    if user:
        update_data = {'user_id': user.id, 'phone_number': user.phone_number, 'nick': user.nick, 'avatar': user.avatar, 'token': token}
        errcode, result = api_post('/api/user/update', data=update_data)
        assert errcode == 0
        assert 'updated_at' in result
