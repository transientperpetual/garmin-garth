import garth
from garth.exc import GarthException
import json
from datetime import date

garth.resume("~/.garth")

try:
    username = garth.client.username
    # Had to remove profile_image_uuid from the list of attributes in the UserProfile class in order to get this to work
    user_profile = garth.UserProfile.get()
    print(user_profile)
    
except GarthException as e:
        print(f"Caught an exception: {e.msg}")
    