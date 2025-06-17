from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Your Phone Number (Optional)'
        })
    )

    preferred_contact = forms.ChoiceField(
        choices=[
            ('', 'Select Preferred Contact Method'),
            ('email', 'Email'),
            ('phone', 'Phone')
        ],
        widget=forms.Select(attrs={
            'class': 'form-input',
            'id': 'preferred-contact'
        })
    )

    best_time = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Best Time to Contact You (Optional)'
        })
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'preferred_contact', 'best_time', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Your Email Address'}),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Your Message',
                'rows': 5
            }),
        }


class FAQForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Name',
            'class': 'form-input'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your Email',
            'class': 'form-input'
        })
    )
    question = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Your Question',
            'class': 'form-textarea',
            'rows': 5
        })
    )
