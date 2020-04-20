#   Simple timer for use in Python
#
#   Erik Boman eribo549@student.liu.se

import time
import threading
import multiprocessing
import inspect
CRED = '\033[91m'
CEND = '\033[0m'

class Timer:

    #   Instantiate by assigning class call to variable
    #   Example: x = Time()
    #   then proceed to call Timer-methods by x.classMethod(args, kwargs)

    def __init__(self, name):
        self.__name = name
        self.__initTime = time.time()
        self.__bool = True
        self.__boolTimerFlag = True
        self.__TimerFlag = True


    def getTimer(self):
        return round(time.time() - self.__initTime, 1)

    def resetTimer(self):
        self.__initTime = time.time()

    def setResetTimer(self, endTime: float):
        if not self.__TimerFlag:
            return
        try:
            if threading.active_count() == multiprocessing.cpu_count():
                raise RuntimeError(f"{CRED}setResetTimer: Not enough threads available{CEND}"
                                   f"\n---> {CRED}Process will continue{CEND}")
            if not isinstance(endTime, int):
                raise TypeError(f'{CRED}setResetTimer: Input \'endTime\' must be integer or float{CEND}'
                                f"\n---> {CRED}Process will continue{CEND}")
            t = threading.Timer(endTime, self.resetTimer)
            return t
        except Exception as e:
            self.__TimerFlag = False
            print("Failed to start boolean timer because of error:\n------>", e)

    def getBool(self):
        return self.__bool

    def setBool(self, setTo: bool):
        #print(inspect.stack())
        self.__bool = setTo

    def returnBool(self, arg):
        self.__bool = arg

    def setBoolTimer(self, endTime=10, arg=bool, name=str):

        if not self.__boolTimerFlag:
            return
        try:
            if threading.active_count() == multiprocessing.cpu_count():
                raise RuntimeError(f"{CRED}setBoolTimer: Not enough threads available{CEND}"
                                   f"\n---> {CRED}Process will continue{CEND}")
            if not isinstance(arg, bool):
                raise TypeError(f"{CRED}setBoolTimer: Input \'arg\' must be a boolean-type{CEND}"
                                f"\n---> {CRED}Process will continue{CEND}")
            if not isinstance(endTime, float):
                raise TypeError(f'{CRED}setBoolTimer: Input \'endTime\' must be integer or float{CEND}'
                                f'\n---> {CRED}Process will continue{CEND}')
            t = threading.Timer(endTime, self.setBool, [arg])
            t.setDaemon(True)
            t.name = name
            #t.start()
            return t
        except Exception as e:
            raise e

            self.__boolTimerFlag = False
            print("Failed to start boolean timer because of error:\n--->", e)



