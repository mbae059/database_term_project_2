import sys

import test1


class Test:
    def __init__(self):
        self.bar = 3
    # does something that has nothing to do with Test.bar
    def do_something(self):
        pass

    # def __init__(self, test_class: test1.test_interface=None):
    #     self.test_class = test_class
    # def set_test_class(self, test_interface_implementation):
    #     self.test_class = test_interface_implementation


test = Test()
test.set_test_class(test1.test_interface_implementation_1())
test.test_class.print_test()
