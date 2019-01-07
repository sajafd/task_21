from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
	message = "You are not the owner of this article. Go away! You're naughty..."

	def has_object_permission(self, request, view, obj): 
		if obj.added_by == request.user:
			return True 
		else: 
			return False
