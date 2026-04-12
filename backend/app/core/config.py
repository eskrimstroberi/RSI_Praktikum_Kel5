from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Use Field(default=...) to satisfy Error diagnostics
    POSTGRES_USER: str = Field(default="postgres")
    POSTGRES_PASSWORD: str = Field(default="DefaultPassword123!")
    POSTGRES_SERVER: str = Field(default="postgres")
    POSTGRES_DB: str = Field(default="postgres")
    POSTGRES_PORT: int = Field(default=5432)

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    JWT_SECRET_KEY: str = Field(default="None")
    JWT_ALGORITHM: str = Field(default="None")

    model_config = SettingsConfigDict(env_file_encoding="utf-8", extra="ignore")


settings = Settings()
