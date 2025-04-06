'''
Question.No - 01
By default are django signals executed synchronously or asynchronously? Please
support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic

Answer:-
Django signals are executed synchronously by default. This means that any signal handler will block the flow of code until it finishes. I proved this by adding a time.sleep(5) in a post_save signal and measuring the time it took for .create() to return. It clearly waited ~5 seconds, showing the signal runs inline with the calling process.

'''


import os
import sys
import django
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'signal_demo.settings')
django.setup()

from core.models import Car

print("[MAIN] Creating Car...")
start = time.time()
Car.objects.create(name="Tesla Model 3")

end = time.time()
print(f"[MAIN] Done. Time taken: {end - start:.2f} seconds")
