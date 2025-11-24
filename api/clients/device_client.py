from api.clients.base_clients import ApiClient
import allure
from utils.helpers.logging_decorators import logging_api_call


class DeviceApiClient(ApiClient):
    endpoint = 'objects'

    @allure.step('Getting all devices')
    @logging_api_call
    def get_all_devices_api(self):
        return self.client.get(f"{self.url}/{self.endpoint}")

    @allure.step('Getting devices by ids')
    @logging_api_call
    def get_devices_by_ids_api(self, *device_ids):
        params = [("id", device_id) for device_id in device_ids]
        return self.client.get(f"{self.url}/{self.endpoint}", params=params)

    @allure.step('Getting device by id')
    def get_device_by_id_api(self, device_id):
        return self.client.get(f"{self.url}/{self.endpoint}/{device_id}")

    @allure.step('Creating device')
    def create_devices_api(self, payload):
        return self.client.post(f"{self.url}/{self.endpoint}", json=payload)

    @allure.step('Updating full device')
    def update_full_device_api(self, payload, device_id):
        return self.client.put(f"{self.url}/{self.endpoint}/{device_id}", json=payload)

    @allure.step('Updating device partial')
    def update_partial_device_api(self, payload, device_id):
        return self.client.patch(f"{self.url}/{self.endpoint}/{device_id}", json=payload)

    @allure.step('Delete device')
    def delete_device_api(self, device_id):
        return self.client.delete(f"{self.url}/{self.endpoint}/{device_id}")
