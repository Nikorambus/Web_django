from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']    # Поля используемые для формы заполнения

        widgets = {
            "title": TextInput(attrs={                      # Указываем атрибуты
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),

            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи',
            }),

            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата статьи (YYYY.MM.DD HH:MI:SS)',
            }),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
            }),
        }