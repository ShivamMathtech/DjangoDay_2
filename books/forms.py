from django import forms
from .models import Book ,NewBook

class Bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','author','price','description','publish_date']
        
class NewBookForm(forms.ModelForm):
    class Meta:
        model=NewBook
        fields=['title','author','price','description','publish_date']