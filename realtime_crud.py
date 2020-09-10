from firebase import firebase

from config import project_url


class FirebaseCRUD:
    def __init__(self):
        self.fire_base_url = project_url
        self.firebase_project = firebase.FirebaseApplication(self.fire_base_url, None)

    def post_data(self, data_base, table, data):
        result = self.firebase_project.post(f'/{data_base}/{table}', new_user, {'print': 'pretty'},
                                            {'X_FANCY_HEADER': 'VERY FANCY'})
        print(result)

    def read_data(self, data_base, table):
        result = self.firebase_project.get(f'/{data_base}/{table}', None)
        print(result)


new_fire_base = FirebaseCRUD()
new_fire_base.read_data(data_base="ponasasa", table="users")
# new_user = {
#     "first_name": 'Abednego',
#     "last_name": 'Kilonzo'
# }
# new_fire_base.post_data(data=new_user, data_base="ponasasa", table="users")
