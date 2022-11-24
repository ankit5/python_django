from django.contrib import admin

from .models import Book
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ["id", "title", "description"]
  search_fields  = ['title']
  list_editable = (
        'title',
    )
