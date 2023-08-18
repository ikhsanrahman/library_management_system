from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import BookViewSet, StudentViewSet, BorrowingViewSet

router = routers.DefaultRouter()
router.register("books", BookViewSet)
router.register("students", StudentViewSet)
router.register("borrowings", BorrowingViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
