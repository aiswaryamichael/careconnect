# custom permission
from urllib.request import Request

from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):

        # object level permission

        # if obj.user==request.user:
        #     return True

        if request.method=="GET":  # any user can read
            return True

        return request.user==obj.user # only the creator of the object can update or delete

# condition obj.user==request.user check whether the creator of
# object and requested user are same