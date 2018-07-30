from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from app.models import contact
#from accounts.models import Document, Category, ImageCategory
from django.forms import ModelForm
from django.forms.widgets import TextInput, NumberInput


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')


class DocumentForm(forms.Form):
    keyword = forms.CharField(max_length=200)


class CreateImageForm(forms.ModelForm):
    title = forms.CharField(max_length=200)


from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=200)
    file = forms.FileField()



class contactForm(forms.ModelForm):  
    class Meta:  
        model = contact  
        fields = "__all__"  





