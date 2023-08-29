from datetime import date

from car import CarFactory

if __name__ == "__main__":
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
