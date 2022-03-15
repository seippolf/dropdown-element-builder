from dropdown import Dropdown
from csv_class import CSV
from time import sleep
import sys


def main():
    args = sys.argv
    if len(args) == 2:
        try:
            c = CSV(args[1])
            for i in range(len(c)):
                header = c.get(i)[0]
                body = c.get(i)[1]
                print(Dropdown(header,body))
        except FileNotFoundError:
            print('File not found')
    else:
        help()
def help():
    print('Usage: dropdown_builder [filename]')
main()