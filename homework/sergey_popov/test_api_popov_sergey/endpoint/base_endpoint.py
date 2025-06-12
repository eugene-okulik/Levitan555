import allure


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    headers = {'Content-Type': 'application/json'}
    response = None
    json = None

    @allure.step('Check that status code is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, 'Status code is incorrect'

    def check_obj_name(self, obj_name):
        with allure.step(f'Check name object is {obj_name}'):
            assert self.json['name'] == obj_name, 'Object is not UPD'

    def check_obj_id(self, new_obj_id):
        self.json = self.response.json()
        with allure.step(f'Check name object is {new_obj_id}'):
            assert self.json['id'] == new_obj_id, 'ID is incorrect'
