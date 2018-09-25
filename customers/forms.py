from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class Customer_SignUp_Form(UserCreationForm):

    class Meta:

        model = get_user_model()
        fields = ('email','full_name','password1','password2')


