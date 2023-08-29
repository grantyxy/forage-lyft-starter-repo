from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Battery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass
