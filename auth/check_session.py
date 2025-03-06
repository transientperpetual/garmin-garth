import garth
from garth.exc import GarthException
import json

garth.resume("~/.garth")

try:
    username = garth.client.username
    print(f"Logged in as {username}")
except GarthException as e:
        print(f"Caught an exception: {e.msg}")