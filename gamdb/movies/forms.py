from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(max_length=200)
    text = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField(min_value=1, max_value=10)