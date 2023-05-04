import logging

logger = logging.getLogger(__name__)

# handler = logging.FileHandler("test.log")
formatter = logging.Formatter("%(name)s - %(message)s")
logger.setLevel(logging.INFO)
# handler.setFormatter(formatter)

# logger.addHandler(handler)
logger.info("test the custom logger")