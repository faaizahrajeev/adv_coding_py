# well to start off, lets do exception handling
class MyException(Exception):
    pass
def test_exception():
    try:
        raise MyException("An exception")
    except MyException as e:
        print("MyException caught")
        raise
    except Exception as e:
        print("Exception caught")
    finally:
        print("Finally block")
test_exception()
# MyException caught
# Finally block
# Traceback (most recent call last):
#   File "logging.py", line 126, in <module>
#     test_exception()
#   File "logging.py", line 123, in test_exception
#     raise MyException("An exception")
# __main__.MyException: An exception



import logging
import logging.config
logging.basicConfig(filename="example.log", level=logging.INFO)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
# This is an info message
# This is a warning message
# This is an error message
# This is a critical message
# example.log:
# INFO:root:This is an info message
# WARNING:root:This is a warning message
# ERROR:root:This is an error message
# CRITICAL:root:This is a critical message

# logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S", level=logging.DEBUG, filename="example.log", filemode="a") to append to the file

logger = logging.getLogger(__name__)
logger.info("Hello from logging")
# INFO:__main
# :Hello from
# logging

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)
logger.info("Hello from logging")
# INFO:__main__:Hello from logging
# logging.conf
# [loggers]

# keys=root, exampleLogger

try:
    a = 1/0
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
# ERROR:root:Exception occurred
# Traceback (most recent call last):
#   File "logging.py", line 158, in <module>
#     a = 1/0
# ZeroDivision
# Error: division by zero

from logging.handlers import RotatingFileHandler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=5)
logger.addHandler(handler)
for _ in range(10000):
    logger.info("Hello, logging")

from logging.handlers import TimedRotatingFileHandler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler("timed_app.log", when="s", interval=5, backupCount=5)
logger.addHandler(handler)
for _ in range(10000):
    logger.info("Hello, logging")

import logging
import logging.config
import yaml
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logger = logging.getLogger(__name__)
logger.info("Hello from logging")
