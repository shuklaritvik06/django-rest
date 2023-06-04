import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Books


class Book(DjangoObjectType):
    class Meta:
        model = Books
        fields = "__all__"
        
        
class BookInput(graphene.InputObjectType):
    book_name = graphene.String(required=True)
    book_desc = graphene.String(required=True)
    book_isbn = graphene.String(required=True)
        

class Query(graphene.ObjectType):
    book = graphene.Field(Book, id=graphene.Int(required=True))
    hello = graphene.String()
    books = graphene.List(Book)

    def resolve_book(self, info, id):
        try:
            return Books.objects.filter(pk=id).get()
        except Books.DoesNotExist:
            return None
        
    def resolve_books(self, info):
        try:
            return Books.objects.all()
        except Books.DoesNotExist:
            return None
    
    def resolve_hello(self, info):
        try:
            return "API IS UP!"
        except Exception:
            return None


class CreateBook(graphene.Mutation):
    book = graphene.Field(Book)
    class Arguments:
        data = BookInput(required=True)
    def mutate(self, info, data):
        book_data = data
        book = Books(**book_data)
        book.save()
        return CreateBook(book=book)


class UpdateBook(graphene.Mutation):
    book = graphene.Field(Book)

    class Arguments:
        id = graphene.Int(required=True)
        data = BookInput(required=True)

    def mutate(self, info, id, data):
        try:
            book_data = data
            book_found = Books.objects.get(pk=id)
            book_found.book_name = book_data.book_name
            book_found.book_desc = book_data.book_desc
            book_found.book_isbn = book_data.book_isbn
            book_found.save()
            return UpdateBook(book=book_found)
        except Books.DoesNotExist:
            return None

class DeleteBook(graphene.Mutation):
    success = graphene.Boolean()
    deleted_id = graphene.Int()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        try:
            deleted_id = id
            book = Books.objects.get(pk=id)
            book.delete()
            return DeleteBook(success=True, deleted_id=id)
        except Books.DoesNotExist:
            return DeleteBook(success=False, deleted_id=0)


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
