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



    # Initiate Runner
    def run(self):
        #Fill
        
        

        



'''if __name__ == "__main__":
    #Fill'''