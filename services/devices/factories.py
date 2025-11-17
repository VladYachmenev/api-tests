from faker import Faker
import random
from services.devices.models.device_model import DeviceBase, DeviceInfo
faker_ru = Faker('ru_RU')


def generate_device_data():
    device_info = DeviceInfo(
        year=int(faker_ru.year()),
        price=random.uniform(1.0, 100.0),
        cpu_model=faker_ru.text(),
        hard_disk_size=faker_ru.text())

    return DeviceBase(name=faker_ru.word(), data=device_info)