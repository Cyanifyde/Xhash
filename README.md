# Xhash
The homeplace of CrossHash

This repository contains an implementation of a custom hash function. This document provides an overview of how the function works and how to use it.

## Table of Contents

- [Hash Class](#Xhash)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## How It Works

The `Hash` class implemented here defines a hash function that takes a string and a salt value and generates a hash of a specified length. The functionality of the hash function can be broken down into several steps:

1. **Initialization**: When a `Hash` object is instantiated, the hash length can be specified. If not provided, it defaults to 256. The object also maintains several internal lists used during the hash generation process.

    ```python
    hash = Hash(hash_length=256)
    ```

2. **Hash Generation**: The `hash` method takes a string and a salt value, combines them, and generates a hash of the specified length.

    ```python
    hash.hash("input_string", "salt")
    ```

3. **Line Generation**: During the hash generation process, the string is divided into segments, each of which is converted to a pair of coordinates. These coordinates define lines that are used in the intersection calculation.

4. **Intersection Counting and Angle Calculation**: For each line, the number of intersections with the other lines is counted. The angles at these intersections are also calculated. The sum of the intersections and angles is used to generate the hash value.

5. **Trimming**: If the generated hash exceeds the specified length, it is trimmed to fit.
