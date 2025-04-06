import time
from core.models import Book

def run():
    print("Saving book...")
    start = time.time()
    Book.objects.create(title="Signal Example")
    end = time.time()
    print(f"Save done in {end - start:.2f} seconds")
