from django import forms
from review.models import Ulasan

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Ulasan
        fields = ['reviewer_name', 'review_text', 'rating']
