from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission): # 커스텀을 위해서 상속받아와야함.
    # GET:누구나, PUT/PATCH:해당유저

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # Safe_methods는 데이터에 영향을 미치지 않는 메소드 = GET을 의미
            return True
        return obj.user == request.user # put/patch는 일치하는 경우에만 true
    