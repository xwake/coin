from django.db import models
from django.contrib import admin
import datetime

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 40)
    createtime = models.DateField(auto_now_add=True)

class Catalog(models.Model):
    cname = models.CharField(max_length = 40)
    creater = models.ForeignKey(User,default='1')
    createtime = models.DateField(auto_now_add=True)


class BlogPost(models.Model):
  title = models.CharField(max_length = 150)
  body = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)

  class Meta:
        ordering = ('-timestamp',)

class SourceLink(models.Model):
  title = models.CharField(max_length = 150)
  link = models.CharField(max_length = 300)
  targetregex = models.CharField(max_length = 300)
  key1 = models.CharField(max_length = 50,null=True,blank=True,default="")
  key2 = models.CharField(max_length = 50,null=True,blank=True,default="")
  key3 = models.CharField(max_length = 50,null=True,blank=True,default='')
  key4 = models.CharField(max_length = 50,null=True,blank=True,default='')
  key5 = models.CharField(max_length = 50,null=True,blank=True,default='')
  key6 = models.CharField(max_length = 50,null=True,blank=True,default='')
  key7 = models.CharField(max_length = 50,null=True,blank=True,default='')
  key8 = models.CharField(max_length = 50,null=True,blank=True,default='')
  key9 = models.CharField(max_length = 50,null=True,blank=True,default='')
  createtime = models.DateField(auto_now_add=True)
  updatetime = models.DateField(auto_now=True)
  creater = models.ForeignKey(User,default='1')
  catalog = models.ForeignKey(Catalog)
  status = models.IntegerField(max_length = 2)

  class Meta:
        ordering = ('-createtime',)

class UrlResult(models.Model):
  title = models.CharField(max_length = 150)
  link = models.CharField(max_length = 300)
  createtime = models.DateTimeField(auto_now_add=True,default=datetime.datetime.now())
  hashid = models.IntegerField()
  srclinkid = models.ForeignKey(SourceLink)

  class Meta:
        ordering = ('-createtime',)


class BlogPostAdmin(admin.ModelAdmin):
  list_display = ('title','timestamp')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','createtime')

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('cname','creater','createtime')

class SourceLinkAdmin(admin.ModelAdmin):
  list_display = ('title','link','createtime','updatetime')

class UrlResultAdmin(admin.ModelAdmin):
  list_display = ('title','link','createtime')


class TestTask(models.Model):
    ttname = models.CharField(max_length = 20)
    ttname2 = models.CharField(max_length = 20)

    def printSome (self):
        print 'tasks.str is print...'

    class Meta:
        ordering = ('-ttname',)

class TestTaskAdmin(admin.ModelAdmin):
    list_display = ('ttname','ttname2')


admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(SourceLink,SourceLinkAdmin)
admin.site.register(UrlResult,UrlResultAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Catalog,CatalogAdmin)
admin.site.register(TestTask,TestTaskAdmin)
