#!/usr/bin/python3

import os
import sys
import logging

# global consts
app_version = "1.0.0"
log_level = 'DEBUG'
log_filename = "stl_to_png.log"
min_python_version = (3, 6)


def validate_python():
    """Validate that the right Python version is running."""
    if sys.version_info[:2] < min_python_version:
        print(f"Error #1: {__file__} requires at least Python version {min_python_version}. Aborting!")
        sys.exit(1)


def log_setup():
    """Start logging to file and write version"""
    logging.basicConfig(format='%(asctime)-16s %(levelname)-8s %(message)s', level=logging.INFO, filename=log_filename)
    log = logging.getLogger()
    log.info(f'Starting {__file__} version: {app_version}')
    log.info(f'Changing log level to {log_level}')
    log.setLevel(log_level)


def test_arguments():
    """Test for arguments passed"""
    if len(sys.argv) != 4:
        msg = 'Error #2: Missing arguments [stl_file] [png_file] [img_size]. Aborting!'
        print(msg)
        logging.critical(msg)
        sys.exit(2)


def main():
    stl_file = sys.argv[1]
    logging.debug(f'Param: STL file to convert: "{stl_file}"')
    png_file = sys.argv[2]
    logging.debug(f'Param: PNG output file: "{png_file}"')
    img_size = sys.argv[3]
    logging.debug(f'Param: IMG size: "{img_size}"')
    logging.info(f'Stopping application')
    return 0


if __name__ == "__main__":
    validate_python()
    log_setup()
    test_arguments()
    sys.exit(main())
