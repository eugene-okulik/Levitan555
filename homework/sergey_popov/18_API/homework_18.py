import requests


def get_all():
    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code == 200, 'Status code is incorrect'


get_all()


def get_one():
    post_id = 1
    response = requests.get(f'http://167.172.172.115:52353/object/{post_id}')
    assert response.status_code == 200
    assert response.json()['id'] == post_id, 'ID is incorrectly'


get_one()


def post_obj():
    body = {
        'data': {'color': 'white', 'size': 'big'}, 'name': 'First object'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'


post_obj()


def post_obj_test():
    body = {
        'data': {'color': 'white', 'size': 'big'}, 'name': 'First object'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    return response.json()['id']


def clear(post_id):
    response = requests.delete(f'http://167.172.172.115:52353/object/{post_id}')


def put_obj():
    post_id = post_obj_test()
    body = {
        'data': {'color': 'white', 'size': 'big'}, 'name': 'Third object'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{post_id}',
        json=body,
        headers=headers
    )
    assert response.json()['name'] == 'Third object', 'Object is not UPD'
    clear(post_id)


put_obj()


def patch_obj():
    post_id = post_obj_test()
    body = {'name': 'Four object'}
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{post_id}',
        json=body,
        headers=headers
    )
    assert response.json()['name'] == 'Four object', 'Object is not UPD'
    clear(post_id)


patch_obj()


def del_post():
    post_id = post_obj_test()
    response = requests.delete(f'http://167.172.172.115:52353/object/{post_id}')


del_post()
