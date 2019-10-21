#******************************************************************************#
#                                                                              #
#                                                         ::::::::             #
#    main module                                        :+:    :+:             #
#                                                      +:+                     #
#    By: pacovali <marvin@codam.nl>                   +#+                      #
#                                                    +#+                       #
#    Created: 2019/01/01 00:00:00 by pacovali      #+#    #+#                  #
#    Updated: 2019/01/01 00:00:00 by pacovali      ########   odam.nl          #
#                                                                              #
#******************************************************************************#

from initial_check import initial_check
from Rubik_class import Rubik
from Solver_class import Solver
import time

commands = initial_check();
mixed = Rubik();

for command in commands :
    mixed.choose_rotation(command);

start_time = time.time()
solver = Solver(mixed);
solution = solver.solve();
print (solution);
print ("--- %.6s seconds ---" % (time.time() - start_time));
