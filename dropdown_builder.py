#!/usr/bin/python3
import sys 
import modules.cli as cli
from modules.dropdown import Dropdown
from modules.csv_class import CSV

def main():
    args = sys.argv
    if len(args) == 3:
        try:
            csv_file = CSV(args[1])
            f = open(args[2], 'x')
            for row in csv_file:
                f.write(str(Dropdown(row[0],row[1])))
        except FileNotFoundError:
            print('File not found')
        except FileExistsError:
            print('Cannot write file that already exists')
    else:
        print(cli.usage())
main()