from django.urls import path, include
from . import views
#rom django.conf.urls import url

from django.contrib import admin
admin.autodiscover()

"""
urlpatterns = [
    path('', views.current_datetime),
]
"""
urlpatterns = [
    path('', views.index, name='index'),
    path('books',views.display_all_books, name='display_all_books' ),
    path('books/<str:title>/',views.book_details, name='book_details' ),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed' ),
    
    #url(r'^$', views.index, name='index'),
    #url(r'^books/$', views.BookListView.as_view(), name='books'),
    #name - связь темплейтс с юрл
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
"""
именя в path - для того, чтобы ссылки из шаблонов кидать
path('articles/<int:year>/<int:month>/' ...) - при переходе /articles/2005/03/  
Джанго вызовет функцию .views.month_archive(request, year=2005, month=3)
name='index' - это как мы обращаемся к ссылке по имени
"""
