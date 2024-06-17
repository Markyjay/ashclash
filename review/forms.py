from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            "title",
            "text",
            "rating",
        )

    title = forms.CharField(max_length=200)
    rating = forms.IntegerField(min_value=1, max_value=5)
    text = forms.CharField(widget=forms.Textarea)