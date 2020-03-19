from django.db import models

# Create your models here.
class Edit(models.Model):
    price = models.CharField(max_length=120, default='')
    about = models.TextField(default='')
    coment = models.TextField(default='')
    image = models.FileField(null=True, blank=True)
    def get_absolute_url(self):
        return "/%s/" % (self.id)

class FeedFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    feed = models.ForeignKey(Edit, on_delete=models.CASCADE, related_name='files')