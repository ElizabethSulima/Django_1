from django.contrib import admin
from .models import Article, Tag, Scope

from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            cleaned_data = form.cleaned_data
            if 'is_main' in cleaned_data and cleaned_data['is_main']:
                if self.instance.pk:
                    raise ValidationError('Основной тэг может быть указан только один раз')
                else:
                    if self.initial[0].get('is_main', False):
                        raise ValidationError('Ошибка: Основной тэг уже выбран')
                    else:
                        pass
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Tag
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.site.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.site.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
