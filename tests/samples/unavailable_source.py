string = """
from snoop import Config

def foo():
    return 3

for color in [False, True]:
    Config(color=color).snoop(foo)()
"""


def main():
    exec(string, {})


expected_output = """
12:34:56.78 >>> Call to foo in File "/path/to_file.py", line 4
12:34:56.78    4 | SOURCE IS UNAVAILABLE
12:34:56.78    5 | SOURCE IS UNAVAILABLE
12:34:56.78 <<< Return value from foo: 3
[90m12:34:56.78 [0m[36m[1m>>> Call to foo in File "/path/to_file.py", line 4[0m
[90m12:34:56.78 [0m[90m   4[0m | SOURCE IS UNAVAILABLE
[90m12:34:56.78 [0m[90m   5[0m | SOURCE IS UNAVAILABLE
[90m12:34:56.78 [0m[32m[1m<<< Return value from foo: [0m[38;5;141m3[39m
"""
