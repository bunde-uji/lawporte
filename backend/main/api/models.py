from django.db import models as m
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

MAX_LENGTH = 500
class AbstractModel(m.Model):
    created = m.DateTimeField(auto_now_add=True)
    updated = m.DateTimeField(auto_now=True)
    flag = m.BooleanField(default=True)

    class Meta:
        abstract=True
        ordering = ('-created',)

# Create your models here.


class User(AbstractUser):
    REQUIRED_FIELDS = []


class ArticleCategory(AbstractModel):
    name = m.CharField(max_length=MAX_LENGTH)


class Article(AbstractModel):
    title = m.CharField(max_length=MAX_LENGTH)
    thumbnail = m.ImageField(upload_to='articles')
    content = m.TextField()
    category = m.ForeignKey(ArticleCategory, on_delete=m.CASCADE)


class NewsLetter(AbstractModel):
    names = m.CharField(max_length=MAX_LENGTH)
    email = m.EmailField(max_length=MAX_LENGTH)





class DownloadCategory(AbstractModel):
    name = m.CharField(max_length=MAX_LENGTH)
    


    


class Download(AbstractModel):
    title = m.CharField(max_length=MAX_LENGTH)
    description = m.TextField(max_length=MAX_LENGTH)
    file_format = m.TextField(max_length=10, editable=False, blank=True)
    size = m.CharField(max_length=20)
    file = m.FileField(upload_to='downloads')






class JournalCategory(AbstractModel):
    name = m.CharField(max_length=MAX_LENGTH)
    parent = m.ForeignKey('JournalCategory', on_delete=m.CASCADE)






class JournalAuthor(AbstractModel):
    names = m.CharField(max_length=MAX_LENGTH)
    title = m.CharField(max_length=MAX_LENGTH)






class Journal(AbstractModel):
    title = m.CharField(max_length=MAX_LENGTH)
    abstract = m.TextField()
    keywords = m.CharField(max_length=MAX_LENGTH)
    issue_number = m.CharField(max_length=MAX_LENGTH)
    publication_date = m.DateField()
    file = m.FileField(upload_to='journals')
    price = m.PositiveIntegerField(default=0)
    authors = m.ManyToManyField(JournalAuthor)
    categories = m.ManyToManyField(JournalCategory)




class JournalPurchase(AbstractModel):
    code = m.CharField(primary_key=True, max_length=MAX_LENGTH)
    amount = m.PositiveIntegerField()
    journal = m.ForeignKey(Journal, on_delete=m.CASCADE)
    


class Quiz(AbstractModel):
    title = m.CharField(max_length=MAX_LENGTH)
    description = m.TextField()
    end_date = m.DateField()


class QuizPost(AbstractModel):
    quiz = m.ForeignKey(Quiz, on_delete=m.CASCADE)
    names = m.CharField(max_length=MAX_LENGTH)
    email = m.EmailField(max_length=MAX_LENGTH)
    phone = m.CharField(max_length=MAX_LENGTH)
    content = m.TextField()
    likes = m.PositiveIntegerField(default=0, editable=False)

    class Meta(AbstractModel.Meta):
        abstract = False
        ordering = ('-likes')




class PicOfWeekImage(AbstractModel):
    image = m.ImageField(upload_to='pic-of-week')





class PicOfWeek(AbstractModel):
    caption = m.CharField(max_length=MAX_LENGTH)
    likes = m.PositiveIntegerField(default=0, editable=False)
    images = m.ManyToManyField(PicOfWeekImage)