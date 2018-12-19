from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from friendship.models import Friend,Follow,Block

# Create your models here.
class Profile(models.Model):
  pic = models.ImageField(upload_to='images/',blank=True)
  user = models.OneToOneField(User,null = True,on_delete=models.CASCADE,related_name = "profile")
  bio = models.TextField()
     


  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
        if created:
                Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
            instance.profile.save()

  post_save.connect(save_user_profile, sender=User)

  def __str__(self):
    return self.bio

  def save_profile(self):
    self.save()

  def update_profile(self):
    self.update()

  def delete_profile(self):
    self.delete()


  @classmethod
  def search_profile(cls, name):
    profile = Profile.objects.filter(user__username__icontains = name)
    return profile
    
  @classmethod
  def get_profile_by_id(cls, id):
      user_profile = Profile.objects.get(user=id)
      return user_profile

  @classmethod
  def get_profile_by_username(cls, user):
      profile_info = cls.objects.filter(user__contains=user)
      return profile_info

class Image(models.Model):
  name = models.CharField(max_length=50)
  image = models.ImageField(upload_to = 'images/',blank=True)
  caption = models.TextField(blank = True)
  posted_on = models.DateTimeField(auto_now_add=True)
  profile = models.ForeignKey(User, blank=True,on_delete = models.CASCADE)
  details = models.ForeignKey(Profile, null=True)

  def __str__(self):
      return self.name

  class Meta:
        ordering = ['posted_on']

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

  def update_caption(self):
    self.update()

  @classmethod
  def get_images_on_profile(cls,profile):
      images = Image.objects.filter(profile__pk = profile)
      return images

  @property
  def count_likes(self):
      likes = self.likes.count()
      return likes

  
  @property
  def count_comments(self):
      comments = self.comments.count()
      return comments

class Comment(models.Model):
    image = models.ForeignKey(Image,blank=True, on_delete=models.CASCADE,related_name='comment')
    commenter = models.ForeignKey(User, blank=True)
    comment_itself= models.TextField()


    def delete_comment(self):
        self.delete()
    
    def save_comment(self):
        self.save()

    @classmethod
    def get_comments_on_image(cls, id):
        the_comments = Comment.objects.filter(image__pk=id)
        return the_comments


    def __str__(self):
        return self.comment_itself



class Likes(models.Model):
    who_liked=models.ForeignKey(User,on_delete=models.CASCADE, related_name='likes')
    liked_image =models.ForeignKey(Image, on_delete=models.CASCADE, related_name='likes')

    def save_like(self):
        self.save() 

    def __str__(self):
      return self.who_liked

