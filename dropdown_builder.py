#!/usr/bin/python3
import sys
from modules.dropdown import Dropdown
from modules.csv_class import CSV

def main():
    args = sys.argv
    if len(args) == 2:
        try:
            c = CSV(args[1])
            for i in range(len(c)):
                header = c[0][0]
                body = c[0][1]
                print(Dropdown(header,body))
        except FileNotFoundError:
            print('File not found')
    else:
        help()

def help():
    """
        CLI help message
    """
    print('Usage: dropdown_builder [filename]')
    
main()