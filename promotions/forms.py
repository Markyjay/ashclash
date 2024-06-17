from django import forms
from .models import PromotionalPlayer
from products.widgets import CustomClearableFileInput
from cloudinary.forms import CloudinaryFileField


class PromotionalPlayerForm(forms.ModelForm):
    class Meta:
        model = PromotionalPlayer
        fields = '__all__'

    image = CloudinaryFileField(required=False, widget=CustomClearableFileInput)