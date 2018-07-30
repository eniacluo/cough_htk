#!/usr/bin/python3

import random
import os
import sys

pwd = os.getcwd()

if len(sys.argv) != 2:
    print('name of list required!')
    exit(1)

name = sys.argv[1]
listfile = pwd + '/' + name + '_list.scp'

if not os.path.isfile(listfile):
    print(listfile + ' does not exist!')
    exit(1)

with open(listfile, 'r') as f:
    files = f.readlines()
    all_count = len(files)
    all_index = list(range(all_count))
    training_count = int(all_count*0.8)
    testing_count = all_count - training_count

    for i in range(1000):
        ia = int(random.random()*all_count)
        ib = int(random.random()*all_count)
        temp = files[ia]
        files[ia] = files[ib]
        files[ib] = temp

    if len(sys.argv) > 2 and sys.argv[2] == '1':
        with open(pwd + '/' + name + '_training.scp', 'w') as fwtr:
            for i in range(training_count):
                fwtr.write(files[all_index[i]])

        with open(pwd + '/' + name + '_testing.scp', 'w') as fwte:
            for i in range(testing_count):
                fwte.write(files[all_index[i+training_count]])
    else:
        for i in range(5):
            index_testing = int(i*0.2*all_count)
            files_copy = files
            with open(pwd + '/' + name + '_testing' + str(i+1) + '.scp', 'w') as fwte:
                for j in range(testing_count):
                    fwte.write(files_copy[index_testing + j])

            with open(pwd + '/' + name + '_training' + str(i+1) + '.scp', 'w') as fwtr:
                for j in range(all_count):
                    if not (j >= index_testing and j < index_testing + testing_count):
                        fwtr.write(files_copy[j])




