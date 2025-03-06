import garth
from garth.exc import GarthException
import json
from datetime import date

garth.resume("~/.garth")

try:
    username = garth.client.username
    
    # Define the date for which you want to retrieve stress data (last number represents number of weeks to fetch data for)
    # end_date = date.today().isoformat()
    end_date = "2025-03-02"
    steps_data = garth.DailySteps.list(end=end_date, period=1)
    print(steps_data)
    
except GarthException as e:
        print(f"Caught an exception: {e.msg}")
    