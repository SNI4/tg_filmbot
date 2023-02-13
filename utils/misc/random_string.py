from random import choice
from string import ascii_letters, digits


async def random_string(length=8):
    return ''.join(choice(ascii_letters + digits) for i in range(length))
