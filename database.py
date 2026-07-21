"""Database initialization and connection management."""

import sqlite3
import logging
from pathlib import Path
from contextlib import asynccontextmanager

from config import settings

logger = logging.getLogger(__name__)

# Database path
DB_PATH = Path(settings.DATABASE_PATH)


def get_connection() -> sqlite3.Connection:
    """Get a database connection."""
    # Create data directory if it doesn't exist
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


async def init_db() -> None:
    """Initialize the database with required tables."""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # TODO: Add more tables as needed
        
        conn.commit()
        logger.info('Database tables created successfully')
    except sqlite3.Error as e:
        logger.error(f'Database initialization error: {e}')
        conn.rollback()
        raise
    finally:
        conn.close()


@asynccontextmanager
async def get_db():
    """Async context manager for database connections."""
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()
