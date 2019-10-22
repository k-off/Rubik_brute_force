#******************************************************************************#
#                                                                              #
#                                                         ::::::::             #
#    Rubik class                                        :+:    :+:             #
#                                                      +:+                     #
#    By: pacovali <marvin@codam.nl>                   +#+                      #
#                                                    +#+                       #
#    Created: 2019/01/01 00:00:00 by pacovali      #+#    #+#                  #
#    Updated: 2019/01/01 00:00:00 by pacovali      ########   odam.nl          #
#                                                                              #
#******************************************************************************#

import numpy as np

class Rubik :
    def __init__(self) :
        self.F = np.array([['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]);
        self.R = np.array([['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]);
        self.L = np.array([['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]);
        self.D = np.array([['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]);
        self.U = np.array([['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]);
        self.B = np.array([['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]);
    from rubik_methods import F_rotate, R_rotate, B_rotate, L_rotate, U_rotate, D_rotate;

    def choose_rotation(self, s) :
        axes = (1, 0);
        amount = 1;
        if (len(s) == 2 and s[1] == "'") :
            axes = (0, 1);
        elif (len(s) == 2 and s[1] == '2') :
            amount = 2;
        if (s[0] == 'F') :
            self.F_rotate(amount, axes);
        if (s[0] == 'R'):
            self.R_rotate(amount, axes);
        if (s[0] == 'L') :
            self.L_rotate(amount, axes);
        if (s[0] == 'D') :
            self.D_rotate(amount, axes);
        if (s[0] == 'U') :
            self.U_rotate(amount, axes);
        if (s[0] == 'B') :
            self.B_rotate(amount, axes);

    def print_rubik(self) :
        print(self.F);
        print(self.R);
        print(self.B);
        print(self.L);
        print(self.U);
        print(self.D, "\n");
