from rest_framework import viewsets
from api.models import Category, Expense
from .serializer import CategoryModelSerializer, ExpenseModelSerializer
from dj_rql.drf import RQLFilterBackend
from .filters import CategoryFilterClass, ExpenseFilterClass
from rest_framework import permissions
from api.permissions import ExpenseOwnerPermission


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = CategoryFilterClass
    permission_classes = [permissions.AllowAny]


class ExpenseModelViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = ExpenseFilterClass
    permission_classes = [permissions.DjangoModelPermissions, ExpenseOwnerPermission]
