from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=200, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )

    text = forms.CharField(
        required=False, 
        widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'})
        )

    rating = forms.IntegerField(
        min_value=0, 
        max_value=10, 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
        )