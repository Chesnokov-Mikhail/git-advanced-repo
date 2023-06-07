import logging

# Включаем логирование через logging
logger = logging.getLogger(__name__)
handler = logging.FileHandler(filename='./logs/games.log')
error_handler = logging.FileHandler(filename='./logs/errors.log')
handler.setLevel(logging.INFO)
error_handler.setLevel(logging.ERROR)
log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
error_log_format = logging.Formatter('%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s')
handler.setFormatter(log_format)
error_handler.setFormatter(error_log_format)
logger.addHandler(error_handler)
logger.addHandler(handler)
