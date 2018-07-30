#!/usr/bin/python3

import random
import os
import sys

pwd = os.getcwd()

if len(sys.argv) != 3:
    print('<value> <filler_hmm_path> required!')
    exit(1)

try:
    hmm_path = sys.argv[1]
    inc_dec_value = float(sys.argv[2])
except ValueError:
    print('input is not valid!')
    exit(1)

with open(pwd + '/' + hmm_path, 'r') as f:
    hmm_lines = f.readlines()
    value_list = list(map(float, hmm_lines[8].split(' ')[1:])) # mean vector
    inc_value_list = [i+inc_dec_value for i in value_list]
    dec_value_list = [i-inc_dec_value for i in value_list]
    inc_str = ' ' + ' '.join(list(map(str, inc_value_list))) + '\n'
    dec_str = ' ' + ' '.join(list(map(str, dec_value_list))) + '\n'
    hmm_lines[8] = inc_str
    with open(pwd + '/' + hmm_path + '_1', 'w') as fw1:
        fw1.writelines(hmm_lines)
    hmm_lines[8] = dec_str
    with open(pwd + '/' + hmm_path + '_2', 'w') as fw2:
        fw2.writelines(hmm_lines)


