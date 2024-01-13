# CONSTANTS
file_customer = "customer.json"
arr_customer_types = ["loans", "casual", "commercial"]
int_max_minute = 1440
test_run = 5
dict_customer_types = {
    'loans': {
        'time_process': 15,
        'time_wait': 30
    },
    'casual': {
        'time_process': 20,
        'time_wait': 20
    },
    'commercial': {
        'time_process': 10,
        'time_wait': 10
    },
}
dict_shifts = {
    'night': {
        'starts_at': 0,
        'ends_at': 479
    },
    'morning': {
        'starts_at': 480,
        'ends_at': 959
    },
    'noon': {
        'starts_at': 960,
        'ends_at': 1439
    }
}

turkish_names = [
    "Ahmet", "Mustafa", "Fatma", "Emir", "Elif", "Zeynep", "Yusuf", "Esra",
    "Ali", "Selin", "Burak", "Firuza", "Duhan","Gizem", "Can", "Melis", "Ece", "Cem", "Seda",
    "Kaan", "Deniz", "Onur", "Furkan", "Serkan", "Aysel", "Merve",
    "Umut", "Dilara", "Ceren", "Kerem", "Yasemin", "Berk", "Gamze",
    "Talha", "Levent", "Selma", "Serdar", "Tolga", "Meltem", "Burcu",
    "Efe", "Elif Nur", "Batuhan", "Kadir", "Burcu", "Tuncay", "Pelin",
    "Hakan", "Ebru", "Erhan", "Serap", "Zehra", "Emre", "Asuman",
    "Serkan", "Duygu", "Cihan", "Derya", "Alper", "Bilge", "Yavuz", "Aylin", "Alp", "Sibel",
    "Emrah", "Arda", "Tarkan", "Burcu", "Emine", "Oktay", "Esin", "Serkan",
    "Bengi", "Ufuk", "Dilek", "Umut", "Kaan", "Duygu", "Mert", "Funda", "Alp",
    "Erdem"
]
