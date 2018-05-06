from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,verbose_name='Yazar',on_delete=models.CASCADE,related_name='posts')
    title=models.CharField(max_length=120,verbose_name='Başlık')
    content=RichTextField(verbose_name='Icerik')
    publising_Date=models.DateTimeField(verbose_name='Yayınlanma Tarihi',auto_now=True)
    image=models.ImageField(null=True,blank=True)
    slug=models.SlugField(unique=True,editable=False,max_length=130)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post:detail',kwargs={'slug':self.slug})
        #return "/post/{}".format(self.id)
    def get_update_url(self):
        return reverse('post:update',kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('post:delete',kwargs={'slug':self.slug})

    def get_create_url(self):
        return reverse('post:create')

    def get_unique_slag(self):
        slug=slugify(self.title.replace('ı','i'))
        unique_slug=slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug='{}-{}'.format(slug,counter)
            counter +=1
        return unique_slug

    def save(self,*args,**kwargs):
        self.slug = self.get_unique_slag()
        return super(Post,self).save(*args,**kwargs)

    class Meta:
        ordering=['-publising_Date']


class Comment(models.Model):
    post=models.ForeignKey('post.Post',related_name='comments',on_delete=models.CASCADE)
    name =models.CharField(max_length=200,verbose_name='İsim')
    content=models.TextField(verbose_name='Yorum')
    created_date=models.DateTimeField(auto_now_add=True)
