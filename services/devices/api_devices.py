from shared.clients import ApiClient
from settings import settings


class DevicesApi(ApiClient):
    endpoint = 'objects'

    def get_all_devices_api(self):
        return self.client.get(f"{self.url}/{self.endpoint}")

    def get_devices_by_ids_api(self, *device_ids):
        params = [("id", device_id) for device_id in device_ids]
        return self.client.get(f"{self.url}/{self.endpoint}", params=params)

    def create_devices_api(self, payload):
        return self.client.post(f"{self.url}/{self.endpoint}", json=payload)
