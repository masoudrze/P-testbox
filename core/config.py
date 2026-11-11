import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    base_url: str
    default_timeout: int


settings = Settings(
    base_url=os.getenv("BASE_URL", ""),
    default_timeout=int(os.getenv("DEFAULT_TIMEOUT", "10000")),
)