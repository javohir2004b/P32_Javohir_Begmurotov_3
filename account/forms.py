from django.contrib.auth.forms import UserCreationForm

from account.models import CustomerUser


class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ('phone', 'email',)