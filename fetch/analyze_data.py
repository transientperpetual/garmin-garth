import garth
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import json
import garth
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import json

garth.resume("~/.garth")

# Fetch sleep data for a specific date
sleep_data = garth.connectapi(
    f"/wellness-service/wellness/dailySleepData/{garth.client.username}",
    params={"date": "2025-01-12", "nonSleepBufferMinutes": 60},
)

# Print full sleep data for debugging
print(json.dumps(sleep_data, indent=2))

# Extract sleep stages
stages = sleep_data.get("sleepLevelsMap", {}).get("sleep", [])

if not stages:
    print("No sleep stage data found!")
    exit()

# Convert timestamps & extract levels
timestamps = []
levels = []
for stage in stages:
    if "startTimeInSeconds" in stage and "activityLevel" in stage:
        timestamps.append(datetime.fromtimestamp(stage["startTimeInSeconds"]))
        levels.append(stage["activityLevel"])
    else:
        print("Missing data in:", stage)

# Map sleep stages
stage_mapping = {1: "Awake", 2: "Light", 3: "Deep", 4: "REM"}
stage_colors = {"Awake": "red", "Light": "yellow", "Deep": "blue", "REM": "purple"}

stage_labels = []
for level in levels:
    if level in stage_mapping:
        stage_labels.append(stage_mapping[level])
    else:
        print(f"Unknown sleep stage: {level}")
        stage_labels.append("Unknown")

# Create DataFrame
df = pd.DataFrame({"Time": timestamps, "Stage": stage_labels})

# Ensure we have data
if df.empty:
    print("No valid sleep data to plot!")
    exit()

# Plot
plt.figure(figsize=(12, 5))
plt.scatter(df["Time"], df["Stage"], c=df["Stage"].map(stage_colors), edgecolors="black", s=50)
plt.plot(df["Time"], df["Stage"], linestyle="-", alpha=0.5, color="black")

plt.xlabel("Time")
plt.ylabel("Sleep Stage")
plt.title(f"Sleep Stages for {sleep_data.get('calendarDate', 'Unknown')}")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
