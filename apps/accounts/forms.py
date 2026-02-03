from allauth.account.forms import LoginForm, SignupForm
from django import forms

class CustomLoginForm(LoginForm):
    remember = forms.BooleanField(required=False, label='Remember Me')

    def login(self, *args, **kwargs):
        remember = self.cleaned_data.get('remember')
        self.request.session.set_expiry(0 if not remember else None)
        return super().login(*args, **kwargs)


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, required=True, label='First Name')
    middle_name = forms.CharField(max_length=30, required=False, label='Middle Name')
    last_name = forms.CharField(max_length=30, required=True, label='Last Name')
    
    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.middle_name = self.cleaned_data['middle_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user