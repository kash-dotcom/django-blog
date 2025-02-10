from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_posts")
    featureed_image = CloudinaryField("image", default="image/upload/v1629780000/default.jpg")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE, related_name="comments",
                             null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="comments_author")
    body = models.TextField(default="")
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    challenge = models.FloatField(default=3.5)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
