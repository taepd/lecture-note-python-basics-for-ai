import logging


if __name__ == "__main__":
    logger = logging.getLogger("main")
    logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.INFO)

    steam_handler = logging.FileHandler("my.log", mode="w", encoding="utf8")
    logger.addHandler(steam_handler)

    logger.debug("틀렸어!!")
    logger.info("확인행!!")
    logger.warning("조심해!!")
    logger.error("에러났어!!")
    logger.critical("망했다!!")
