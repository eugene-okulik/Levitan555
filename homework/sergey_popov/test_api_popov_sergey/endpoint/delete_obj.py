import allure
import requests
from .base_endpoint import Endpoint
from .get_obj import GetObj


class DelObj(Endpoint):

    @allure.feature('Delete request')
    @allure.story('Delete object')
    @allure.title('Удаление объекта')
    def del_obj(self, new_obj_id):
        with allure.step(f'Delete object {new_obj_id}'):
            self.response = requests.delete(f'{self.url}/{new_obj_id}')
            return self.response

    def check_remove_obj(self, new_obj_id, get_one_obj):
        with allure.step(f'Check that object with id = {new_obj_id} is removed'):
            get_one_obj.get_obj_one(new_obj_id)
            assert get_one_obj.response.status_code == 404, 'Object not removed'
