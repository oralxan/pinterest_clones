from django.db.models import *
from django.contrib.auth.models import User
from accounts.models import Author
class Post(Model):
    name = CharField(
        'name of the post',
        max_length=512
    )
    descriptions = TextField(
        'descriptions for the post'
    )
    img = ImageField(
        'image of the post',
        upload_to='pinterest_img/'
    )
    author  = ForeignKey(
        User,
        verbose_name='Author',
        on_delete=CASCADE
    )
    
    date = DateField(
        'date of the post'
    )
    
  
   
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name  = 'post'
        verbose_name_plural = 'posts'
        ordering = ('date',)

