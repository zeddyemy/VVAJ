from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Username",
        })
    )

    email = forms.EmailField(  
        widget=forms.EmailInput(attrs={
            "placeholder": "Email",
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "input-field"
        })
    )
    
    confirm_password = forms.CharField(
    widget=forms.PasswordInput(attrs={
        "placeholder": "Confirm password",
        "class": "input-field"
    })
)
    
    
    submit = forms.CharField(
        widget=forms.TextInput(attrs={
            "type": "submit",
            "class": "btn-primary",
            "value": "Sign Up"
        })
    )



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
