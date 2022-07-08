from django.shortcuts import render
from django.http import HttpResponse  

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views import generic


"""
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
"""

from .models  import Book, Author, BookInstance, Genre

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """
      Функция отображения для домашней страницы сайта.
      request - это объект запроса, используемый для генерации этого ответа. При изменении адресса сайта
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применён по умолчанию.
    num_boos_find = Book.objects.filter(title__icontains="the").count()
    
    num_visits=request.session.get('num_visits', 0)
    # Получение значения сессии.
    request.session['num_visits'] = num_visits + 1
    # Передача значения в сессию


    context={'num_books_str':num_books,'num_instances':
    num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors, 'num_boos_find':num_boos_find, 'num_visits':num_visits}
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(request,'index.html',context)

def display_all_books(request):
  all_books = Book.objects.all()
  context = {'books': all_books}
  return render(request,'book_list.html',context)

def book_details(request,title):
  book_by_title = Book.objects.filter(title__icontains = title)
  context = {'book_by_title' : book_by_title}
  return render(request,'book_details.html',context)



class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = BookInstance
    template_name ='bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')




class BookListView(generic.ListView):
    model = Book