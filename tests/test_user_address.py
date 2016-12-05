# coding=utf-8


def test_user_address_create(api_post, token):
    data = {'user_id': 1, 'region_code': '440103', 'street': 'test', 'consignee': 'avicha', 'contact': '010-12345678910', 'token': token}
    errcode, result = api_post('/api/user_address/create', data=data)
    assert errcode == 0
    assert 'id' in result
    assert 'created_at' in result


def test_user_address_update(api_post, token, user_address):
    if user_address:
        update_data = {'user_address_id': user_address.id, 'region_code': user_address.region_code, 'street': user_address.street, 'consignee': user_address.consignee, 'contact': user_address.contact, 'token': token}
        errcode, result = api_post('/api/user_address/update', data=update_data)
        assert errcode == 0
        assert 'updated_at' in result


def test_user_address_list(api_get_list, token):
    errcode, result, total_rows = api_get_list('/api/user_address/list', data={'token': token})
    assert errcode == 0
    assert total_rows >= 0
    if total_rows > 0:
        user_address = result[0]
        assert 'id' in user_address
        assert 'user_id' in user_address
        assert 'region_code' in user_address
        assert 'street' in user_address
        assert 'is_default' in user_address
        assert 'consignee' in user_address
        assert 'contact' in user_address
        assert 'created_at' in user_address


def test_user_address_set_default(api_post, token, user_address):
    if user_address:
        errcode, result = api_post('/api/user_address/set_default', data={'user_address_id': user_address.id, 'token': token})
        assert errcode == 0


def test_user_address_delete(api_get, token, user_address):
    if user_address:
        errcode, result = api_get('/api/user_address/delete', data={'token': token, 'user_address_id': user_address.id})
        assert errcode == 0
        assert 'deleted_at' in result
