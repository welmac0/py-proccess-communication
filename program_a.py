import subprocess
import random
import sys


def get_random():
    return random.random()


def get_message(msg):
    match msg:
        case "Hi":
            return "Hi"
        case "GetRandom":
            return get_random()
        case "Shutdown":
            exit(0)
        case _:
            return "Command ignored..."


'''
Program A: Pseudo-Random Number Generator
Program A will act as a pseudo-random number generator. D
It reads commands from stdin, where each command is delimited by a line break, D
and writes responses to stdout. The program should handle the following commands: D
Hi: Responds with "Hi" on stdout.
GetRandom: Responds with a pseudo-random integer on stdout.
Shutdown: Gracefully terminates the program.
Any unknown commands should be ignored.
'''

while True:
    msg = sys.stdin.readline().strip()
    print(get_message(msg), flush=True)
