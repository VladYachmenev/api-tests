import pytest


class TestsDevices:

    def test_get_devices(self, function_devices_api):
        response = function_devices_api.get_all_devices_api()
        assert response.status_code == 200
        print(response.json())
        a = response.json()
        c = []
        for i in a:
            for b in i.keys():
                if b == 'name':
                    c.append(i[b])
        print(c)

