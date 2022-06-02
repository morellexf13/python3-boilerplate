"""
Module Docstring
"""

__author__ = "morellexf26"
__version__ = "0.1.0"
__license__ = "MIT"

from logzero import logger


def main():
    """ Main entry point of the app """
    logger.info("hello world")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
