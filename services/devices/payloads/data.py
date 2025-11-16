from pydantic import BaseModel, Field
from typing import Optional


class DeviceInfo(BaseModel):
    year: Optional[int] = None
    price: Optional[float] = None
    cpu_model: Optional[str] = Field(
        default=None,
        alias='CPU model',  # для JSON сериализации/десериализации
        description='Модель процессора'
    )
    hard_disk_size: Optional[str] = Field(
        default=None,
        alias='Hard disk size',
        description='Размер жесткого диска'
    )

    class Config:
        # Позволяет использовать как оригинальные имена, так и алиасы
        validate_by_name = True


class DeviceTestData(BaseModel):
    name: Optional[str] = None
    data: Optional[DeviceInfo] = None
