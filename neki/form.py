from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"title"}))
    description = forms.CharField(required=False)
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
           raise  forms.ValidationError("zasral si")
        if not "news" in title:
            raise forms.ValidationError("spet si zasral")
        return title



class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"title"}))
    description = forms.CharField(required=False)
    price = forms.DecimalField(initial=199.99)