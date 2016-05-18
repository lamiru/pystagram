import re
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserProfile

User = get_user_model()

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    def clean_password2(self):
        password2 = super(SignupForm, self).clean_password2()
        if password2:
            if len(password2) < 6:
                raise forms.ValidationError('Input at least 6 letters.')
            elif re.match(r'^\d+$', password2):
                raise forms.ValidationError("Don't input numeric letters only.")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email').strip()
        if email:
            if User.objects.filter(email=email).exists() == True:
                raise forms.ValidationError('This email is already used.')
        return email

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('biography',)
