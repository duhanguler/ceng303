# Local
import util, config
import randomGenerator


class ClerkCalculator():
    def __init__(self):
        self.dict_customers = {}

        # Start shifts for minimum clerks, so its 1.
        self.dict_clerks = {
            'night': [
                {
                    'name': "Murat",
                    'available_at': 0
                }
            ],
            'morning': [
                {
                    'name': "Mehmet",
                    'available_at': 480
                }
            ],
            'noon': [
                {
                    'name': "Firuza",
                    'available_at': 960
                }
            ],
        }

    # Calculate which shift by minute value
    def findShift(self, minute_at):
        for shift in config.dict_shifts:
            if minute_at >= config.dict_shifts[shift]['starts_at'] and minute_at <= config.dict_shifts[shift][
                'ends_at']:
                return shift
        return None

    def createNewClerk(self):
        return {
            'name': util.generateName(),
            'status': False
        }

    def getAvailableClerk(self, shift, time_now, wait_until, process_time):
        # Check if any available clerk for the shift
        for clerk in self.dict_clerks[shift]:
            # Find available clerk
            # Check if clerk available at given time
            if clerk['available_at'] <= time_now:
                clerk['available_at'] = time_now + process_time
                return clerk
            # Check if clerk will be available until wait time exceeds
            if clerk['available_at'] < wait_until:
                clerk['available_at'] = wait_until + process_time
                return clerk

        # If no available clerk is found, create new one
        new_clerk = {
            'name': randomGenerator.generateName(),
            'available_at': time_now + process_time
        }
        self.dict_clerks[shift].append(new_clerk)
        return new_clerk

    # Initiate Runner
    # def run(self):


