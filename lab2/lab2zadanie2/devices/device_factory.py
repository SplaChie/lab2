from abc import ABC, abstractmethod
from devices.laptop import IProneLaptop, XiaomiLaptop, GalaxyLaptop
from devices.smartphone import IProneSmartphone, XiaomiSmartphone, GalaxySmartphone
from devices.ebook import IProneEBook, XiaomiEBook, GalaxyEBook

class DeviceFactory(ABC):
    @abstractmethod
    def create_laptop(self):
        pass

    @abstractmethod
    def create_smartphone(self):
        pass

    @abstractmethod
    def create_ebook(self):
        pass

class IProneFactory(DeviceFactory):
    def create_laptop(self):
        return IProneLaptop()

    def create_smartphone(self):
        return IProneSmartphone()

    def create_ebook(self):
        return IProneEBook()

class XiaomiFactory(DeviceFactory):
    def create_laptop(self):
        return XiaomiLaptop()

    def create_smartphone(self):
        return XiaomiSmartphone()

    def create_ebook(self):
        return XiaomiEBook()

class GalaxyFactory(DeviceFactory):
    def create_laptop(self):
        return GalaxyLaptop()

    def create_smartphone(self):
        return GalaxySmartphone()

    def create_ebook(self):
        return GalaxyEBook()
