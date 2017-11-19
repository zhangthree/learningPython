#!/usr/bin/python

import logging


class safeLog:
    def __init__(self):
        self.__logdir = 'py.log'
        self.__logger = logging.getLogger("mylog")
        self.__handler = logging.FileHandler(self.__logdir)
        self.__formatter = logging.Formatter('%(asctime)s - %(levelno)s - %(pathname)s - %(lineno)d - %(message)s')
        self.__handler.setFormatter(self.__formatter)
        self.__logger.addHandler(self.__handler)
        self.__logger.setLevel(logging.INFO)

    def logInfo(self,msg):
        self.__logger.info(msg)

    def logWarning(self,msg):
        self.__logger.warning(msg)

    def logError(self,msg):
        self.__logger.error(msg)

    


    