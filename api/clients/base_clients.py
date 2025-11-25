import requests
from requests import Response
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Union
from settings import settings


class HttpClientInterface(ABC):
    @abstractmethod
    def get(self, url: str, **kwargs) -> Response:
        pass

    @abstractmethod
    def post(self, url: str, **kwargs) -> Response:
        pass

    @abstractmethod
    def put(self, url: str, **kwargs) -> Response:
        pass

    @abstractmethod
    def patch(self, url: str, **kwargs) -> Response:
        pass

    @abstractmethod
    def delete(self, url: str, **kwargs) -> Response:
        pass


class HttpClient(HttpClientInterface):
    def __init__(self):
        self.session = requests.session()

    def get(self, url, **kwargs):
        return self.session.get(url, **kwargs)

    def post(self, url, **kwargs):
        return self.session.post(url, **kwargs)

    def put(self, url, **kwargs):
        return self.session.put(url, **kwargs)

    def patch(self, url, **kwargs):
        return self.session.patch(url, **kwargs)

    def delete(self, url: str, **kwargs):
        return self.session.delete(url, **kwargs)


class ApiClient:
    def __init__(self, client: HttpClientInterface):
        self.url = settings.api_url
        self.client = client

