from firebase import firebase

from config import project_url


class FirebaseCRUD:
    def __init__(self):
        self.fire_base_url = project_url
        self.firebase_project = firebase.FirebaseApplication(self.fire_base_url, None)

    def post_data(self):
        new_user = 'Abednego Kilonzo'

        result = self.fire_base_url.post('/users', new_user, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
        print(result)


new_fire_base = FirebaseCRUD
new_fire_base.post_data()
