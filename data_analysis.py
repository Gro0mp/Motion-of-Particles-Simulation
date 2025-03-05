import math
import stdio


# Entry point.
def main():
    # Initialzes variables ETA, RHO, T, R, and METER_PER_PIXEL to their appropriate
    # values.
    ETA = 9.135e-4
    RHO = 0.5e-6
    T = 297.0
    R = 8.31457
    METERS_PER_PIXEL = 1.75e-7
    # Sets the counter n to zero.
    n = 0

    # While the input is not empty, run the while loop.
    while not stdio.isEmpty():
        # Reads from standard input.
        displacements = stdio.readAllFloats()
        # Calculate var as the sum of the squares of the n displacements
        # (each converted from pixels to meters) read from standard input.
        var = sum(map(lambda r: math.pow(METERS_PER_PIXEL * r, 2), displacements))
        # Divide var by 2 * n
        var = var / (2 * len(displacements))
        # Increments n by 1
        n += 1
        # Estimate Boltzmann’s constant as 6 * math.pi * var * ETA * RHO / T.
        BOLTZMANN = (6 * math.pi * var * ETA * RHO) / T
        # Estimate Avogadro’s constant as R / BOLTZMANN.
        AVOGADRO = R / BOLTZMANN
        # Write to standard output the two constants in scientific notation
        # (using the format string ’%e’) and separated by a space.
        stdio.writef('%e %e\n', BOLTZMANN, AVOGADRO)


if __name__ == '__main__':
    main()
