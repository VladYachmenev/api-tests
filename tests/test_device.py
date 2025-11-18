import pytest

from api.models.device_model import (
    DeviceAddResponse,
    DeviceGetResponse,
    DeviceUpdateResponse,
    DeviceDeleteResponse
)

from utils.assertions.base_assertions import (
    assert_status_code,
    validate_schema,
    validate_scheme_for_array
)
from utils.assertions.device_assertions import assert_devices_core_fields, assert_partial_device_update, assert_delete_device

from utils.factories.device_factory import (
    generate_full_payload,
    generate_partial_update_payload
)


class TestsDevicesApi:
    """Tests for Devices API endpoints"""

    def test_get_devices(self, function_devices_api):
        response = function_devices_api.get_all_devices_api()
        assert_status_code(response, 200)
        validate_scheme_for_array(response, DeviceGetResponse)

    def test_get_devices_by_id(self, function_devices_api):
        response = function_devices_api.get_devices_by_ids_api(1, 2, 3)
        assert_status_code(response, 200)
        validate_scheme_for_array(response, DeviceGetResponse)

    def test_get_device_by_id(self, function_devices_api):
        response = function_devices_api.get_device_by_id_api(7)
        assert_status_code(response, 200)
        validate_schema(response, DeviceGetResponse)

    def test_create_device(self, function_devices_api):
        payload = generate_full_payload()
        response = function_devices_api.create_devices_api(payload.model_dump(by_alias=True))
        assert_status_code(response, 200)
        response_model = validate_schema(response, DeviceAddResponse)
        assert_devices_core_fields(payload=payload, response_model=response_model)

    def test_full_update_device(self, function_devices_api, function_create_device_api):
        response_id = function_create_device_api
        payload = generate_full_payload()
        response = function_devices_api.update_full_device_api(payload.model_dump(by_alias=True), response_id)
        assert_status_code(response, 200)
        response_model = validate_schema(response, DeviceUpdateResponse)
        assert_devices_core_fields(payload=payload, response_model=response_model)

    @pytest.mark.parametrize('field', ['name', 'year', 'price', 'cpu_model', 'hard_disk_size'])
    def test_partial_update_device(self, function_devices_api, function_create_device_api, field):
        device_id = function_create_device_api
        payload = generate_partial_update_payload(field)
        response = function_devices_api.update_partial_device_api(payload.model_dump(by_alias=True, exclude_none=True),
                                                                  device_id)
        assert_status_code(response, 200)
        response_model = validate_schema(response, DeviceUpdateResponse)
        assert_partial_device_update(payload=payload, response_model=response_model)

    def test_delete_device(self, function_devices_api, function_create_device_api):
        device_id = function_create_device_api
        response = function_devices_api.delete_device_api(device_id)
        assert_status_code(response, 200)
        response_model = validate_schema(response, DeviceDeleteResponse)
        assert_delete_device(response_model=response_model,device_id=device_id)