#!/usr/bin/env python3
from cli import welcome_user
from scripts.brain_even import even
from scripts.brain_calc import calc
from scripts.brain_gcd import gcd
from scripts.brain_progression import progression


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    # even()
    # calc()
    # gcd()
    progression()


if __name__ == '__main__':
    main()
