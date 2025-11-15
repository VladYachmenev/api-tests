from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DeviceInfo:
    year: Optional[int] = None
    price: Optional[float] = None
    cpu_model: Optional[str] = field(default=None, metadata={'json': 'CPU model'})
    hard_disk_size: Optional[str] = field(default=None, metadata={'json': 'Hard disk size'})


@dataclass
class DeviceTestData:
    name: Optional[str] = None
    data: Optional[DeviceInfo] = None
