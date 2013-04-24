from django.contrib import admin
from fluent_blogs.admin.entryadmin import AbstractEntryBaseAdmin, EntryAdmin
from fluent_blogs.models import get_entry_model, Entry

__all__ = (
    'AbstractEntryBaseAdmin', 'EntryAdmin',
)


# Ony register the admin when the entry model is not customized.
if get_entry_model() is Entry:
    admin.site.register(Entry, EntryAdmin)
