from abc import ABC, abstractmethod
from datetime import date


# Engine接口
class Engine(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


# Battery接口
class Battery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


# Serviceable接口
class Serviceable(ABC):
    def needs_service(self) -> bool:
        pass


# Car类
class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()


# Engine实现类
class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 30000


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 60000


class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool):
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on


# Battery实现类
class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        days_since_last_service = (self.current_date - self.last_service_date).days
        return days_since_last_service >= 730  # 2 years


class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        days_since_last_service = (self.current_date - self.last_service_date).days
        return days_since_last_service >= 1460  # 4 years


# CarFactory类
class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int,
                         last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int,
                      last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)


# 使用工厂创建不同类型的Car对象
current_date = date(2023, 8, 29)
last_service_date = date(2023, 2, 15)
current_mileage = 80000  # Assuming mileage for the examples
last_service_mileage = 60000

car1 = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
car2 = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
car3 = CarFactory.create_palindrome(current_date, last_service_date, True)
car4 = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
car5 = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)

# 检查是否需要服务
print(car1.needs_service())
print(car2.needs_service())
print(car3.needs_service())
print(car4.needs_service())
print(car5.needs_service())
