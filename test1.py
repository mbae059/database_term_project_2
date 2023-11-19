from abc import *


class test_interface(metaclass=ABCMeta):
    def __init__(self):
        self.string = "123"

    @abstractmethod
    def print_test(self):
        print("123")


class test_interface_implementation_1(test_interface):
    def print_test(self):
        print("456")
