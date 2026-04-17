from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Username",
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "input-field"
        })
    )
    submit = forms.CharField(widget=forms.TextInput(attrs={
        "type": "submit",
        "class": "btn-primary",
        "value": "Sign Up"
    }))

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Username",
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "input-field"
        })
    )
    submit = forms.CharField(widget=forms.TextInput(attrs={
        "type": "submit",
        "class": "btn-primary",
        "value": "Login"
    }))
    