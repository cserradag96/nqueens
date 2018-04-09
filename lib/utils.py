# -*- encoding: utf-8 -*-

#######################################################################################################################
# DESCRIPTION:
#######################################################################################################################

# TODO

#######################################################################################################################
# AUTHORS:
#######################################################################################################################

# Carlos Serrada, 13-11347, <cserradag96@gmail.com>
# Juan Ortiz, 13-11021 <ortiz.juan14@gmail.com>

#######################################################################################################################
# DEPENDENCIES:
#######################################################################################################################

from subprocess import Popen, PIPE, STDOUT
from os.path import basename

#######################################################################################################################
# FUNCTIONS:
#######################################################################################################################

# Read a file.non
def readNQ(size):
    return int(size)

# Write content into file
def writeFile(content, file_path):
    with open(file_path, 'w') as file:
        file.write(str(content))

# Translate booleans into bits string
def boolToBits(x):
    return '1' if x else '0'

# Iterator for stdout
def iterStdout(p):
  while True:
    line = p.stdout.readline()
    if not line: break
    yield str(line)[2:-3]

# Minisat pipe
def minisat(input_path, output_path):
    print("")
    command = "./minisat/core/minisat " + input_path + " " + output_path
    process = Popen(command.split(), stdout=PIPE, stderr=STDOUT)
    for line in iterStdout(process):
        print(line)

# Function to print verbose messages
def printStatus(status):
    separator = "\n======================\n"
    message = separator + "# " + status + separator
    print(message, end="")

# Extract name from file_path and add pbm format
def namePBM(size):
    return size + ".pbm"

#######################################################################################################################
# :)
#######################################################################################################################
