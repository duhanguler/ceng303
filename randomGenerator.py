# Local
import config, util

# External
import random

def generateName():
    return random.choice(config.turkish_names)

def generateMinutes(count):
    return random.sample(range(0, config.int_max_minute), count)

def generateCustomers(count):
    arr_minutes = generateMinutes(count)
    dict_customers = {}
    for minute in arr_minutes:
        # Convert minute to str time
        time_at = util.convertMinuteToTime(minute)
        dict_customers[time_at] = {
            "name": generateName(),
            "type": random.choice(config.arr_customer_types),
            "clerk_processed": ""
        }
    # Write generated customers to json file
    util.writeJsonFile(config.file_customer, dict_customers)