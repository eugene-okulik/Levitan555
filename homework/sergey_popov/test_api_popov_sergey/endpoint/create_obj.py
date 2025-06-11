import allure
import requests

from .base_endpoint import Endpoint


class CreateObj(Endpoint):

    @allure.feature('Post request')
    @allure.story('Create object')
    @allure.title('Создание объекта')
    @allure.step('Run post request')
    def new_obj(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
