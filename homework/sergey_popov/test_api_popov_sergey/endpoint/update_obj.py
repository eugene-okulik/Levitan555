import requests
import allure

from .base_endpoint import Endpoint


class UpdateObj(Endpoint):

    @allure.feature('Put request')
    @allure.story('Update object full')
    @allure.title('Изменение всего объекта')
    @allure.step('Update object full')
    def change_obj(self, body, new_post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{new_post_id}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.feature('Patch request')
    @allure.story('update object part')
    @allure.title('Изменение части объекта')
    @allure.step('Run patch request')
    def change_part_obj(self, body, new_post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{new_post_id}',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
