from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# admin.site.register(Question)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Poll Question Title ...', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text', 'choice_text']


admin.site.register(Question, QuestionAdmin)
