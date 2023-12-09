def bar():
    print('bar')


class Foo:
    li = ['bar', 'bar1', 'bar2']

    def __init__(self):
        self.li[0]()
temp = Foo()
