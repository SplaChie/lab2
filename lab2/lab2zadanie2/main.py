from devices.device_factory import IProneFactory, XiaomiFactory, GalaxyFactory

def main():
    # Створення девайсів через IProneFactory
    iprone_factory = IProneFactory()
    laptop1 = iprone_factory.create_laptop()
    smartphone1 = iprone_factory.create_smartphone()
    ebook1 = iprone_factory.create_ebook()

    print(laptop1)
    print(smartphone1)
    print(ebook1)

    # Створення девайсів через XiaomiFactory
    xiaomi_factory = XiaomiFactory()
    laptop2 = xiaomi_factory.create_laptop()
    smartphone2 = xiaomi_factory.create_smartphone()
    ebook2 = xiaomi_factory.create_ebook()

    print(laptop2)
    print(smartphone2)
    print(ebook2)

    # Створення девайсів через GalaxyFactory
    galaxy_factory = GalaxyFactory()
    laptop3 = galaxy_factory.create_laptop()
    smartphone3 = galaxy_factory.create_smartphone()
    ebook3 = galaxy_factory.create_ebook()

    print(laptop3)
    print(smartphone3)
    print(ebook3)

if __name__ == "__main__":
    main()
