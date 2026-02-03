from django import forms

from book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'  

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter an author for the book'}),
            'publication_year':forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter book publication year'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter book publisher'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter number of pages'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter literary genre'}),
            'language': forms.TextInput(attrs={'class': 'form-control', 'rows':5 ,'placeholder': 'Please enter book language'}),
            'cover': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the type of cover'}),
            'category':forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter a short description of the book'}),
            'img': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter an image'})
            
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)


        get_title = cleaned_data.get('title')

        check_title = Book.objects.filter(title=get_title)
        if check_title:
            msg = f'This book is already registered in your shelf!'
            self.add_error('title', msg)

        return cleaned_data
    

class BookUpdateForm(forms.ModelForm):
     class Meta:
        model = Book
        fields = ['publication_year', 'publisher','pages','genre','language','category','description', 'img']

        widgets = {
            #'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter book title'}),
            #'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter an author for the book'}),
            'publication_year':forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter book publication year'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter book publisher'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter number of pages'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter literary genre'}),
            'language': forms.TextInput(attrs={'class': 'form-control', 'rows':5 ,'placeholder': 'Please enter book language'}),
            #'cover': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the type of cover'}),
            'category':forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter a short description of the book'}),
            'img': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter an image'})

        }