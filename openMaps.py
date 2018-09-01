#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 22:34:43 2018

@author: abhishek
"""

import webbrowser, sys

if len(sys.argv)>1:
    address=' '.join(sys.argv[1:])
    
webbrowser.open('https://www.google.com/maps/place/'+address)