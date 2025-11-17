import pytest

from shared.utils.base_assertions import validate_schema, validate_scheme_for_array, assert_status_code
from services.devices.models.device_model import DeviceAddResponse, DeviceGet, DeviceUpdateResponse, make_list_for_parametrise
from services.devices.factories import generate_device_data, generate_device_data_for_partial_update
from services.devices.assertions_devices import assert_devices_core_fields


class TestsDevicesApi:
    """Tests for Devices API endpoints"""
    def test_get_devices(self, function_devices_api):
        response = function_devices_api.get_all_devices_api()
        assert_status_code(response, 200)
        validate_scheme_for_array(response.json(), DeviceGet)

    def test_get_devices_by_id(self, function_devices_api):
        response = function_devices_api.get_devices_by_ids_api(1, 2, 3)
        assert_status_code(response, 200)
        validate_scheme_for_array(response.json(), DeviceGet)

    def test_get_device_by_id(self, function_devices_api):
        response = function_devices_api.get_device_by_id_api(7)
        assert_status_code(response, 200)
        validate_schema(response.json(), DeviceGet)

    def test_create_device(self, function_devices_api):
        payload = generate_device_data()
        response = function_devices_api.create_devices_api(payload.model_dump(by_alias=True))
        assert_status_code(response, 200)
        response_model = validate_schema(response.json(), DeviceAddResponse)
        assert_devices_core_fields(payload=payload, response_model=response_model)

    def test_full_update_device(self, function_devices_api, function_create_device_api):
        response_id = function_create_device_api
        payload = generate_device_data()
        response = function_devices_api.update_full_device_api(payload.model_dump(by_alias=True), response_id)
        assert_status_code(response, 200)
        response_model = validate_schema(response.json(), DeviceUpdateResponse)
        assert_devices_core_fields(payload=payload, response_model=response_model)

    @pytest.mark.parametrize('field', make_list_for_parametrise())
    def test_partial_update_device(self, function_devices_api, function_create_device_api, field):
        response_id = function_create_device_api
        payload = generate_device_data_for_partial_update(field)
        response = function_devices_api.update_partial_device_api(payload.model_dump(by_alias=True, exclude_none=True), response_id)
        assert_status_code(response, 200)

