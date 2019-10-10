from django.utils.translation import ugettext_lazy as _, ugettext
from django.contrib import admin
from django.forms.widgets import Textarea, TextInput
from adminsortable.admin import NonSortableParentAdmin, SortableTabularInline
from . import models
from django.db.models import TextField, CharField


class TextWidget(Textarea):
    def __init__(self, attrs=None):
        default_attrs = {'cols': '26', 'rows': '3'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)


class CharsWidget(TextInput):
    def __init__(self, attrs=None):
        default_attrs = {'size': '18'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)


class InputSettingsFieldInline(SortableTabularInline):
    model = models.InputSettingsField
    fields = ('input_name', 'output_name', 'date_format', 'default_value',
        'exclude_if_empty', 'omit', 'example_value')
    formfield_overrides = {
        TextField: {'widget': TextWidget},
        CharField: {'widget': CharsWidget},
    }


class InputSettingsAdmin(NonSortableParentAdmin):
    list_display = ('name', 'default_format', 'uid', 'webhook')
    readonly_fields = ('uid', 'webhook',)
    fields = ('uid', 'name', 'description', 'default_format', 'webhook')
    inlines = [InputSettingsFieldInline]
    actions = ['update_field_definitions']

    def webhook(self, obj):
        return "asñdfjalkdsjflksajdflksad"
        return obj.get_webhook_url()
    webhook.short_description = _("Webhook")

    def get_fields(self, request, obj=None):
        if obj is None:
            return ('name', 'description', 'default_format')
        return ('uid', 'name', 'description', 'default_format', 'webhook')

    def update_field_definitions(self, request, queryset):
        for settings in queryset:
            settings.update_field_definitions()
        self.message_user(request, ugettext("Updated field definitions"))
    update_field_definitions.short_description = _("Update field definitions")


class InputAdmin(admin.ModelAdmin):
    list_display = ('settings', 'format', 'internal_source', 'processed',
        'modified', 'raw_content')
    list_filter = ('format', 'internal_source', 'processed', 'created',
        'modified', 'settings')
    actions = ['update_field_definitions']
    
    def get_fields(self, request, obj=None):
        if obj is None:
            return ('settings', 'format', 'processed', 'raw_content')
        return ('settings', 'internal_source', 'format', 'processed', 'raw_content',
            'created', 'modified')

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return []
        return self.get_fields(request, obj)

    def update_field_definitions(self, request, queryset):
        for settings in queryset:
            settings.update_field_definitions()
        self.message_user(request, ugettext("Updated field definitions"))
    update_field_definitions.short_description = _("Update field definitions")

admin.site.register(models.InputSettings, InputSettingsAdmin)
admin.site.register(models.Input, InputAdmin)
