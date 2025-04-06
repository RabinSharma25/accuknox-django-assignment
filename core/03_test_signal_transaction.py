'''
Answer:-
Yes, by default, Django signals like post_save run within the same database transaction as the caller.
This means: if you raise an exception inside the signal or the main code, everything gets rolled back.

✅ Goal:
We will create a Book, trigger a post_save signal that creates a related BookLog, and then raise an exception after both are called — if the transaction is truly atomic, neither Book nor BookLog will be saved.


'''

import os
import sys
import django

# Django setup
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "signal_demo.settings")
django.setup()

from django.db import transaction
from core.models import Book, BookLog

try:
    with transaction.atomic():
        print("[MAIN] Creating Book...")
        Book.objects.create(title="Transactional Signal Test")
        print("[MAIN] Raising Exception to trigger rollback...")
        raise Exception("Forcing rollback after save.")
except Exception as e:
    print(f"[MAIN] Caught exception: {e}")

# Checking if any data was saved
book_exists = Book.objects.filter(title="Transactional Signal Test").exists()
log_exists = BookLog.objects.filter(message__icontains="Transactional Signal Test").exists()

print(f"\n[RESULT] Book exists? {book_exists}")
print(f"[RESULT] BookLog exists? {log_exists}")


# ✅ This proves:
# Django signals (like post_save) are run inside the same DB transaction.
# If an exception is raised after the model is saved, both the model and signal-created data are rolled back.
