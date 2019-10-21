#******************************************************************************#
#                                                                              #
#                                                         ::::::::             #
#    rubik_methods module                               :+:    :+:             #
#                                                      +:+                     #
#    By: pacovali <marvin@codam.nl>                   +#+                      #
#                                                    +#+                       #
#    Created: 2019/01/01 00:00:00 by pacovali      #+#    #+#                  #
#    Updated: 2019/01/01 00:00:00 by pacovali      ########   odam.nl          #
#                                                                              #
#******************************************************************************#

import numpy as np

def F_rotate(self, amount, axes) :
    self.F = np.rot90(self.F, amount, axes);
    for i in range(0, amount) :
        for j in range(3) :
            if (axes[0] < axes[1]) :
                tmp = [self.U[2][j], self.R[j][0], self.D[0][2 - j], self.L[2 - j][2]];
            else :
                tmp = [self.D[0][2 - j], self.L[2 - j][2], self.U[2][j], self.R[j][0]];
            self.U[2][j] = tmp[1];
            self.R[j][0] = tmp[2];
            self.D[0][2 - j] = tmp[3];
            self.L[2 - j][2] = tmp[0];

def R_rotate(self, amount, axes) :
    self.R = np.rot90(self.R, amount, axes);
    for i in range(amount) :
        for j in range(3) :
            if (axes[0] < axes[1]) :
                tmp = [self.U[2 - j][2], self.B[j][0], self.D[2 - j][2], self.F[2 - j][2]];
            else :
                tmp = [self.D[2 - j][2], self.F[2 - j][2], self.U[2 - j][2], self.B[j][0]];
            self.U[2 - j][2] = tmp[1];
            self.B[j][0] = tmp[2];
            self.D[2 - j][2] = tmp[3];
            self.F[2 - j][2] = tmp[0];

def B_rotate(self, amount, axes) :
    self.B = np.rot90(self.B, amount, axes);
    for i in range(amount) :
        for j in range(3) :
            if (axes[0] < axes[1]) :
                tmp = [self.U[0][2 - j], self.L[j][0], self.D[2][j], self.R[2 - j][2]];
            else :
                tmp = [self.D[2][j], self.R[2 - j][2], self.U[0][2 - j], self.L[j][0]];
            self.U[0][2 - j] = tmp[1];
            self.L[j][0] = tmp[2];
            self.D[2][j] = tmp[3];
            self.R[2 - j][2] = tmp[0];

def L_rotate(self, amount, axes) :
    self.L = np.rot90(self.L, amount, axes);
    for i in range(amount) :
        for j in range(3) :
            if (axes[0] < axes[1]) :
                tmp = [self.U[j][0], self.F[j][0], self.D[j][0], self.B[2 - j][2]];
            else :
                tmp = [self.D[j][0], self.B[2 - j][2], self.U[j][0], self.F[j][0]];
            self.U[j][0] = tmp[1];
            self.F[j][0] = tmp[2];
            self.D[j][0] = tmp[3];
            self.B[2 - j][2] = tmp[0];

def U_rotate(self, amount, axes) :
    self.U = np.rot90(self.U, amount, axes);
    for i in range(0, amount) :
        for j in range(3) :
            if (axes[0] < axes[1]) :
                tmp = [self.B[0][2 - j], self.R[0][2 - j], self.F[0][2 - j], self.L[0][2 - j]];
            else :
                tmp = [self.F[0][2 - j], self.L[0][2 - j], self.B[0][2 - j], self.R[0][2 - j]];
            self.B[0][2 - j] = tmp[1];
            self.R[0][2 - j] = tmp[2];
            self.F[0][2 - j] = tmp[3];
            self.L[0][2 - j] = tmp[0];

def D_rotate(self, amount, axes) :
    self.U = np.rot90(self.U, amount, axes);
    for i in range(0, amount) :
        for j in range(3) :
            if (axes[0] < axes[1]) :
                tmp = [self.F[2][j], self.R[2][j], self.B[2][j], self.L[2][2 - j]];
            else :
                tmp = [self.B[2][j], self.L[2][2 - j], self.F[2][j], self.R[2][j]];
            self.F[2][j] = tmp[1];
            self.R[2][j] = tmp[2];
            self.B[2][j] = tmp[3];
            self.L[2][2 - j] = tmp[0];