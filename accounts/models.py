from django.db.models import *

class Author(Model):
    author = CharField(
        'author',
        max_length=256
    )
   
    img = ImageField(
        'img of the post',
        upload_to='accounts_img/'
    )

    def __str__(self):
        return f'{self.author}'  
