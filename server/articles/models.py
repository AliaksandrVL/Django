from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField()
    content = models.TextField()
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' - '.join([self.name, str(self.created)])