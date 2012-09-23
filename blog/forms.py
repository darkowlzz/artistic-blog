from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=150, required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)
