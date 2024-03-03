from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) #on_delete 모델에서 데이터 삭제 = 연결된 데이터 삭제
    # primary_key를 User의 pk로 설정하여 통합적으로 관리
    nickname = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    subjects = models.CharField(max_length=128)
    image = models.ImageField(upload_to='profile/', default='default.png')


@receiver(post_save, sender=User)  # post_save의 이벤트 발생 사실로 해당 유저 인스턴스와 연결되는 프로필 데이터를 생성 => (유저 생성 = 프로필 자동생성) 코드
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)