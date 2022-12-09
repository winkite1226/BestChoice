from django.db import models
from users.models import User

# Create your models here.
class Festival_Article(models.Model):
    festival_title = models.CharField(max_length=50, default='')  #축제 제목
    festival_desc = models.TextField()  #축제 설명
    festival_address = models.CharField(max_length=50)  #축제 장소
    festival_region = models.CharField(max_length=50)  #축제 지역
    festival_date = models.CharField(max_length=50)  #축제 기간
    festival_image = models.CharField(max_length=100)  #축제 이미지
    festival_price = models.CharField(max_length=30)  # 축제 요금
    festival_cost = models.CharField(max_length=10)  # 무료 or 유료
    festival_start = models.DateField()  #시작일
    festival_end = models.DateField()  #종료일
    #festival_status는 추가할지 고려
    
class Join_Article(models.Model):
    join_author = models.ForeignKey(User,  verbose_name="작성자", on_delete=models.CASCADE)  #모집 작성자
    join_festival = models.ForeignKey(Festival_Article, verbose_name="축제", on_delete=models.CASCADE)  #모집 축제
    join_title = models.CharField(max_length=20)  #모집 제목
    join_count = models.IntegerField(default=0)  #모집 인원
    join_desc = models.TextField()  #모집 설명
    join_period = models.DateTimeField()  #모집 마감일
    join_status = models.BooleanField(default=False) # true일때 모집중, false 종료
    join_created_at = models.DateTimeField(auto_now_add=True) #모집 게시글 생성 시간
    join_updated_at = models.DateTimeField(auto_now= True) #모집 게시글 수정 시간

class Comment(models.Model):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE) # 댓글 작성자
    comment_article = models.ForeignKey(Join_Article, on_delete=models.CASCADE, related_name="comments") # 모집 게시글
    comment_content= models.TextField() # 댓글 내용
    comment_created_at = models.DateTimeField(auto_now_add=True) # 댓글 작성시간
    comment_updated_at = models.DateTimeField(auto_now= True) # 댓글 수정시간
    
class Bookmark(models.Model):
    bookmark_user = models.ForeignKey(User, on_delete=models.CASCADE)  # 북마크한 사용자
    bookmark_festival = models.ForeignKey(Festival_Article, on_delete=models.CASCADE)  # 북마크한 축제게시글