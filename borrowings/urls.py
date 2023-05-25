from borrowings.views import BorrowingViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = "borrowing"

router = DefaultRouter()
router.register("", BorrowingViewSet)

urlpatterns = [
    path("return-borrowing/<int:pk>/", BorrowingViewSet.as_view({"post": "return_borrowing"}), name="return-borrowing"),
] + router.urls
