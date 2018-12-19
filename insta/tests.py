from django.test import TestCase
from .models import Profile, Image, Comment
from django.contrib.auth.models import User

class ProfileTestClass(TestCase):
    '''
    Tests the profile class and its functions and methods
    '''
    def setUp(self):
      
        self.profile = Profile(bio='bio example', pic='example.jpeg')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        '''
        Function that tests whether user profile is being saved
        '''
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_method(self):
        '''
        Function that tests whether user profile info can be deleted
        '''
        self.profile.save_profile()
        self.profile.delete_profile()




class ImageTestClass(TestCase):
    '''
    Tests the Image class and its functions and methods
    '''
    def setUp(self):
        self.image = Image(name='example', caption='example caption')
        self.image.save_image()
 
        self.image = Image(name='example',image='example.jpg', caption='example caption', posted_on='two minutes ago', profile=self.profile)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        '''
        Function that tests whether an image is saved to database
        '''
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        '''
        Function that tests whether an image can be deleted from the database
        '''
        self.image.save_image()
        self.image.delete_image()

    
    def test_update_method(self):
        """
        Function to test that an image's details can be updated
        """
        self.image.save_image()
        new_image = Image.objects.filter(caption='example caption').update(caption='example')
        images = Image.objects.get(caption='example')
        self.assertTrue(images.caption, 'example')
    

class CommentTestClass(TestCase):
    '''
    Tests the Comment class and its functions and methods
    '''
    def setUp(self):
      self.comment = Comment(comment_itself='skjlKDL',)

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_method(self):
        '''
        Function that tests whether a comment is being saved to the database
        '''
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_method(self):
        '''
        Function that tests whether a comment can be deleted
        '''
        self.comment.save_comment()
        self.comment.delete_comment()




       