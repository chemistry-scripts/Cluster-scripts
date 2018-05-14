#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Testing suite for submission scripts.

This version tests OCCIGEN scripts
Last Update 2018-05-12 by Emmanuel Nicolas
email emmanuel.nicolas -at- cea.fr
Requires Python3 to be installed.
"""

import argparse
import sys
import os
import logging
import shlex
import re


def main():
    """
    Main method.

    Get requirements (programs that)
    """
    # Setup logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()

    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    # Get parameters from command line
    options = get_options()

    # Run basic tests

    # For every required program, run the corresponding tests
    if options['adf']:
        run_adf_tests()
    elif options['g09']:
        run_g09_tests()
    elif options['g16']:
        run_g16_tests()
    elif options['orca']:
        run_orca_tests()


def get_options():
    """Check command line options and accordingly set computation parameters."""
    parser = argparse.ArgumentParser(description=help_description(),
                                     epilog=help_epilog())
    parser.formatter_class = argparse.RawDescriptionHelpFormatter
    parser.add_argument('-p', '--programs', default="all", type=str, nargs='+',
                        help="Programs to test. Options: adf, g09, g16, orca, all")

    try:
        args = parser.parse_args()
    except argparse.ArgumentError as error:
        print(str(error))  # Print something like "option -a not recognized"
        sys.exit(2)

    # Get values from parser
    options = dict.fromkeys(['adf', 'g09', 'g16', 'orca'], False)
    options['adf'] = 'adf' in args.programs or 'all' in args.programs
    options['g09'] = 'g09' in args.programs or 'all' in args.programs
    options['g16'] = 'g16' in args.programs or 'all' in args.programs
    options['orca'] = 'orca' in args.programs or 'all' in args.programs

    return options


def help_description():
    """Return description of program for help message."""
    return """Test suite for submission scripts."""


def help_epilog():
    """Return additional help message."""
    return """."""


if __name__ == '__main__':
    main()
