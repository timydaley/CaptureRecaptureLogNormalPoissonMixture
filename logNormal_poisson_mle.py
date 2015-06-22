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

from __future__ import print_function
import numpy as np
import sys
import argparse
import math


# read data
def read_counts(input_file):
  counts = []
  for line in input_file:
    count = line.split('\t')
    # ensure that the counts are one per line
    if len(count) != 1 :
      print("counts must be a single column file\n", file = sys.stderr)
    # end if
    assert(len(count) == 1)
    counts.append(int(count[0]))
  # form histogram from counts using numpy histogram
  np.asarray(counts)
  max_count = np.amax(counts)
  counts_hist, bin_edges = np.histogram(counts, bins = range(1, max_count + 2), range = [1, max_count + 2])
  return counts_hist 
  

def read_hist(input_file):
  counts_hist = []
  indexes = []
  for line in input_file:
    split_line = line.split('\t')
    # ensure lines are two columns
    if len(split_line) != 2 :
      print("counts hist must be two columns per line\n", file = sys.stderr)
    # end if
    assert(len(split_line == 2))
    indx = int(split_line[0])
    indexes.append(indx)
    if indx > 1 :
      indx_jump = indx - indexes[-2] - 1
      if indx_jump > 0 :
        filler = [0]*indx_jump
        counts_hist.append(filler)
    # end both ifs
    count_freq = int(split_line[1])
    counts_hist.append(count_freq)
  return np.asarray(counts_hist)

def main():
  parser = argparse.ArgumentParser(description = 'MLE for log-Normal Poisson capture-recapture counts data')
  parser.add_argument('-i', '--input_filename', dest='input_filename',
                      type=argparse.FileType('r'),
                      help='input file name')
  parser.add_argument('-H', '--HISTOGRAM', action = "store_true",
                      dest = 'HISTOGRAM', default = False, 
                      help = "input file is a two column histogram")
  parser.add_argument('-V', '--VERBOSE', action = "store_true",
                      dest = 'VERBOSE', default = False,
                      help = "run in verbose mode")
  #
  args = parser.parse_args()
  # read in files
  counts_hist = np.array([])
  # input file is a histogram
  if args.HISTOGRAM :
    counts_hist = read_hist(args.input_filename)
  else :
    counts_hist = read_counts(args.input_filename)
  if args.VERBOSE :
    print("Counts_hist :", file = sys.stderr)
    for indx in xrange(0, len(counts_hist)) :
      print("%s\t%s" % (indx + 1, counts_hist[indx]), file = sys.stderr)
# end of main

if __name__ == '__main__':
  main()
    
                      


