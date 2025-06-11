import allure
import requests
from .base_endpoint import Endpoint


class DelObj(Endpoint):

    @allure.feature('Delete request')
    @allure.story('Delete object')
    @allure.title('Удаление объекта')
    def del_obj(self, new_post_id):
        with allure.step(f'Delete object {new_post_id}'):
            self.response = requests.delete(f'{self.url}/{new_post_id}')
            return self.response
