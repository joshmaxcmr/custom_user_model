from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age","email", "nationality" )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ( "username", "email", "age", )