import datetime
import queue
class Car:
    def __init__(self, license_plate, charge_type, charge_amount):
        self.license_plate = license_plate
        self.charge_type = charge_type
        self.charge_amount = charge_amount

class ChargingStation:
    def __init__(self, id, power, capacity):
        self.id = id
        self.power = power
        self.capacity = capacity
        self.queue = queue.Queue(maxsize=capacity)
        self.total_charging_time = 0

    def is_full(self):
        return self.queue.full()

    def add_car(self, charging_volume):
        self.queue.put(charging_volume)
        self.total_charging_time += charging_volume / self.power

# 创建两个快充电桩和三个慢充电桩
# charging_stations = [
#     ChargingStation('A', 30, 2),
#     ChargingStation('B', 30, 2),
#     ChargingStation('C', 7, 2),
#     ChargingStation('D', 7, 2),
#     ChargingStation('E', 7, 2)
# ]



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
