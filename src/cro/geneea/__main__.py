#-*- coding: utf-8 -*-

"""
The command line interface.
"""
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", required=True, help="source filename")
    
    args = vars(parser.parse_args())
    print("Geneea API hello")

    client = Client(args['--file'])

    # TODO arguments = parser.parse_args()
