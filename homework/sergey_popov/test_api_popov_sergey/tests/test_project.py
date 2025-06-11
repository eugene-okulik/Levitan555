import allure
import requests
import pytest

obj_list = [
    {'data': {'color': 'white', 'size': 'big'}, 'name': 'First object'},
    {'data': {'color': 'green', 'size': 'small'}, 'name': 'Second object'},
    {'data': {'color': 'red', 'size': 'big'}, 'name': 'Third object'}
]


@allure.feature('Get request')
@allure.story('Provides information about all objects')
@allure.title('Запрос информации обо всех объектах')
def test_get_all(start_test_ses, start_test_fun):
    with allure.step('object information'):
        response = requests.get('http://167.172.172.115:52353/object')
    with allure.step('Check that status code is 200'):
        assert response.status_code == 200, 'Status code is incorrect'


@allure.feature('Get request')
@allure.story('Provides information about one object')
@allure.title('Запрос информации об одном объекте')
def test_get_one(new_post_id, start_test_fun):
    with allure.step(f'Provides information about objects with id {new_post_id}'):
        response = requests.get(f'http://167.172.172.115:52353/object/{new_post_id}')
    with allure.step('Check that status code is 200'):
        assert response.status_code == 200
    with allure.step(f'Check that post id is {new_post_id}'):
        assert response.json()['id'] == new_post_id, 'ID is incorrect'


@allure.feature('Post request')
@allure.story('Create object')
@allure.title('Создание объекта')
@pytest.mark.parametrize('objects', obj_list)
def test_post_obj(objects, start_test_fun):
    with allure.step('Prepare test data'):
        body = {
            'data': {'color': 'white', 'size': 'big'}, 'name': 'First object'
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step('Run post request'):
        response = requests.post(
            'http://167.172.172.115:52353/object',
            json=body,
            headers=headers
        )
    with allure.step('Check that status code is 200'):
        assert response.status_code == 200, 'Status code is incorrect'


@allure.feature('Put request')
@allure.story('Update object full')
@allure.title('Изменение всего объекта')
@pytest.mark.critical
def test_put_obj(new_post_id, start_test_fun):
    with allure.step('Prepare test data'):
        body = {
            'data': {'color': 'white', 'size': 'big'}, 'name': 'Third object'
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step('Run put request'):
        response = requests.put(
            f'http://167.172.172.115:52353/object/{new_post_id}',
            json=body,
            headers=headers
        )
    with allure.step('Check name object is Third object'):
        assert response.json()['name'] == 'Third object', 'Object is not UPD'


@allure.feature('Patch request')
@allure.story('update object part')
@allure.title('Изменение части объекта')
@pytest.mark.medium
def test_patch_obj(new_post_id, start_test_fun):
    with allure.step('Prepare test data'):
        body = {'name': 'Four object'}
        headers = {'Content-Type': 'application/json'}
    with allure.step('Run patch request'):
        response = requests.patch(
            f'http://167.172.172.115:52353/object/{new_post_id}',
            json=body,
            headers=headers
        )
    with allure.step('Check name object is Four object'):
        assert response.json()['name'] == 'Four object', 'Object is not UPD'


@allure.feature('Delete request')
@allure.story('Delete object')
@allure.title('Удаление объекта')
def test_del_post(new_post_id, start_test_fun):
    with allure.step(f'Delete object {new_post_id}'):
        requests.delete(f'http://167.172.172.115:52353/object/{new_post_id}')