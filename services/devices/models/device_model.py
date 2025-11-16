from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class DeviceResponseInfo(BaseModel):
    year: Optional[int] = None
    price: Optional[float] = None
    cpu_model: Optional[str] = Field(
        default=None,
        alias='CPU model',
        description='Модель процессора'
    )
    hard_disk_size: Optional[str] = Field(
        default=None,
        alias='Hard disk size',
        description='Размер жесткого диска'
    )


class DeviceResponseModel(BaseModel):
    id: str
    name: str
    data: DeviceResponseInfo
    created_at: datetime = Field(alias='createdAt')



