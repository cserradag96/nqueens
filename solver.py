#!/usr/bin/python3
# -*- encoding: utf-8 -*-

#######################################################################################################################
# DESCRIPTION:
#######################################################################################################################

# Solver for N-Queens using Minisat

#######################################################################################################################
# AUTHORS:
#######################################################################################################################

# Carlos Serrada, 13-11347, <cserradag96@gmail.com>
# Juan Ortiz, 13-11021 <ortiz.juan14@gmail.com>

#######################################################################################################################
# PATH:
#######################################################################################################################

from sys import path       # System path
from os import getcwd      # Current path
from os.path import join   # Join paths

# Add custom lib path to application path
path.append(join(getcwd(), "lib"))

#######################################################################################################################
# DEPENDENCIES:
#######################################################################################################################

import sys
from nqueens import *

#######################################################################################################################
# MAIN:
#######################################################################################################################

if __name__ == "__main__":
    size = sys.argv[1]

    printStatus("Generando CNF")
    puzzle = NQueens(readNQ(size))

    printStatus("Guardando CNF")
    writeFile(puzzle.cnf, "input.txt")

    printStatus("Ejecutando minisat")
    minisat("input.txt", "output.txt")

    printStatus("Generando imagen")
    writeFile(puzzle.genBitmap("output.txt"), namePBM(size))

#######################################################################################################################
# :)
#######################################################################################################################
