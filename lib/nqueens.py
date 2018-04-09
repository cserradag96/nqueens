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

from term import Term
from clause import Clause
from cnf import CNF
from utils import *

#######################################################################################################################
# CLASS DECLARATION:
#######################################################################################################################

class NQueens:
    def __init__(self, size):
        self.size = size
        self.cnf = self.genCNF()

    # Generate CNF
    def genCNF(self):
        n = self.size
        expression = CNF(n)

        # Cell clauses
        for i in range(n):
            terms = []
            for j in range(1, n + 1):
                terms.append(Term(j + n*i))
            expression.add(Clause(terms))

        # Row clauses
        for i in range(n):
            for j in range(1, n):
                number = n*i + j
                for l in range(1, n - j + 1):
                    expression.add(Clause([-Term(number), -Term(number + l)]))

        # Columns clauses
        for j in range(1, n+1):
            for i in range(n):
                number = n*i + j
                for l in range(1, n - i):
                    expression.add(Clause([-Term(number), -Term(number + l*n)]))

        # Clauses diagonals left to right (upper bound)
        for i in range(n-1):
            for j in range(i, n-1):
                number = n*i + j + 1
                for l in range(1, n - j):
                    expression.add(Clause([-Term(number), -Term(number + l*(n + 1))]))

        # Clauses diagonals left to right (lower bound)
        for i in range(n-1):
            for j in range(i):
                number = n*i + j + 1
                for l in range(1, n - i):
                    expression.add(Clause([-Term(number), -Term(number + l*(n + 1))]))

        # Clauses diagonals right to left (upper bound)
        for i in range(n):
            for j in range(n-i):
                number = n*i + j + 1
                for l in range(1, j + 1):
                    expression.add(Clause([-Term(number), -Term(number + l*(n - 1))]))

        # Clauses diagonals right to left (lower bound)
        for i in range(n):
            for j in range(n-i, n):
                number = n*i + j + 1
                if (number != n*n):
                    for l in range(1, n - i):
                        expression.add(Clause([-Term(number), -Term(number + l*(n - 1))]))

        return expression

    # Solve problem
    def solve(self, output_path):
        variables = self.cnf.parse(output_path)
        if len(variables) == 0:
            print("No se pudo encontrar ninguna solución")
            sys.exit(1)

        return [[variables[self.size*i + j] for j in range(self.size)] for i in range(self.size)]

    # Generate bitmap image
    def genBitmap(self, output_path):
        header = "P1\n" + str(self.size) + " " + str(self.size) + "\n"
        bitmap = "\n".join([" ".join([boolToBits(x) for x in row]) for row in self.solve(output_path)])
        return header + bitmap + "\n"

#######################################################################################################################
# :)
#######################################################################################################################
