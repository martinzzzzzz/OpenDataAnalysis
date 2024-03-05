#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:01:18 2024

@author: martin
"""

import os
import sys
from pathlib import Path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import action


def test_action():
    
    o = 'test/test_outputs/'
    oh = 'test/test_outputs/test_header'
    wcf = 'test/test_wordClouds'
    lolf = 'test/test_listOfLinks'
    fpaf = 'test/test_figuresperArticle'
    
    action(oh,o,wcf,lolf,fpaf)
    
    assert os.path.exists(wcf)
    assert os.path.exists(lolf)
    assert os.path.exists(fpaf)
    assert os.path.exists(os.path.join(fpaf, 'figure.png'))
    assert os.path.exists(os.path.join(wcf, 'test_file.png'))
    assert os.path.exists(os.path.join(lolf, 'test_file.txt'))

    # Clean up the test files
    os.remove(os.path.join(wcf, 'test_file.png'))
    os.remove(os.path.join(lolf, 'test_file.txt'))
    os.remove(os.path.join(fpaf, 'figure.png'))