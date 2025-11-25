from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class DeviceData(BaseModel):
    year: Optional[int] = None
    price: Optional[float] = None
    cpu_model: Optional[str] = Field(
        default=None,
        alias='CPU model'
    )
    hard_disk_size: Optional[str] = Field(
        default=None,
        alias='Hard disk size'
    )
    model_config = ConfigDict(extra='allow', populate_by_name=True)

    @classmethod
    def create_list_of_fields(cls):
        return list(cls.model_fields.keys())


class DeviceBase(BaseModel):
    name: str
    data: Optional[DeviceData] = None


class DeviceGetResponse(DeviceBase):
    id: str

    def __repr__(self):
        return f"DeviceGetResponse"


class DeviceAddResponse(DeviceBase):
    id: str
    created_at: datetime = Field(alias='createdAt')

    def __repr__(self):
        return f"DeviceAddResponse"


class DeviceUpdateResponse(DeviceBase):
    id: str
    updated_at: datetime = Field(alias='updatedAt')

    def __repr__(self):
        return f"DeviceUpdateResponse"


class DevicePartialUpdate(DeviceBase):
    name: Optional[str] = None
    data: Optional[DeviceData] = None

    def __repr__(self):
        return f"DevicePartialUpdate"


class DeviceDeleteResponse(BaseModel):
    message: str

    def __repr__(self):
        return f"DeviceDeleteResponse"
