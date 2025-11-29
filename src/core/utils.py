from datetime import datetime
import random

from datetime import datetime
import random

def generate_id():
    now = datetime.now()
    random_num = random.randint(100, 999)
    id = f"{now.hour:02d}{now.minute:02d}{random_num}"
    
    return id


def get_datetime_str():
    now = datetime.now()
    return f"{now.day}/{now.month}/{now.year}-{now.hour}:{now.minute}:{now.second}::{now.microsecond%100}"


def get_date_str():
    now = datetime.now()
    return f"{now.day}/{now.month}/{now.year}"