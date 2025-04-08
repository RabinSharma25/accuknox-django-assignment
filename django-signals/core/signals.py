import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, BookLog, Car

@receiver(post_save, sender=Car)
def slow_signal_handler(sender, instance, created, **kwargs):
    if created:
        print("[SIGNAL] Sleeping for 5 seconds...")
        time.sleep(5)
        print("[SIGNAL] Done sleeping.")



# ✅ This signal proves that Django signals run in the same DB transaction and thread as the caller.
@receiver(post_save, sender=Book)
def create_book_log(sender, instance, created, **kwargs):
    if created:
        print(f"[SIGNAL] Running in thread: {threading.current_thread().name}")
        print("[SIGNAL] Creating BookLog...")
        BookLog.objects.create(message=f"Book '{instance.title}' was created.")
        print("[SIGNAL] BookLog created")