import pandas as pd

# Определение данных об оборудовании
equipment_data = {
    "Excavator": {
        "type": "Excavator",
        "capacity": 20,  # тонны
        "dig_depth": 6,  # метры
        "swing_radius": 10,  # метры
        "ground_type": ["Soft", "Hard", "Rock"],
        "weather": ["Sunny", "Rain", "Snow"],
        "cost": 1000,  # в час
    },
    "Bulldozer": {
        "type": "Bulldozer",
        "blade_width": 3,  # метры
        "horsepower": 150,
        "ground_type": ["Soft", "Hard"],
        "weather": ["Sunny", "Rain", "Snow"],
        "cost": 500,  # в час
    },
    "Crane": {
        "type": "Crane",
        "capacity": 50,  # тонны
        "boom_length": 50,  # метры
        "jib_length": 20,  # метры
        "ground_type": ["Hard"],
        "weather": ["Sunny", "Rain", "Windy"],
        "cost": 1500,  # в час
    },
}

# Определение данных о типе грунта
ground_type_data = {
    "Soft": {
        "description":
            "Soft ground, such as sand or loose soil",
        "restrictions": [
            "Excavator (dig depth)", "Bulldozer (horsepower)",
            "Crane (ground type)"
        ],
    },
    "Hard": {
        "description":
            "Hard ground, such as compacted soil or gravel",
        "restrictions": [
            "Excavator (dig depth)", "Bulldozer", "Crane (ground type)"
        ],
    },
    "Rock": {
        "description":
            "Solid rock, requiring additional equipment",
        "restrictions": [
            "Excavator (dig depth)", "Bulldozer", "Crane (ground type)"
        ],
    },
}

# Определение погодных данных
weather_data = {
    "Sunny": {
        "description": "Ясная и солнечная погода",
        "restrictions": []
    },
    "Rain": {
        "description":
            "Дождливая погода может повлиять на состояние грунта",
        "restrictions": [
            "Excavator (ground type)", "Bulldozer (ground type)",
            "Crane (ground type)"
        ],
    },
    "Snow": {
        "description":
            "Снежная погода может повлиять на состояние грунта и доступ к нему",
        "restrictions": [
            "Excavator (ground type)", "Bulldozer (ground type)",
            "Crane (ground type)"
        ],
    },
    "Windy": {
        "description": "Ветреная погода может повлиять на работу крана",
        "restrictions": ["Crane (weather)"],
    },
}


def get_equipment_options(order_params):
	# Проверьте, нет ли неправильного типа грунта или погодных условий
	if order_params["ground_type"] not in ground_type_data:
		raise ValueError("Invalid ground type: {}".format(
		    order_params["ground_type"]))
	if order_params["weather"] not in weather_data:
		raise ValueError("Invalid weather condition: {}".format(
		    order_params["weather"]))

	# Фильтр оборудования в зависимости от типа грунта и погодных условий
	available_equipment = []
	for equipment, data in equipment_data.items():
		restrictions = ground_type_data[order_params["ground_type"]]["restrictions"] + \
          weather_data[order_params["weather"]]["restrictions"]
		if not any(restriction in data["restrictions"]
		           for restriction in restrictions):
			available_equipment.append(data)

	# Вернуть доступные варианты оборудования
	return available_equipment


def get_estimated_cost(equipment, duration):
	return equipment["cost"] * duration


def main():
	# Получение параметров заказа из пользовательского ввода
	order_params = {
	    "work_type":
	        input("Напишите тип работы (Excavator, Bulldozer, Crane): "),
	    "ground_type":
	        input("Введите тип грунта (Soft, Hard, Rock): "),
	    "weather":
	        input("Напишите погодные условия (Sunny, Rain, Snow, Windy): "),
	    "duration":
	        float(input("Напишите продолжительность аренды (hours): "))
	}
