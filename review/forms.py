from django import forms
from products.widgets import CustomClearableFileInput
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

    title = forms.CharField(max_length=200)
    image = forms.ImageField(label='Image',
                required=False, widget=CustomClearableFileInput)
    rating = forms.IntegerField(min_value=1, max_value=5)
    text = forms.CharField(widget=forms.Textarea)