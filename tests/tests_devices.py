from shared.utils.base_assertions import validate_schema, validate_scheme_for_array, assert_status_code
from services.devices.models.device_model import DeviceAddResponse, DeviceGet
from services.devices.factories import generate_device_data
from services.devices.assertions_devices import assert_devices


class TestsDevices:
    """Tests for Devices API endpoints"""
    def test_get_device(self, function_devices_api):
        response = function_devices_api.get_all_devices_api()
        assert_status_code(response, 200)
        validate_scheme_for_array(response.json(), DeviceGet)

    def test_get_devices(self, function_devices_api):
        response = function_devices_api.get_devices_by_ids_api(1, 2, 3)

    def test_create_device(self, function_devices_api):
        payload = generate_device_data()
        response = function_devices_api.create_devices_api(payload.model_dump(by_alias=True))
        assert_status_code(response, 200)
        response_model = validate_schema(response.json(), DeviceAddResponse)
        assert_devices(payload=payload, response_model=response_model)
