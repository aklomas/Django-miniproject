from django.db import models

# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Image(models.Model):
    image_id = models.CharField(max_length=100, null=True)
    pic = models.FileField("Image", upload_to="uploads/images/")
    DI = models.FileField("DiskImage", upload_to="uploads/diskimages/", null=True)
    upload_date = models.DateTimeField(auto_now_add=True)


@receiver(pre_delete, sender=Image)
def image_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.pic.delete(False)
    instance.DI.delete(False)
