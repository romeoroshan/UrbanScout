from django.contrib.auth.backends import ModelBackend

class CustomModelBackend(ModelBackend):
    def user_can_authenticate(self, user):
        # Allow authentication for both active and inactive users
        return True
