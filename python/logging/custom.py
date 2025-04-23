import logging
logger = logging.getLogger(__name__)
# print(logger.__str__())
console_handler = logging.StreamHandler()
print(console_handler)
file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
print(file_handler)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.warning("Look at my logger!")
print(logger.handlers)
