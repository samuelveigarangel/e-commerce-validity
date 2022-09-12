from uuid import uuid4


def random_number():
    number_order = str(uuid4())[:13].upper()
    return number_order
