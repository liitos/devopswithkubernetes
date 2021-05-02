import random
import string
import time
from datetime import datetime, timezone

result_str = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + '-', k = 40))

while True:
    now = datetime.now()
    fnow = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    print(f"{fnow}: {result_str}")
    time.sleep(5.0)

