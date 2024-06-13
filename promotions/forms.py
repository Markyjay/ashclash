from django import forms
from .models import PromotionalPlayer
from cloudinary.forms import CloudinaryFileField


class PromotionalPlayerForm(forms.ModelForm):
    class Meta:
        model = PromotionalPlayer
        fields = '__all__'

    image = CloudinaryFileField(required=False)