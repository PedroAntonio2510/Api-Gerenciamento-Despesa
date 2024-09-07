from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ExpenseModelViewSet, CategoryModelViewSet

router = DefaultRouter()
router.register('category', CategoryModelViewSet)
router.register('expense', ExpenseModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
