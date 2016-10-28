#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Plantilla base para archivos de python
import sys
import logging
import argparse

import mylib

def sample_function(param):
    mylib.do_something()
    return param

def main(argv):
    # My code here
    logging.warning('Sample warning log in main')
    sample_function('Some text')
    print(argv)
    pass

if __name__ == "__main__":
    # Input arguments adquisition
    parser = argparse.ArgumentParser(description='Descripcion de lo que hace el programa')
    # Inputs are set by keyboard in the Python call
    parser.add_argument('PARAM1', nargs=1, help='Primer parametro obligatorio')
    args = parser.parse_args()
    p1 = args.PARAM1[0]

    # Set logger config
    logging.basicConfig(filename='myapp.log',format='%(asctime)s-%(levelname)s-%(name)s: %(message)s', level=logging.DEBUG)

    main(p1)
