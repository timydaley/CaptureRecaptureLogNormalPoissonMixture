# logNormal_poisson_mle:
#   a tool to compute the maximum likelihood estimators
#   for zero-truncated log-Normal Poisson count data
#   
#    Copyright (C) 2015 Timothy Daley
# 
#    Authors: Timothy Daley
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.	If not, see <http://www.gnu.org/licenses/>.

import sys
import argparse
import math
from __future__ import print_function

# read data
def read_count_data(input_file)
  counts = []
  for line in input_file :
    count = line.split('\t')
    # ensure that the counts are one per line
    if(!(len(count) == 1))
      print("counts must be a single column file", file = sys.stderr)
    assert(len(count) == 1)
    counts.append(count[0])
  # form histogram from counts
  max_count = max(counts, key = int)

def read_hist_data(