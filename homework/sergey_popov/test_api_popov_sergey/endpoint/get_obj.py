import requests
import allure
from .base_endpoint import Endpoint


class GetObj(Endpoint):

    @allure.feature('Get request')
    @allure.story('Provides information about all objects')
    @allure.title('Запрос информации обо всех объектах')
    @allure.step('Object information')
    def get_obj_all(self):
        self.response = requests.get(self.url)
        return self.response

    @allure.feature('Get request')
    @allure.story('Provides information about one object')
    @allure.title('Запрос информации об одном объекте')
    def get_obj_one(self, new_obj_id):
        with allure.step(f'Provides information about objects with id {new_obj_id}'):
            self.response = requests.get(f'{self.url}/{new_obj_id}')
            return self.response
