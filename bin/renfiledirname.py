# -*- coding: utf-8 -*-
# !/usr/bin/env python3

__author__ = "Vicentini Tommaso"
__version__ = "01.01"

import os
import sys


ezmode = False


def main():
    """
    main
    :return: none
    """
    before = " "
    after = "_"
    directory = ".\\"

    if ezmode == 0:
        if len(sys.argv) <= 2 or len(sys.argv) > 4:
            bin_answer = 0
            while bin_answer == 0:
                before = input("before:  ")
                if before == "":
                    answer = input("are you sure of what you are doing (Y)?  ")
                    answer = answer.lower()
                    if answer == "y":
                        bin_answer = 1
                else:
                    bin_answer = 1

            after = input("after:  ")
            directory = ".\\" + input("directory(press ENTER for current directory):  ")
            if directory == "":
                directory = ".\\"

        elif len(sys.argv) == 3:
            before = sys.argv[1]
            after = sys.argv[2]

        elif len(sys.argv) == 4:
            before = sys.argv[1]
            after = sys.argv[2]
            directory = ".\\" + sys.argv[3]

    try:
        for root, dirs, files in os.walk(directory):
            for i in files:
                if i != __file__.split("\\")[-1]:   #nome del file corrente
                    v_file = i.split(".")
                    os.rename(os.path.join(root, i), os.path.join(root, v_file[0].replace(before, after) + "." + v_file[1]))
            for i in dirs:
                os.rename(os.path.join(root, i), os.path.join(root, i.replace(before, after)))
    except OSError:
        reserved_names = "CON PRN AUX NUL COM1 COM2 COM3 COM4 COM5 COM6 COM7 COM8 COM9 " \
                         "LPT1 LPT2 LPT3 LPT4 LPT5 LPT6 LPT7 LPT8 LPT9"
        reserved_characters = '\\ / : * ? " < > |'
        print("there are invalid characters[" + reserved_characters + "  " + reserved_names + "]")
        pass
    exit()


if __name__ == "__main__":
    main()
