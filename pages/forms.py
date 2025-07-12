from django import forms
from .models import Login

class LoginForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name", help_text="Enter your full name:")
    email = forms.EmailField(label="Email", required=False)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    message = forms.CharField(label="Message", widget=forms.Textarea)

class LoginModelForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address', 'autocomplete': 'email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'autocomplete': 'new-password'}),
            'message': forms.Textarea(attrs={'placeholder': 'Type your message here', 'rows': 4, 'cols': 40}),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'password': 'Password',
            'message': 'Your Message',
        }


