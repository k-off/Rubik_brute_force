#******************************************************************************#
#                                                                              #
#                                                         ::::::::             #
#    Solver class                                       :+:    :+:             #
#                                                      +:+                     #
#    By: pacovali <marvin@codam.nl>                   +#+                      #
#                                                    +#+                       #
#    Created: 2019/01/01 00:00:00 by pacovali      #+#    #+#                  #
#    Updated: 2019/01/01 00:00:00 by pacovali      ########   odam.nl          #
#                                                                              #
#******************************************************************************#

import numpy as np
import copy
from Rubik_class import Rubik

class Solver :
    def __init__(self, initial_mixed) :
        self.reference = Rubik();
        self.mixed = copy.deepcopy(initial_mixed);
        self.sequence = "";
        self.peak_moves = 0;
        self.allowed = np.array(["R", "R2", "R'",
                                "L", "L2", "L'",
                                "F", "F2", "F'",
                                "B", "B2", "B'",
                                "U", "U2", "U'",
                                "D", "D2", "D'"]);
        self.inverse = np.array([["R'"], ["R'", "R'"], ["R"],
                                ["L'"], ["L'", "L'"], ["L"],
                                ["F'"], ["F'", "F'"], ["F"],
                                ["B'"], ["B'", "B'"], ["B"],
                                ["U'"], ["U'", "U'"], ["U"],
                                ["D'"], ["D'", "D'"], ["D"],
                                ]);

    from solver_methods import solve;