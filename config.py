"""Configuration for ShahinTechBot using environment variables."""

from pydantic_settings import BaseSettings
from pydantic import Field
import logging


class Settings(BaseSettings):
    """Application settings."""
    
    # Bot settings
    BOT_TOKEN: str = Field(..., description='Telegram bot token')
    ADMIN_ID: int = Field(..., description='Administrator Telegram user ID')
    
    # Database settings
    DATABASE_PATH: str = Field(default='data/bot.db', description='SQLite database path')
    
    # Logging settings
    LOG_LEVEL: str = Field(default='INFO', description='Logging level')
    
    # Application settings
    DEBUG: bool = Field(default=False, description='Debug mode')
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True


# Load settings from environment
settings = Settings()  # type: ignore


# Verify critical settings
if not settings.BOT_TOKEN:
    raise ValueError('BOT_TOKEN environment variable is required')

if not settings.ADMIN_ID:
    raise ValueError('ADMIN_ID environment variable is required')

logger = logging.getLogger(__name__)
logger.info(f'Settings loaded: DEBUG={settings.DEBUG}, LOG_LEVEL={settings.LOG_LEVEL}')
