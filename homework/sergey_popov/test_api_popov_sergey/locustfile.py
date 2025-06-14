from locust import task, HttpUser


class ActionApi(HttpUser):
    obj_id = None
    obj_json = {'data': {'color': 'white', 'size': 'big'}, 'name': 'First object'}
    obj_headers = {'Content-Type': 'application/json'}

    def on_start(self):
        response = self.client.post('/object', json=self.obj_json, headers=self.obj_headers)
        self.obj_id = response.json()['id']

    @task
    def get_req_all(self):
        self.client.get('/object')

    @task
    def get_req_one(self):
        self.client.get(f'/object/{self.obj_id}')

    @task
    def post_req(self):
        self.client.post('/object', json=self.obj_json, headers=self.obj_headers)

    @task
    def put_req(self):
        body = {'data': {'color': 'white', 'size': 'big'}, 'name': 'Second object'}
        self.client.put(f'/object/{self.obj_id}', json=body, headers=self.obj_headers)

    @task
    def patch_req(self):
        body = {'data': {'color': 'green', 'size': 'small'}}
        self.client.patch(f'/object/{self.obj_id}', json=body, headers=self.obj_headers)
