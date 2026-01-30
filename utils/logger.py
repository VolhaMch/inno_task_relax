import logging
import os
from datetime import datetime

def get_logger(name: str = "automation"):
    # Создаём папку logs, если её нет
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Имя файла с датой
    log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")

    # Настройка логгера
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Чтобы не дублировать хендлеры при повторном вызове
    if not logger.handlers:

        # Логи в файл
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(logging.INFO)
        file_format = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        file_handler.setFormatter(file_format)

        # Логи в консоль
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter(
            "%(levelname)s | %(message)s"
        )
        console_handler.setFormatter(console_format)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
