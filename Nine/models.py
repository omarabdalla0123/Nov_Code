from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name="posts")
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "categories"
def __str__(self):
        return f"Comment by {self.name} on {self.post}"




class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    posts = models.ManyToManyField(Post, related_name="tags", blank=True)

    def __str__(self):
        return self.name
    

    class Comment(models.Model):
        post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="comments")
        name = models.CharField(max_length=80)
        text = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
    

class Author(models.Model):
    pass