from django import forms

from book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__' 

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your product name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a description for your product'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'})
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)

        # UNICITATE PE FIRST NAME SI LAST NAME
        get_name= cleaned_data.get('name')
        get_author = cleaned_data.get('author')

        check_name_author = Book.objects.filter(name=get_name, author=get_author)
        if check_name_author:
            msg = f'This book is already registered.'
            self.add_error('name', msg)
            self.add_error('author', msg)

        return cleaned_data
        
