from django.urls import path
from rest_framework.routers import DefaultRouter

from borrowings.views import BorrowingViewSet

app_name = "borrowing"

router = DefaultRouter()
router.register("", BorrowingViewSet)

urlpatterns = router.urls
