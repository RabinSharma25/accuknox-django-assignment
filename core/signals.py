import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book

@receiver(post_save, sender=Book)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal started...")
    time.sleep(5)
    print("Signal finished.")
