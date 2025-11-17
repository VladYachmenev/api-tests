from shared.clients import ApiClient
from settings import settings


class DevicesApi(ApiClient):
    endpoint = 'objects'

    def get_all_devices_api(self):
        return self.client.get(f"{self.url}/{self.endpoint}")

    def get_devices_by_ids_api(self, *device_ids):
        params = [("id", device_id) for device_id in device_ids]
        return self.client.get(f"{self.url}/{self.endpoint}", params=params)

    def get_device_by_id_api(self, device_id):
        return self.client.get(f"{self.url}/{self.endpoint}/{device_id}")

    def create_devices_api(self, payload):
        return self.client.post(f"{self.url}/{self.endpoint}", json=payload)

    def update_full_device_api(self, payload, device_id):
        return self.client.put(f"{self.url}/{self.endpoint}/{device_id}", json=payload)

    def update_partial_device_api(self, payload, device_id):
        return self.client.patch(f"{self.url}/{self.endpoint}/{device_id}", json=payload)

    def delete_device_api(self, device_id):
        return self.client.delete(f"{self.url}/{self.endpoint}/{device_id}")
