import logging

disable_loggers = ['flake8', 'pytest-flake8']


def pytest_configure():
    """Configure logging."""
    for logger_name in disable_loggers:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.ERROR)