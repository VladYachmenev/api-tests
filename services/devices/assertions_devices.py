from services.devices.models.device_model import DeviceBase, DeviceAddResponse, DeviceUpdateResponse


def assert_devices(payload: DeviceBase, response_model: DeviceAddResponse | DeviceUpdateResponse):
    if isinstance(response_model, DeviceAddResponse):
        assert response_model.name == payload.name
        assert response_model.data == payload.data
        assert response_model.id is not None
        assert response_model.created_at is not None
