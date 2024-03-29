# from django import forms
# from .models import Flats


# class ClothesForm(forms.ModelForm):
#     class Meta:
#         model = Flats
#         exclude = ["is_active"]
#         widgets = {
#             'title': forms.TextInput(attrs={'class': "form-control"}),
#             'description': forms.Textarea(attrs={'class': "form-control"}),
#             'image': forms.ClearableFileInput(attrs={'class': "form-control"}),
#             'size': forms.Select(attrs={'class': "form-control"}),
#             'price': forms.NumberInput(attrs={'class': "form-control"}),
#             'old_price': forms.NumberInput(attrs={'class': "form-control"}),
#             'currency': forms.Select(attrs={'class': "form-control"}),
#             'category': forms.Select(attrs={'class': "form-control"})
#         }