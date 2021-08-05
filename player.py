#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
from termcolor import colored
from colorama import init

init()

os.system("clear")
print(colored('_________________________', 'blue', 'on_red'))
print(colored('|                       |', 'blue', 'on_red'))
print(colored('|      -------------    |', 'blue', 'on_red'))
print(colored('|     |            |    |', 'blue', 'on_red'))
print(colored('|     |            |    |', 'blue', 'on_red'))
print(colored('|     |            |    |', 'blue', 'on_red'))
print(colored('|     |            |    |', 'blue', 'on_red'))
print(colored('|   JJL            |    |', 'blue', 'on_red'))
print(colored('|  JJJJ           JJ    |', 'blue', 'on_red'))
print(colored('|  JJJJ          JJJ    |', 'blue', 'on_red'))
print(colored('|   JJ            JJ    |', 'blue', 'on_red'))
print(colored('-------------------------', 'blue', 'on_red'))
print('------------------------')
a = input('Your Music: ')
print('------------------------')
os.system('mpv ' + a + ' > /dev/null')
print('------------------------')
os.system('player.py')
