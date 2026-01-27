from django import forms

from book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__' 

        widgets = {'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a book title'}),
                   'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter an author '}),
                   'publication_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter publication year'}),
                   'publisher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a publisher '}),
                   'language': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter book language '}),
                   'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter literary genre'})
                     }

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)

        get_title = cleaned_data.get('title')
        
        check_title = Book.objects.filter(first_name=get_title)
        if check_title:
            msg = f'This book is already registered.'
            self.add_error('title', msg)
          
        return cleaned_data
        
