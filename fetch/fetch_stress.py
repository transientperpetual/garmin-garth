import garth
from garth.exc import GarthException
import json
from datetime import date

garth.resume("~/.garth")

try:
    username = garth.client.username
    
    # Define the date for which you want to retrieve stress data (last number represents number of weeks to fetch data for)
    stress_data = garth.connectapi("/usersummary-service/stats/stress/weekly/2025-03-05/3")
    print(stress_data)

    # Define file path
    file_path = "stress_data.json"
    # Save JSON object to file
    with open(file_path, "w") as file:
        json.dump(stress_data, file, indent=4)
    print(f"Sleep data saved to {file_path}")
    
except GarthException as e:
        print(f"Caught an exception: {e.msg}")
    