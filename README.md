# Rubik

### Rubik's cube solver

**Rubik** is an algorithmic project at Codam (42). Objective is to find shortest solution in least possible amount of time.

## Input

User provides as single argument a string containing 1 to 20 movements in standard notation:

    `F, B, R, U, L, D, F', B', R', U', L', D', F2, B2, R2, U2, L2, D2`

where letters stay for both side and rotation notations:

    `F` - front side (rotate front side 90 degrees clockwize)
    `B` - back side (rotate back side 90 degrees clockwize)
    `R` - right side (rotate right side 90 degrees clockwize)
    `U` - upper side (rotate upper side 90 degrees clockwize)
    `L` - left side (rotate left side 90 degrees clockwize)
    `D` - down side (rotate down side 90 degrees clockwize)

    `'` - rotate side _counter-clockwize_
    `2` - rotate side 180 degrees clockwize

Also, `random amount_of_moves` generates a random sequence with user-defined length (1 - 20 moves).

## Output

Program returns a string containing a sequence of moves (see input).

## Algorithm

No elaborate algorithms were applied. A simple brute force with some slight improvements. The worst case will take `1.27 * 10^21 s` (18^input-length) time to solve. The proposed improvements reduce this time to `3.3 * 10^19 s` (15^input-length), which is still too far from an appropriate result.
