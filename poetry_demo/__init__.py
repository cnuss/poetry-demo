__version__ = '0.0.1'

from mylib import getip, whoami


def whoismylib():
    return whoami()


def main():
    print(f"Your IP is: {getip()}")
