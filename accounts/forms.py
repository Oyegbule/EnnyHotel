from django import forms
from django.contrib.auth.models import User

class StaffRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[],  # This removes the rules
        help_text=None   # This removes the "Your password must..." text
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        # This part is crucial: it hashes the password so you can actually login
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user