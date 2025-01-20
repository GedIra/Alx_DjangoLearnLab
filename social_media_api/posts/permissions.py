from rest_framework import permissions

class IsOwnerOrReadOnlyPermission(permissions.BasePermission):
  message = 'Action not allowed.'

  def has_object_permission(self, request, view, obj):
    
    user = request.user
    
    if request.method in permissions.SAFE_METHODS:
      return  True
    else:
      return user == obj.author
