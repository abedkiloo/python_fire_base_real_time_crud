from firebase import firebase

from config import project_url


class FirebaseCRUD:
    def __init__(self):
        self.fire_base_url = project_url
        self.firebase_project = firebase.FirebaseApplication(self.fire_base_url, None)

    def post_data(self, data_base, table, data):
        result = self.firebase_project.post(f'/{data_base}/{table}', data, {'print': 'pretty'},
                                            {'X_FANCY_HEADER': 'VERY FANCY'})
        print(result)

    def read_data(self, data_base="ponasasa", table="users", index=None):
        request_string = f'/{data_base}/{table}'
        if index is not None:
            request_string = request_string + f"/{index}"
        result = self.firebase_project.get(request_string, None)
        data = dict()
        for key, value in result.items():
            data[key] = value
        return data

    def single_object(self, index):
        obj = self.read_data(data_base="ponasasa", table="users", index=index)
        return obj

    def read_objects(self, objects):
        print(objects)

    def update_object(self, data_base="ponasasa", table="users", index=None, ):
        request_string = f'/{data_base}/{table}/-MGriENlOp0fuio9rXts'

        result = self.firebase_project.put(request_string, 'first_name', 'Abed')

    def delete_data_object(self, data_base="ponasasa", table="users", index=None, ):

        request_string = f'/{data_base}/{table}'

        result = self.firebase_project.delete(request_string, "-MGriENlOp0fuio9rXts")


new_fire_base = FirebaseCRUD()

# new_fire_base.read_objects(
#     new_fire_base.read_objects(new_fire_base.read_data()))
# new_fire_base.read_objects(
#     new_fire_base.single_object("-MGriENlOp0fuio9rXts"))
new_fire_base.update_object()
new_fire_base.delete_data_object()
