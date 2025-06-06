import os
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    print("Video wurde gespeichert")
    if created:
        print("new video created")

def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Kommentare
    """
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)

# post_save.connect(video_post_save, sender=Video)
# pre_delete.connect(video_post_save, sender=Video)

# apps.py

# def ready(self):
#     import DEIN_APP

# settings.py
#     content.apps.ContentConfig


# FFmpeg -> Systemumgebungsvariablen
