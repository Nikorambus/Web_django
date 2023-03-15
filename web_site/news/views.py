from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date')                       # Сортировка по дате
    return render(request, 'news/news_home.html', {'news': news})   # Доп параметр


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'                                 # Ключ для передачи объекта в шаблон


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm                                       # Используемая форма


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':            # Проверка, каким методом отправляются данные
        form = ArticlesForm(request.POST)
        if form.is_valid():                 # Если форма была коректной то сохраняется
            form.save()
            return redirect('/news/')       # Выполн переодр
        else:
            error = 'Форма была не верной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)

