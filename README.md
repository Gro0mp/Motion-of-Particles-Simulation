# Motion-of-Particles-Simulation

## Overview

This project is a computational recreation of Jean Baptiste Perrin's groundbreaking 1908 experiment that provided direct evidence for the atomic nature of matter. By tracking the motion of polystyrene beads undergoing Brownian motion, the code estimates fundamental physical constants and demonstrates the random molecular interactions predicted by Einstein's kinetic theory.

## Background

In 1827, botanist Robert Brown observed the random erratic motion of pollen grains in water. In 1905, Albert Einstein developed a quantitative theory of Brownian motion, hypothesizing that this movement resulted from millions of tiny water molecules colliding with larger particles. Jean Baptiste Perrin experimentally validated this theory in 1908, winning the 1926 Nobel Prize in Physics.

## Project Components

The project consists of several Python scripts that work together to analyze Brownian motion:

### 1. `blob.py`
- Defines a `Blob` class to represent particles
- Tracks center of mass and pixel count for each particle
- Calculates Euclidean distances between blobs

### 2. `blob_finder.py`
- Identifies blobs (potential particles) in microscope images
- Uses luminance thresholding to separate foreground and background
- Implements depth-first search to find connected pixel components

### 3. `bead_tracker.py`
- Tracks bead movement between consecutive image frames
- Identifies and calculates displacement of beads
- Handles cases where beads may disappear from view

### 4. `data_analysis.py`
- Analyzes bead displacement data
- Estimates Boltzmann's constant
- Calculates Avogadro's constant

## Prerequisites

- Python 3.x
- NumPy (optional, depending on implementation)
- Image processing libraries (used in original implementation)

## Usage

### Tracking Beads

```bash
python3 bead_tracker.py [pixels] [tau] [delta] [image_files]
```

Example:
```bash
python3 bead_tracker.py 25 180.0 25.0 data/run_1/frame00000.jpg data/run_1/frame00001.jpg
```

### Analyzing Data

```bash
python3 bead_tracker.py [pixels] [tau] [delta] [image_files] | python3 data_analysis.py
```

## Scientific Parameters

- Temperature (T): 297 K (room temperature)
- Water Viscosity (η): 9.135 × 10^-4 N·s/m²
- Bead Radius (ρ): 0.5 × 10^-6 m
- Meters per Pixel: 1.75 × 10^-7 m

## Key Concepts

- Luminance Thresholding
- Depth-First Search for Blob Detection
- Euclidean Distance Calculation
- Einstein-Smoluchowski Equation
- Stokes-Einstein Relation

## Acknowledgements

Adapted from the Atomic Nature of Matter assignment developed at Princeton University by David Botstein, Tamara Broderick, Ed Davisson, Daniel Marlow, William Ryu, and Kevin Wayne.
