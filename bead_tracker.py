import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    # Initialize p (int), tau (float), delta (float) and frames (str[]) as command-line arguments.
    p = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    frames = sys.argv[4:]
    # Creates the object BlobFinder and initializes it to the variable bf, with the
    # parameters being the first value in frames and the command-line argument tau.
    bf = BlobFinder(Picture(frames[0]), tau)
    # Creates the variable prevBeads, sets it to the object BlobFinder with the getBeads method.
    prevbeads = bf.getBeads(p)
    for i in range(1, len(frames)):
        bf = BlobFinder(Picture(frames[i]), tau)
        currbeads = bf.getBeads(p)
        # For each bead currBead in currBeads, find a bead prevBead from prevBeads
        # that is no further than delta and is closest to
        # currBead, and if such a bead is found, write its distance
        # (using format string ’%.4f\n’) to currBead.
        for currBead in currbeads:
            closest = math.inf
            for prevBead in prevbeads:
                r = currBead.distanceTo(prevBead)
                if r <= delta and r < closest:
                    closest = r
            if closest != math.inf:
                stdio.writef('%.4f\n', closest)
        # Write a newline character.
        stdio.writeln()
        # Sets prevbeads to currbeads
        prevbeads = currbeads


if __name__ == '__main__':
    main()
