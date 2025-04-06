'''
Question.No - 02
Do django signals run in the same thread as the caller? Please support your
answer with a code snippet that conclusively proves your stance. The code does not need to be
elegant and production ready, we just need to understand your logic.


Answer:-
Yes, Django signals run in the same thread as the caller by default.
This means any delay or heavy logic inside the signal handler will block the main thread and increase the time taken by the operation (e.g., .save() or .create()).
'''
# To run this file run the command given below
# python3 core/test_signal_thread.py




import time
import threading
import os
import sys
import django

# Add the root of your Django project to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set your Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'signal_demo.settings')

# Setup Django
django.setup()

from core.models import Book

print(f"[MAIN] Running in thread: {threading.current_thread().name}")
print("[MAIN] Saving book...")

start = time.time()
Book.objects.create(title="Thread Test Book")
end = time.time()

print(f"[MAIN] Save done in {end - start:.2f} seconds")

# ✅ This proves Django signals run in the same thread as the caller by printing thread names.
