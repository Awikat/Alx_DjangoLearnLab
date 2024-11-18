from django import forms
from bookshelf.models import Book

class ExampleForm(forms.Form):
    query = forms.CharField(max_length=100, required=True)  # Validates user input
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }
