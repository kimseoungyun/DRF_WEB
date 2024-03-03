from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

# 유저테이블과 프로필 테이블을 같은 모델인 것처럼 함께 볼 수 있는 방법 (유저 모델만 관라지ㅏ 페이지에 등록하게 되면 프로필 모델은 나타나지 X)

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)