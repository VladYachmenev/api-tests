from api.models.device_model import DeviceBase, DeviceDate, DevicePartialUpdate, DeviceAddResponse, DeviceUpdateResponse
from datetime import datetime
from deepdiff import DeepDiff


def assert_devices_core_fields(payload: DeviceBase, response_model: DeviceAddResponse | DeviceUpdateResponse):
    assert response_model.name == payload.name
    assert response_model.data == payload.data
    assert response_model.id is not None
    if hasattr(response_model, 'created_at'):
        assert response_model.created_at is not None
        _assert_valid_timestamp(response_model.created_at)
    if hasattr(response_model, 'updated_at'):
        assert response_model.updated_at is not None
        _assert_valid_timestamp(response_model.updated_at)


def assert_partial_device_update(payload: DevicePartialUpdate, response_model: DeviceUpdateResponse):
    for field_name in payload.model_fields_set:
        expected_value = getattr(payload, field_name)
        actual_value = getattr(response_model, field_name)

        if isinstance(expected_value, DeviceDate):
            for nested_field in expected_value.model_fields_set:
                expected_nested = getattr(expected_value, nested_field)
                actual_nested = getattr(actual_value, nested_field)
                assert actual_nested == expected_nested
        else:
            assert actual_value == expected_value


def assert_delete_device(response_model, device_id):
    assert response_model.message == f"Object with id = {device_id}, has been deleted."


def _assert_valid_timestamp(timestamp: datetime):
    assert timestamp.tzinfo is not None
    assert timestamp <= datetime.now(timestamp.tzinfo)
