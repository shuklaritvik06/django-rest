from django.contrib import admin
from crud.models import Books, Authors


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "type")
    search_fields = ("title",)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone", "about")
    search_fields = ("name",)


admin.site.register(Books, BookAdmin)
admin.site.register(Authors, AuthorAdmin)
