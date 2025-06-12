import pytest
import requests

from endpoint.create_obj import CreateObj
from endpoint.update_obj import UpdateObj
from endpoint.get_obj import GetObj
from endpoint.delete_obj import DelObj


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


@pytest.fixture()
def return_post_endpoint():
    return CreateObj()


@pytest.fixture()
def return_put_endpoint():
    return UpdateObj()


@pytest.fixture()
def return_patch_endpoint():
    return UpdateObj()


@pytest.fixture()
def get_all_obj():
    return GetObj()


@pytest.fixture()
def get_one_obj():
    return GetObj()


@pytest.fixture()
def return_del_obj():
    return DelObj()


@pytest.fixture
def new_obj_id():
    body = {'data': {'color': 'white', 'size': 'big'}, 'name': 'First object'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f'http://167.172.172.115:52353/object/{obj_id}')
