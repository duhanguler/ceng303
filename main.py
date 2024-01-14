# Local
import util, config
import randomGenerator

class ClerkCalculator():
    def __init__(self):
        self.dict_customers = {}
        self.time_minute = 0 #Day starts at 00:00


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
            if minute_at >= config.dict_shifts[shift]['starts_at'] and minute_at <= config.dict_shifts[shift]['ends_at']:
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
    
    ## Test for Check Process

    """def getAvailableClerk(self, shift, time_now, wait_until, process_time):
        # Check if any available clerk for the shift
        for clerk in self.dict_clerks[shift]:
            # Find available clerk
            # Check if clerk available at given time
            if clerk['available_at'] <= time_now:
                clerk['available_at'] = time_now + process_time
                print("Bu clerk müşteriyi bekletmeden " + util.convertMinuteToTime(wait_until) + " 'de işleme aldı: :")
                print(clerk)
                return clerk
            # Check if clerk will be available until wait time exceeds
            if clerk['available_at'] < wait_until:
                clerk['available_at'] = wait_until + process_time
                print("Bu clerk müşteriyi bekletip " + util.convertMinuteToTime(wait_until) + " 'de işleme aldı: :")
                print(clerk)
                return clerk

        # If no available clerk is found, create new one
        new_clerk = {
            'name': randomGenerator.generateName(),
            'available_at': time_now + process_time
        }
        self.dict_clerks[shift].append(new_clerk)
        print("Clerk sayısı yetmediği için şu clerk işe geldi: ")
        print(clerk)
        return new_clerk"""


    # Initiate Runner
    def run(self):
        # Read customer data from file
        self.dict_customers = util.readJsonFile(config.file_customer)
        for minute_at in range(config.int_max_minute):
        #     # Check if any customer came at the minute
            if util.convertMinuteToTime(minute_at) in self.dict_customers:
                customer = self.dict_customers[util.convertMinuteToTime(minute_at)]
                shift = self.findShift(minute_at)
                wait_until = (minute_at + config.dict_customer_types[customer['type']]['time_wait']) % config.int_max_minute
                process_time = config.dict_customer_types[customer['type']]['time_process']
                clerk = self.getAvailableClerk(shift, minute_at, wait_until, process_time)
                self.dict_customers[util.convertMinuteToTime(minute_at)]['clerk_processed'] = clerk['name']

        print(f"Clerk needed for {len(self.dict_customers)} customer \n"
                f"Morning shift: {len(self.dict_clerks['morning'])} \n"
                f"Noon shift: {len(self.dict_clerks['noon'])} \n"
                f"Night shift: {len(self.dict_clerks['night'])}")
        
        util.writeJsonFile(config.file_customer, self.dict_customers)
        # Test case for write processed data
        '''
        print("***************************\n")
        print("Morning Shift Last Process per Clerk\n")
        print(self.dict_clerks['morning'])
        print("***************************\n")
        print("Noon Shift Last Process per Clerk\n")
        print(self.dict_clerks['noon'])
        print("***************************\n")
        print("Night Shift Last Process per Clerk\n")
        print(self.dict_clerks['night'])'''
        



if __name__ == "__main__":
    randomGenerator.generateCustomers(1000)
    myCC = ClerkCalculator()
    myCC.run()