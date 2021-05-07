from index.models import Article
from django import forms

class ActorSearchForm(forms.Form):
    first_name =  forms.CharField(
                    required = False,
                    label='Search name or surname!',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )

   
