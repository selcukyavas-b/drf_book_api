from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin=super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin

class IsCommentOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.comment_owner
    
    
class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Yalnızca yazar kendi kitabını düzenleyebilir veya silebilir.
    Diğer kullanıcılar sadece okuyabilir.
    """
    
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS (GET, HEAD, OPTIONS) işlemlerine her zaman izin verilir.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Diğer durumlarda, kullanıcı yalnızca kendi kitabını düzenleyebilir veya silebilir.
        return obj.author == request.user
    
    