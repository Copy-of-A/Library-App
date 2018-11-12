from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie import fields
from catalog.models import Author, Book


class AuthorResource(ModelResource):
    class Meta:
        queryset = Author.objects.all()
        resource_name = 'author'


class BookResource(ModelResource):
    author = fields.ForeignKey(AuthorResource, 'author', blank=True, null=True)
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'

