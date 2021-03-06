from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
	
	author       = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name   = models.CharField('Есіміңіз', max_length = 40)
	last_name    = models.CharField('Әкеңіз', max_length = 40, blank = True, default = 'Білмеймін')
	third_name   = models.CharField('Атаңыз', max_length = 40, blank = True, default = 'Білмеймін')
	fourth_name  = models.CharField('Атаңыздың әкесі', max_length = 40, blank = True, default = 'Білмеймін')
	fiveth_name  = models.CharField('Атаңыздың атасы', max_length = 40, blank = True, default = 'Білмеймін')
	sixth_name   = models.CharField('Атаңыздың атасының әкесі', max_length = 40, blank = True, default = 'Білмеймін')
	seventh_name = models.CharField('Оның атасы', max_length = 40, blank = True, default = 'Білмеймін')

	ru  = models.CharField('Ру', max_length = 90, blank = True, default = 'Білмеймін')
	jus = models.CharField('Жүз', max_length = 90, blank = True, default = 'Білмеймін')
	jynys = models.CharField('Жынысыныз', max_length = 150)
	biog         = models.TextField('Өзіңіз жайында') # категория ПОСТ болған жағдайда, ПОСТ денесі (body)
	birth_day    = models.CharField('Туылған күні', max_length = 3)
	birth_mounth = models.CharField('Туылған Айы', max_length = 20)
	birth_year   = models.CharField('Туылған Жылы', max_length = 150)

	date           = models.DateField('Уақыты', auto_now_add = True)
	contact_number = models.CharField('Байланыс телефоны', max_length = 11, blank = True)
	facebook       = models.CharField('Facebook', max_length = 250, blank = True)
	instagram	   = models.CharField('Instagram', max_length = 250)
	whatsapp	   = models.CharField('Whatsapp', max_length = 12, blank = True)

	category = models.CharField('Категория', max_length = 10, blank = True, default = 'Іздеу')

	
	def __str__(self):
		return self.first_name + ' ' + self.third_name

	
class Comment(models.Model):
	post   = models.ForeignKey(Article, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body   = models.TextField('Пікір')

	def __str__(self):
		return str(self.author)