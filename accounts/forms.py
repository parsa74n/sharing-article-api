from .models import User
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField



class UserCreationForm(forms.ModelForm):
    
    """
    forms for creating users in admin pannel


    """


    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','phone_number','email','staff','superuser','gender')



    def clean_password2(self):
        """
        checking for passwords matching.
        
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2



    def save(self, commit=True):
   
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    """
    form for changing and updating user models in admin pannel
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username','phone_number','email', 'password', 'is_active', 'staff','superuser','gender')