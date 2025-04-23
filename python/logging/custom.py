import logging

def logger(filename: str):
    logger = logging.getLogger(filename)
    # print(logger.__str__())
    console_handler = logging.StreamHandler()
    print(console_handler)
    file_handler = logging.FileHandler(f'{filename}.log', mode="a", encoding="utf-8")
    print(file_handler)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    print(logger.handlers)
    formatter = logging.Formatter(
    "{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",
    )
    console_handler.setFormatter(formatter)
    logger.warning("Look at my logger!")
