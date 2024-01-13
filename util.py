# Local
import config

# External
import json
import random

def readJsonFile(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def writeJsonFile(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Calculate minute value by time
def convertTimeToMinute(time):
    hour, minute = time.split(":")
    minute_at = (int(hour*60) + int(minute)) % config.int_max_minute
    return minute_at

# Calculate time by minute value
def convertMinuteToTime(minute_at):
    hour = minute_at // 60
    minute = minute_at % 60
    return f"{hour:02d}:{minute:02d}"