from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
from django import forms

# Register your models here.
class NewsAdmin(SummernoteModelAdmin):
	summernote_note_fields = ('__all__','text')

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

admin.site.register(Post,NewsAdmin)
