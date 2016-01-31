from django.contrib import admin
from grappelli_nested.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from .models import Check, CheckAttribute, CheckType, CheckTypeAttribute

class CheckAttributeAdmin(NestedTabularInline):
    model = CheckAttribute
    max_num = 0
    extra = 0

class CheckAdmin(admin.ModelAdmin):
    model = Check
    inlines = [ CheckAttributeAdmin ]
    fieldsets  = (
            (None, {
                'fields' : [ 'label', 'check_type', 'check_interval', 'max_confirmations' ],
                }),
            )
    list_display = [ 'label', 'check_type', 'check_interval', 'max_confirmations' ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

class CheckTypeAttributeInline(NestedTabularInline):
    model = CheckTypeAttribute

class CheckTypeAdmin(admin.ModelAdmin):
    model = CheckType
    inlines = [ CheckTypeAttributeInline ]

admin.site.register(CheckType, CheckTypeAdmin)
admin.site.register(Check, CheckAdmin)
