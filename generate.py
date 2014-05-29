#!/usr/bin/env python
from pymarkovchain import MarkovChain
import os

basedir = os.path.abspath(os.path.dirname(__file__))

mc = MarkovChain(os.path.join(basedir, 'sample-markov.db'))

file = open(os.path.join(basedir,'sample-data.txt'), 'r')
mc.generateDatabase(file.read())
file.close