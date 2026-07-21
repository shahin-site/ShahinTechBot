# ShahinTechBot

A professional Telegram bot built with Python 3.12 and aiogram 3, following clean architecture principles.

## Features

- Clean architecture with organized folder structure
- Environment-based configuration
- SQLite database integration
- Comprehensive logging
- Type hints throughout the codebase
- Ready to extend with business logic

## Project Structure

```
ShahinTechBot/
├── handlers/          # Message and event handlers
├── keyboards/        # Inline and reply keyboards
├── database/         # Database models and queries
├── models/           # Pydantic models and data structures
├── services/         # Business logic services
├── utils/            # Utility functions and helpers
├── main.py           # Application entry point
├── config.py         # Configuration management
├── database.py       # Database initialization
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variables template
└── README.md         # This file
```

## Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd ShahinTechBot
```

2. Create and activate a virtual environment:

```bash
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create `.env` file from template:

```bash
cp .env.example .env
```

5. Configure environment variables in `.env`:

```
BOT_TOKEN=your_telegram_bot_token
ADMIN_ID=your_telegram_user_id
DATABASE_PATH=data/bot.db
LOG_LEVEL=INFO
DEBUG=False
```

## Running the Bot

Start the bot with:

```bash
python main.py
```

You should see output similar to:

```
2024-01-15 10:30:45,123 - root - INFO - Starting ShahinTechBot...
2024-01-15 10:30:45,456 - root - INFO - Database initialized
2024-01-15 10:30:45,789 - root - INFO - Bot handlers registered
2024-01-15 10:30:46,012 - root - INFO - Bot started polling (Debug: False)
```

## Configuration

All configuration is managed through environment variables in the `.env` file:

- `BOT_TOKEN`: Your Telegram bot token (required)
- `ADMIN_ID`: Administrator user ID for special commands (required)
- `DATABASE_PATH`: Path to SQLite database (default: `data/bot.db`)
- `LOG_LEVEL`: Logging level - DEBUG, INFO, WARNING, ERROR, CRITICAL (default: `INFO`)
- `DEBUG`: Enable debug mode (default: `False`)

## Logging

Logs are written to both console and `logs/bot.log` file. Configure the log level in `.env` using the `LOG_LEVEL` variable.

## Development

### Adding Handlers

Create handler modules in the `handlers/` folder and register them in `main.py`:

```python
from handlers import your_handler_router

dp.include_router(your_handler_router.router)
```

### Adding Database Models

Define models in `models/` folder and create corresponding database tables in `database.py`:

```python
# In models/user.py
from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    username: str
    ...
```

### Using Services

Create business logic in `services/` folder:

```python
# In services/user_service.py
class UserService:
    async def get_user(self, user_id: int):
        ...
```

## Contributing

Please follow these guidelines:

1. Maintain clean architecture principles
2. Add type hints to all functions
3. Write comprehensive logging statements
4. Update requirements.txt for new dependencies
5. Follow PEP 8 style guide

## License

MIT License

## Support

For issues and questions, please create an issue in the repository.
