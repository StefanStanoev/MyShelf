from django import forms

from review.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','comment']  

        widgets = {
            'rating': forms.RadioSelect(choices=[(i,f"{i} ⭐")for i in range (1,6)]),
            'comment': forms.Textarea(attrs={'rows':2,'placeholder':'Your opinion about this book'}),
            
        }
