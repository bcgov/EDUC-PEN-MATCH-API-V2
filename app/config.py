import os


class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "EDUC-PEN-MATCH-API-V2")


settings = Settings()