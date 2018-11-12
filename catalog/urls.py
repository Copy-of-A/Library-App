from django.conf.urls import url, include
from catalog import views
from catalog.api import AuthorResource, BookResource

urlpatterns = [
    url('', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]
