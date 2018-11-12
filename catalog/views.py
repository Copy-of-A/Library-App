# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Author, Book
from django.views import generic


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_books=Book.objects.all().count()
    num_authors=Author.objects.count()

    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_authors':num_authors},
    )   


class BookListView(generic.DetailView):
    
    model = Book
    
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context


class BookDetailView(generic.DetailView):
    model = Book
    def book_detail_view(request):
        try:
            book_id=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")
    
        return render(
            request,
            'book_detail.html',
            context={'book':book_id,}
        )
