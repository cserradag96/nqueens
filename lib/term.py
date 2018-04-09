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
# CLASS DECLARATION:
#######################################################################################################################

class Term:
    def __init__(self, name, negative=False):
        self.name = str(name)
        self.negative = negative

    def __str__(self):
        return ("-" if self.negative else "") + self.name

    def __neg__(self):
        return Term(self.name, True)

#######################################################################################################################
# :)
#######################################################################################################################
