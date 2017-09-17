from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_persmission(self, request, view, obj):
        return obj.user == request.user
