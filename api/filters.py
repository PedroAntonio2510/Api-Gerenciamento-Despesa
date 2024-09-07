from dj_rql.filter_cls import AutoRQLFilterClass
from api.models import Category, Expense


class CategoryFilterClass(AutoRQLFilterClass):
    MODEL = Category


class ExpenseFilterClass(AutoRQLFilterClass):
    MODEL = Expense
    FILTERS = [
        {'filter': 'category', 'source': 'category__name', },
        {'filter': 'owner', 'source': 'owner__username', }
    ]
