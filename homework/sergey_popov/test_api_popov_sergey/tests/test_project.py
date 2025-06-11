import allure
import pytest

obj_list = [
    {'data': {'color': 'white', 'size': 'big'}, 'name': 'First object'},
    {'data': {'color': 'green', 'size': 'small'}, 'name': 'Second object'},
    {'data': {'color': 'red', 'size': 'big'}, 'name': 'Third object'}
]

change_object = {'data': {'color': 'red', 'size': 'big'}, 'name': 'Four object'}


def test_get_all(start_test_ses, start_test_fun, get_all_obj):
    get_all_obj.get_obj_all()
    get_all_obj.check_status_code()


def test_get_one(new_post_id, start_test_fun, get_one_obj):
    get_one_obj.get_obj_one(new_post_id)
    get_one_obj.check_status_code()
    get_one_obj.check_obj_id(new_post_id)


@pytest.mark.parametrize('objects', obj_list)
def test_post_obj(objects, start_test_fun, return_post_endpoint):
    return_post_endpoint.new_obj(body=objects)
    return_post_endpoint.check_status_code()


@pytest.mark.critical
def test_put_obj(new_post_id, start_test_fun, return_put_endpoint):
    return_put_endpoint.change_obj(change_object, new_post_id)
    return_put_endpoint.check_obj_name(change_object['name'])


@pytest.mark.medium
def test_patch_obj(new_post_id, start_test_fun, return_patch_endpoint):
    with allure.step('Prepare test data'):
        body = {'name': 'Four object'}
    return_patch_endpoint.change_part_obj(body, new_post_id)
    return_patch_endpoint.check_obj_name(body['name'])


def test_del_post(new_post_id, start_test_fun, return_del_obj):
    return_del_obj.del_obj(new_post_id)
