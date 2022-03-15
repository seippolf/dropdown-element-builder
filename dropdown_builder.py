#!/usr/bin/python3
import sys 
import modules.cli as cli
from modules.dropdown import Dropdown
from modules.csv_class import CSV

def main():
    args = sys.argv
    if len(args) == 2:
        try:
            csv_file = CSV(args[1])
            for row in csv_file:
                print(Dropdown(row[0],row[1]))
        except FileNotFoundError:
            print('File not found')
    else:
        print(cli.usage())
main()