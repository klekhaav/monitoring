from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Customer


# admin form for user creation
class CustomerCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(CustomerCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# admin form for change user fields
class CustomerChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Customer
        fields = ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]
