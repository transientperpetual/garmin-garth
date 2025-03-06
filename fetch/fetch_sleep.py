import garth
from garth.exc import GarthException
import json

garth.resume("~/.garth")

try:
    username = garth.client.username
    sleep_data = garth.connectapi(
    f"/wellness-service/wellness/dailySleepData/{garth.client.username}",
    params={"date": "2025-03-06", "nonSleepBufferMinutes": 60},
    )

    # Define file path
    file_path = "sleep_data.json"
    # Save JSON object to file
    with open(file_path, "w") as file:
        json.dump(sleep_data, file, indent=4)
    print(f"Sleep data saved to {file_path}")
    
except GarthException as e:
        print(f"Caught an exception: {e.msg}")
    