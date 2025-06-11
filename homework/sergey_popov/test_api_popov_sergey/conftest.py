import pytest
import requests


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