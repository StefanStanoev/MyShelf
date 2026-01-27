from django import forms

from category.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__' 

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your category name'}), }

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)


        get_name = cleaned_data.get('name')
        check_name = Category.objects.filter(name=get_name)
        if check_name:
            msg = f'This category is already registered!'
            self.add_error('name', msg)

        return cleaned_data
        
