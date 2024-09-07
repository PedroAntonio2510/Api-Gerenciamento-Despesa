from django.contrib import admin
from .models import Expense, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'expense', 'category', 'description', 'value', 'date', 'owner', 'created_at', 'updated_at']
    search_fields = ('expense',)
    list_filter = ('category', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Expense, ExpenseAdmin)
