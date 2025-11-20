from api.models.device_model import (
    DeviceBase,
    DeviceData,
    DevicePartialUpdate,
    DeviceAddResponse,
    DeviceUpdateResponse,
    DeviceDeleteResponse,
)


def assert_devices_core_fields(payload: DeviceBase, response_model: DeviceAddResponse | DeviceUpdateResponse):
    assert response_model.name == payload.name, f"Name mismatch: expected {payload.name}, got {response_model.name}"
    assert response_model.data == payload.data, f"Data mismatch: expected {payload.data}, got {response_model.data}"
    assert response_model.id is not None
    if hasattr(response_model, 'created_at'):
        assert response_model.created_at is not None, "created_at should not be None"
    if hasattr(response_model, 'updated_at'):
        assert response_model.updated_at is not None, "updated_at should not be None"


def assert_partial_device_update(payload: DevicePartialUpdate, response_model: DeviceUpdateResponse):
    for field_name in payload.model_fields_set:
        expected_value = getattr(payload, field_name)
        actual_value = getattr(response_model, field_name)

        if isinstance(expected_value, DeviceData):
            for nested_field in expected_value.model_fields_set:
                expected_nested = getattr(expected_value, nested_field)
                actual_nested = getattr(actual_value, nested_field)
                assert actual_nested == expected_nested, (
                    f"Nested field '{nested_field}' in '{field_name}' mismatch: "
                    f"expected '{expected_nested}', got '{actual_nested}'"
                )
        else:
            assert actual_value == expected_value, (
                f"Field '{field_name}' mismatch: expected '{expected_value}', got '{actual_value}'"
            )


def assert_delete_device(response_model: DeviceDeleteResponse, device_id: str):
    expected_message = f"Object with id = {device_id} has been deleted."
    assert response_model.message == expected_message, (
        f"Delete message mismatch. Expected: '{expected_message}', Got: '{response_model.message}'"
    )
