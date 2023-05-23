from rest_framework import routers

from books.views import BookListViewSet

router = routers.DefaultRouter()
router.register("", BookListViewSet)

urlpatterns = router.urls

app_name = "books"
