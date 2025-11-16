import pytest
from services.devices.payloads.factories import generate_device_data

class TestsDevices:

    def test_get_devices(self, function_devices_api):
        response = function_devices_api.get_all_devices_api()
        assert response.status_code == 200

    def test_create_devices(self, function_devices_api):
        payload = generate_device_data().model_dump(by_alias=True)
        response = function_devices_api.create_devices_api(payload)
        print(response.json())

