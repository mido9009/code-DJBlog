from django.db import models
from django.utils import timezone

"""
    1 : html widget
    2 : validation
    3 : Best for db
"""

"""
post:
    - title
    - content
    - draft
    - publis_data
    - author
    - image
    - tags
    - category
    - comments

"""

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=20000)
    draft = models.BooleanField(default=True)   
    publish_date = models.DateTimeField(default=timezone.now)
    # publish_date2 = models.DateTimeField(auto_now=True)




    def __str__(self) -> str:
        return self.title