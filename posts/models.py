from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile


# 저자, 저자_프로필, 제목, 카테고리, 본문, 이미지, 좋아요_누른_사람들, 글이_올라간_시간
# 이 아래 하나 변수들이 하나의 필드들이다.
class Post(models.Model):
    # user = User.objects.get(pk=1)
    # posts = user.posts.all()
    # 위의 세팅은 유저가 post에 접근하지 못하는 점을 해결.
    # author랑 likes는 related_name을 지정하지 않는다면 참조할 수 없다. post_set.all()이 되어버리기 때문에 둘이 구분이 되지 않는다.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    body = models.TextField()
    image = models.ImageField(upload_to='post/', default='default.png')
    likes = models.ManyToManyField(User, related_name='like_posts', blank=True)  # OneToOne처럼 다대다 관계를 표시할때 사용
    published_date = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    # ForeignKey로 유저, 프로필, 포스트와 연결함. 텍스트만 추가.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()