# Battery实现类
from datetime import date

from interfaces import Battery


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
