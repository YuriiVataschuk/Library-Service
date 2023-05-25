from rest_framework import viewsets


from borrowings.models import Borrowing
from borrowings.permissions import IsOwnerOrAdmin
from borrowings.serializers import (
    BorrowingDetailSerializer,
    BorrowingCreateSerializer,
    BorrowingReturnSerializer,
)


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = Borrowing.objects.all()
        else:
            queryset = Borrowing.objects.filter(user=user)

        is_active = self.request.query_params.get("is_active")
        if is_active:
            queryset = queryset.filter(actual_return_date__isnull=True)

        user = self.request.query_params.get("user")
        if user and self.request.user.is_staff:
            queryset = queryset.filter(user=user)

        return queryset

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return BorrowingDetailSerializer
        elif self.action == "create":
            return BorrowingCreateSerializer
        elif self.action == "return_borrowing":
            return BorrowingReturnSerializer
        return BorrowingDetailSerializer
