#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 07:41:55 2022

@author: brachuno
"""

# this is the file which calls the instance of SantaCruz
# instantiates it with the configuration, and runs it

import sys
file_name = sys.argv[1]


with open(file_name) as f:
  params = {str(k): v for line in f for (k, v) in [line.strip().split(None, 1)]}

# params conatins everything which controls the model. Really there are 2 parts:
    # one is the set of droughts we will simulate over. This is just a
    # file we point to.
    #
    # the other parts are the actual parameters of the model. Things like
    # the choice of mitigaiton, curtailment infrastructure size etc...

# Now we instantiate our santa cruz class object with our given run parameters