import datetime

class Car:
    def __init__(self, license_plate, charge_type, charge_amount):
        self.license_plate = license_plate
        self.charge_type = charge_type
        self.charge_amount = charge_amount

class ChargingStation:
    def __init__(self):
        self.waiting_area = []
        self.charging_area = {
            "fast": [],
            "slow": []
        }

    def add_car(self, car: Car):
        if car.charge_type == "fast":
            self.waiting_area.insert(0, car)
        else:
            self.waiting_area.append(car)

    def allocate_car(self):
        for car in self.waiting_area:
            if car.charge_type == "fast" and len(self.charging_area["fast"]) < 2:
                self.charging_area["fast"].append(car)
                self.waiting_area.remove(car)
            elif car.charge_type == "slow" and len(self.charging_area["slow"]) < 3:
                self.charging_area["slow"].append(car)
                self.waiting_area.remove(car)

class Pricing:
    @staticmethod
    def calculate_cost(charge_amount, charge_time):
        current_hour = datetime.datetime.now().hour
        if 10 <= current_hour < 15 or 18 <= current_hour < 21:
            price = 1.0
        elif 7 <= current_hour < 10 or 15 <= current_hour < 18 or 21 <= current_hour < 23:
            price = 0.7
        else:
            price = 0.4
        charge_fee = charge_amount * price
        service_fee = charge_amount * 0.8
        total_fee = charge_fee + service_fee
        return total_fee
