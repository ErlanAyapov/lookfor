from .models import Article, Comment
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


# choices = Category.objects.all().values_list('name', 'name')

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = [
			'author', 'first_name', 'last_name', 'third_name', 'fourth_name', 'fiveth_name', 'sixth_name', 'seventh_name', 
			'ru', 'jus', 'jynys', 'biog', 'birth_day', 'birth_mounth', 'birth_year',
			'facebook', 'contact_number', 'instagram', 'whatsapp', 'category'

		]

		widgets = {
			'first_name':   TextInput(attrs={'class': 'form-control','placeholder': 'Есіміңіз',}),
			'last_name':    TextInput(attrs={'class': 'form-control','placeholder': 'Әкеңіз(ешқандай жалғаусыз) , егер білмесеңіз бос қалдырыңыз',}),
			'third_name':   TextInput(attrs={'class': 'form-control','placeholder': 'Атаңыз (ешқандай жалғаусыз)',}),
			'fourth_name':  TextInput(attrs={'class': 'form-control','placeholder': 'Атаңыздың әкесі',}),
			'fiveth_name':  TextInput(attrs={'class': 'form-control','placeholder': 'Атаңыздың атасы',}),
			'sixth_name':   TextInput(attrs={'class': 'form-control','placeholder': 'Атаңыздың атасының әкесі',}),
			'seventh_name': TextInput(attrs={'class': 'form-control','placeholder': 'Атаңыздың атасының әкесі',}),

			'ru':    TextInput(attrs={'class': 'form-select-mystyle',}),
			'jus':   TextInput(attrs={'class': 'form-select-mystyle',}),
			'jynys': TextInput(attrs={'class': 'form-select-mystyle',}),
			'biog':  Textarea (attrs={'class': 'form-control', 'placeholder': 'Өзіңіз жайында немесе бұл платформаға қандай мақсатпен тіркелдіңіз, кімді іздейсіз сол жайында жазыңыз',}),
			
			'birth_day':    TextInput(attrs={'class': 'form-select-birthdate',}),
			'birth_mounth': TextInput(attrs={'class': 'form-select-birthdate',}),
			'birth_year':   TextInput(attrs={'class': 'form-select-birthdate',}),

			'contact_number': TextInput(attrs={'class': 'form-control','placeholder': 'Байланыс номеріңіз, міндетті емес',}),
			'facebook':		  TextInput(attrs={'class': 'form-control','placeholder': 'facebook(-қа) сілтеме, міндетті емес',}),
			'instagram':	  TextInput(attrs={'class': 'form-control','placeholder': 'instagram(-ға) сілтеме, міндетті түрде',}),
			'whatsapp':		  TextInput(attrs={'class': 'form-control','placeholder': 'whatsapp номеріңіз, міндетті емес',}),
		}
		exclude = ['author']


class PostAdd(ModelForm):

	class Meta:
		model  = Article
		fields = ['author', 'biog', 'category']
		
		widgets = {
			'biog':  Textarea (attrs={'class': 'form-control', 'placeholder': 'Жаңалықпен бөліс',}),
		}

		exclude = ['author', 'category']


class CommentForm(ModelForm):
	class Meta:
		model  = Comment
		fields = ['author', 'post', 'body']

		widgets = {
			'body':  Textarea (attrs={'class': 'form-control', 'placeholder': 'Пікір қалдыр',}),
			'post':  TextInput(attrs={'class': 'form-control', 'placeholder': 'post',}),
		}

		exclude = ['author']

class CommentUpdateForm(ModelForm):
	class Meta:
		model  = Comment
		fields = ['body']
		widgets = {
			'body':  Textarea (attrs={'class': 'form-control', 'placeholder': 'Пікір қалдыр',}),
		}

		
