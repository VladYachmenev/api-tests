from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    base_url: str = "https://api.restful-api.dev"

    @property
    def api_url(self) -> str:
        return self.base_url


settings = Settings()
