# Welcome to our CENG303 Project!

Hi! Our project is **Banking Clerks with Python**. 

# About automation

Used integer numbers to represent time by minutes.

It creates customers at a random arrival time and writes a json file
Process reads the data from the json file and starts
1. Checks arrival times by minutes
2. Checks related shift
3. Check for an available clerk and adds a new one if not exist
4. Sets the clerk not available until process time ends
5. Sets the clerk as "clerk_processed" for the customer
6. Write the data to json file
7. Prints how many clerks needed for the customers by shift

# Contributors

No sorting for contributors.

- [M. Duhan Güler](https://github.com/duhanguler)
- [Firuza Rahimova](https://github.com/firagimova)
- [Erham Safa Aksoy](https://github.com/ErhamSafa)
- [Murat Ergin](https://github.com/MurattErginn)
- [Mehmet Yalçın](https://github.com/myalcinnurd)

## How to use?

![Setup Time](https://img.shields.io/badge/Setup_Time-10_min-blue.svg)

**Operating system:** OSX or Linux is recommended although Windows is also supported.

### 1. Install global dependencies

![python 3.5+](https://img.shields.io/badge/python-3.7+-blue.svg)

To check if python3, pip and some of libraries (json, random) is already installed:

```bash
python3 --version
```

<details>
	<summary><b>Install Python3</b></summary>

To install python3 follow instructions [here](https://www.python.org/downloads/)

To install pip - follow instructions [here](https://pip.pypa.io/en/stable/installation/)

</details>
<details>
<summary><b>Install json and random libraries</b></summary>

**Any installation method is fine.**

Recommended:

```bash
python3 -m pip install --user --upgrade pip
python3 -m pip install --user json
python3 -m pip install --user random
```


</details>


### 2. Install project dependencies

Clone the repo

```bash
git clone https://github.com/duhanguler/ceng303
cd ceng303/
```


_**Note:** If you face a distutils error in pip, use `--ignore-installed` flag in above command._

<!-- Wiki should not get cloned -->

### 3. Run the code

1. Run program:
   ```bash
   python3 main.py
   ```


## Project Algorithm and Logic

```mermaid
classDiagram
  class ClerkCalculator {
    - dict_customers: dict
    - time_minute: int
    - dict_clerks: dict

    + findShift(minute_at: int): string
    + createNewClerk(): dict
    + getAvailableClerk(shift: string, time_now: int, wait_until: int, process_time: int): dict
    + run(): void
  }

  class util {
    + readJsonFile(file_path: string): dict
    + writeJsonFile(file_path: string, data: dict): void
    + convertTimeToMinute(time: string): int
    + convertMinuteToTime(minute_at: int): string
  }

  class randomGenerator {
    + generateName(): string
    + generateMinutes(count: int): list
    + generateCustomers(count: int): void
  }

  class config {
    - dict_shifts: dict
    - int_max_minute: int
    - arr_customer_types: list
    - file_customer: string
    - test_run: int
    - dict_customer_types: dict
    - turkish_names: dict
  }

  ClerkCalculator -- util
  ClerkCalculator -- randomGenerator
  ClerkCalculator -- config


```


```mermaid
sequenceDiagram
  participant Customer
  participant ClerkCalculator
  participant util
  participant randomGenerator
  participant config

  Customer ->> ClerkCalculator: generateCustomers(1000)
  ClerkCalculator ->> randomGenerator: generateCustomers(1000)
  randomGenerator ->> util: writeJsonFile(config.file_customer, data)
  ClerkCalculator ->> util: readJsonFile(config.file_customer)
  loop for each minute_at in range(config.int_max_minute)
    ClerkCalculator ->> ClerkCalculator: run() for each minute
    ClerkCalculator ->> util: convertMinuteToTime(minute_at)
    ClerkCalculator ->> util: readJsonFile(config.file_customer)
    ClerkCalculator ->> ClerkCalculator: findShift(minute_at)
    ClerkCalculator ->> ClerkCalculator: getAvailableClerk(self, shift, time_now, wait_until, process_time)
    ClerkCalculator ->> util: convertMinuteToTime(wait_until)
    ClerkCalculator ->> util: writeJsonFile(config.file_customer, dict_customers)
  end
  ClerkCalculator ->> util: writeJsonFile(config.file_customer, dict_customers)

```


