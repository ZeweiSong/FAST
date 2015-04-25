# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:23:08 2015

Please feel free to contact me with any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""

from lib import random_subsample
from lib import ParseOtuTable
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-otu', help='Input OTU table')
parser.add_argument('-d', '--depth', help='Sampling depth for each sample')
parser.add_argument('-iter', default=1, help='Iteration time for each sample')
parser.add_argument('-keep_all', action='store_true', help='Indicate to keep all samples')
args = parser.parse_args()