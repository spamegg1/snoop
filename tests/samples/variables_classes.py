from collections import OrderedDict

import snoop


class WithSlots(object):
    __slots__ = ('x', 'y')

    def __init__(self):
        self.x = 3
        self.y = 4


@snoop.snoop(watch=(
        snoop.Keys('_d', exclude='c'),
        snoop.Attrs('_s'),
        snoop.Indices('_lst')[-3:],
        snoop.Attrs('_lst'),  # doesn't have attributes
))
def main():
    _d = OrderedDict([('a', 1), ('b', 2), ('c', 'ignore')])
    _s = WithSlots()
    _lst = list(range(1000))


expected_output = """
12:34:56.78 >>> Call to main in File "/path/to_file.py", line 20
12:34:56.78   20 | def main():
12:34:56.78   21 |     _d = OrderedDict([('a', 1), ('b', 2), ('c', 'ignore')])
12:34:56.78 .......... len(_d) = 3
12:34:56.78 .......... _d['a'] = 1
12:34:56.78 .......... _d['b'] = 2
12:34:56.78   22 |     _s = WithSlots()
12:34:56.78 .......... _s = <tests.samples.variables_classes.WithSlots object at 0xABC>
12:34:56.78 .......... _s.x = 3
12:34:56.78 .......... _s.y = 4
12:34:56.78   23 |     _lst = list(range(1000))
12:34:56.78 .......... _lst = [0, 1, 2, ..., 997, 998, 999]
12:34:56.78 .......... len(_lst) = 1000
12:34:56.78 .......... _lst[997] = 997
12:34:56.78 .......... _lst[998] = 998
12:34:56.78 .......... _lst[999] = 999
12:34:56.78 <<< Return value from main: None
"""
