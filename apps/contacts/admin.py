from django.contrib import admin
from grappelli_nested.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from .models import NotificationMethod, Contact, ContactGroup, ContactGroupRelations 

class NotificationMethodAdmin(admin.ModelAdmin):
    model = NotificationMethod

class ContactAdmin(admin.ModelAdmin):
    model = Contact

class ContactGroupAdmin(admin.ModelAdmin):
    model = ContactGroup
    
class ContactGroupRelationsAdmin(admin.ModelAdmin):
    model = ContactGroupRelations

admin.site.register(NotificationMethod, NotificationMethodAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactGroup, ContactGroupAdmin)
admin.site.register(ContactGroupRelations, ContactGroupRelationsAdmin)

