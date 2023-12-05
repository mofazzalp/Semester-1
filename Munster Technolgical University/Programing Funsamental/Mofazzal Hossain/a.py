import random
from datetime import datetime
activity_log = open("logs.txt", "a")
custom_format = datetime.now().strftime("%B %d, %Y %H:%M")


print("Example 4:", custom_format)
