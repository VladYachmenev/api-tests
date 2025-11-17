from services.devices.models.device_model import DeviceBase, DeviceAddResponse, DeviceUpdateResponse
from datetime import datetime


def assert_devices_core_fields(payload: DeviceBase, response_model: DeviceAddResponse | DeviceUpdateResponse):
    if isinstance(payload, DeviceBase):
        assert response_model.name == payload.name
        assert response_model.data == payload.data
        assert response_model.id is not None
        if isinstance(response_model, DeviceAddResponse):
            assert response_model.created_at is not None
            _assert_valid_timestamp(response_model.created_at)
        if isinstance(response_model, DeviceUpdateResponse):
            assert response_model.updated_at is not None
            _assert_valid_timestamp(response_model.updated_at)


def _assert_valid_timestamp(timestamp: datetime):
    """Проверяет валидность временной метки"""
    assert timestamp.tzinfo is not None
    assert timestamp <= datetime.now(timestamp.tzinfo)


def assert_partial_device_update(payload, response_model):
   pass