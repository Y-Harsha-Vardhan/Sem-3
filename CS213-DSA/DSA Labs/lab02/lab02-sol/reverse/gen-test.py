#!/usr/bin/env python3
# coding: utf-8


import random
import os


for t in range(6,10):
    os.system(f'mkdir -p ./tests/test{t}')
    test_input = f'./tests/test{t}/input.txt'
    print(f'Dumping {test_input}')
    with open(test_input, 'w') as input_file:
        vmax = 10000
        n   = random.randint(10, vmax)
        input_file.write(f"{n}\n")
        for i in range(n):
            input_file.write(f"{random.randint(0,vmax)}\n")
