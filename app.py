from flask import Flask
from cement.logger import logging
from cement.exception import CementException
import sys, os

def main():
    try:
        logging.info("yhhhh")
        # raise Exception("we are tseting")
        raise CementException(e, sys) from e
    except Exception as e:
        cement = CementException(e, sys)
        logging.info(cement.error_message)
    return "ggggga"





# app = Flask(__name__)


# @app.route('/', methods=['POST', 'GET'])
# def welcome():
#     return "hello"

# if __name__=="__main__":
#     app.run()