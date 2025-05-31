import pytest
import requests

obj_list = [
    {'data': {'color': 'white', 'size': 'big'}, 'name': 'First object'},
    {'data': {'color': 'green', 'size': 'small'}, 'name': 'Second object'},
    {'data': {'color': 'red', 'size': 'big'}, 'name': 'Third object'}
]


@pytest.fixture
def new_post_id():
    body = {'data': {'color': 'white', 'size': 'big'}, 'name': 'First object'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'http://167.172.172.115:52353/object/{post_id}')

@pytest.fixture(scope='session')
def start_test_ses():
    yield print('Start testing')
    print()
    print('Testing completed')

@pytest.fixture()
def start_test_fun():
    yield print('before test')
    print()
    print('after test')

def test_get_all(start_test_ses, start_test_fun):
    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code == 200, 'Status code is incorrect'


def test_get_one(new_post_id, start_test_fun):
    response = requests.get(f'http://167.172.172.115:52353/object/{new_post_id}')
    assert response.status_code == 200
    assert response.json()['id'] == new_post_id, 'ID is incorrect'


@pytest.mark.parametrize('objects', obj_list)
def test_post_obj(objects, start_test_fun):
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

@pytest.mark.critical
def test_put_obj(new_post_id, start_test_fun):
    body = {
        'data': {'color': 'white', 'size': 'big'}, 'name': 'Third object'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{new_post_id}',
        json=body,
        headers=headers
    )
    assert response.json()['name'] == 'Third object', 'Object is not UPD'

@pytest.mark.medium
def test_patch_obj(new_post_id, start_test_fun):
    body = {'name': 'Four object'}
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{new_post_id}',
        json=body,
        headers=headers
    )
    assert response.json()['name'] == 'Four object', 'Object is not UPD'


def test_del_post(new_post_id, start_test_fun):
    requests.delete(f'http://167.172.172.115:52353/object/{new_post_id}')
