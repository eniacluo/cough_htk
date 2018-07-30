#!/usr/bin/python3

import random
import os
import sys

pwd = os.getcwd()

if len(sys.argv) != 5:
    print('<name> <vecSize> <stateNum> <GaussianNum> required!')
    exit(1)

try:
    hmm_name = sys.argv[1]
    hmm_vecSize = int(sys.argv[2])
    hmm_stateNum = int(sys.argv[3])
    hmm_GaussianNum = int(sys.argv[4])
except ValueError:
    print('input is not valid number!')
    exit(1)

with open(pwd + '/' + hmm_name, 'w') as f:
    f.write('  ~o <VecSize> ' + str(hmm_vecSize) + ' <MFCC_0>\n')
    f.write('  ~h' + '\"' + hmm_name + '\"\n')
    f.write('<BeginHMM>\n')
    f.write('  <NumStates> ' + str(hmm_stateNum) + '\n')
    for i in [i+2 for i in range(hmm_stateNum - 2)]:
        f.write('    <State> ' + str(i) + ' <NumMixes> ' + str(hmm_GaussianNum) + '\n')
        for j in range(hmm_GaussianNum):
            f.write('      <Mixture> ' + str(j+1) + ' ' + str(1/hmm_GaussianNum) + '\n')
            f.write('        <Mean> ' + str(hmm_vecSize) + '\n')
            f.write('          ' + '0.0 '*hmm_vecSize + '\n')
            f.write('        <Variance> ' + str(hmm_vecSize) + '\n')
            f.write('          ' + '1.0 '*hmm_vecSize + '\n')
    f.write('  <TransP> ' + str(hmm_stateNum) + '\n')
    for i in range(hmm_stateNum):
        f.write('    ')
        for j in range(hmm_stateNum):
            if i == 0 and j == 1:
                value = 1.0
            elif i == 0:
                value = 0.0
            elif i == hmm_stateNum - 1:
                value = 0.0
            elif i == j:
                value = 0.6
            elif j == i + 1:
                value = 0.4
            else:
                value = 0.0
            f.write(str(value) + ' ')
        f.write('\n')
    f.write('<EndHMM>')
            
