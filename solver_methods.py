#******************************************************************************#
#                                                                              #
#                                                         ::::::::             #
#   solver_methods module                               :+:    :+:             #
#                                                      +:+                     #
#    By: pacovali <marvin@codam.nl>                   +#+                      #
#                                                    +#+                       #
#    Created: 2019/01/01 00:00:00 by pacovali      #+#    #+#                  #
#    Updated: 2019/01/01 00:00:00 by pacovali      ########   odam.nl          #
#                                                                              #
#******************************************************************************#

import numpy as np
from Rubik_class import Rubik

MAX_MOVES = 20;

def compare_cubes(self) :
    return (np.array_equal(self.reference.F, self.mixed.F) and
        np.array_equal(self.reference.R, self.mixed.R) and
        np.array_equal(self.reference.B, self.mixed.B) and
        np.array_equal(self.reference.L, self.mixed.L) and
        np.array_equal(self.reference.U, self.mixed.U) and
        np.array_equal(self.reference.D, self.mixed.D));
    exit();

def check_iterator(i, skip) :
    if skip < 0 :
        return (False);
    if (skip % 2 == 0 and i // 3 == skip) :
        return (True);
    if (skip % 2 == 1 and (skip - (i // 3) == 1 and skip - (i // 3) == 0)) :
        return (True);
    return (False);

def try_next(self, current_move_nr, allowed, inverse, solution, skip) :
    current_move_nr += 1;
    i = 0;
    for move in allowed :
        if check_iterator(i, skip) == False:
            solution = np.append(solution, move);
            self.mixed.choose_rotation(move);
            is_equal = compare_cubes(self);
            if is_equal == True:
                return (np.array([True, solution]));
            if is_equal == False and current_move_nr < self.peak_moves:
                result = try_next(self, current_move_nr, allowed, inverse, solution, i // 3);
                if (result[0] == True):
                    return (result);
            for inv in inverse[i]:
                self.mixed.choose_rotation(inv);
            solution = np.delete(solution, -1);
        i += 1;
    current_move_nr -= 1;
    return (np.array([False, solution]));

def solve(self):
    solution = np.array([]);
    solved = [False, solution];
    while self.peak_moves < MAX_MOVES and solved[0] == False:
        self.peak_moves += 1;
        solved = try_next(self, 0, self.allowed, self.inverse, solution, -1);
        if (solved[0] == True):
            return (solved[1]);