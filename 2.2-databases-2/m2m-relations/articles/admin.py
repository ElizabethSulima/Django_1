from django.contrib import admin
from .models import Article, Tag, Scope

from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            cleaned_data = form.cleaned_data
            if cleaned_data:
                print("Содержимое cleaned_data для формы:")
                for key, value in cleaned_data.items():
                    print(f"{key}: {value}")
                raise ValidationError('Тут всегда ошибка')

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
