from faker import Faker
import random
from api.models.device_model import DeviceBase, DeviceData, DevicePartialUpdate

faker_ru = Faker('ru_RU')


def generate_full_payload():
    device_info = DeviceData(
        year=int(faker_ru.year()),
        price=random.uniform(1.0, 100.0),
        cpu_model=faker_ru.text(),
        hard_disk_size=faker_ru.text())

    return DeviceBase(name=faker_ru.word(), data=device_info)


def generate_partial_update_payload(field):
    data_fields = ['year', 'price', 'cpu_model', 'hard_disk_size']
    default_fields = ['name']
    if field in data_fields:
        device_info_data = {}
        if field == 'year':
            device_info_data[field] = int(faker_ru.year())
        elif field == 'price':
            device_info_data[field] = random.uniform(1.0, 100.0)
        elif field == 'cpu_model':
            device_info_data[field] = faker_ru.text()
        elif field == 'hard_disk_size':
            device_info_data[field] = faker_ru.text()
        device_info = DeviceData(**device_info_data)
        return DevicePartialUpdate(data=device_info)
    if field in default_fields:
        if field == 'name':
            return DevicePartialUpdate(name=faker_ru.text())