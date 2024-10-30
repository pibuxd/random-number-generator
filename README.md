# Pseudo-Random Number Generator and Controller

## Introduction

This project consists of two programs:

1. **Program A**: Pseudo-Random Number Generator (`program_a.py`)
   - Reads commands from standard input (`stdin`) and responds via standard output (`stdout`).
   - Handles the following commands:
     - `Hi`: Responds with `'Hi'`.
     - `GetRandom`: Responds with a pseudo-random integer.
     - `Shutdown`: Gracefully terminates the program.
   - Ignores any unknown commands.

2. **Program B**: Controller (`program_b.py`)
   - Launches Program A as a separate process.
   - Communicates with Program A exclusively through `stdin` and `stdout`.
   - Performs the following actions:
     - Sends the `Hi` command and verifies the correct response.
     - Retrieves 100 random numbers by sending the `GetRandom` command 100 times.
     - Sends the `Shutdown` command to terminate Program A gracefully.
     - Sorts the list of retrieved random numbers.
     - Calculates and prints the median and average of the numbers.

## Requirements

- **Python 3.x** installed on your system.
- Operating System: Windows, macOS, or Linux.

## Quick Start Guide

## Quick Start Guide

### 1. Setup

- Place both `program_a.py` and `program_b.py` in the same directory.

- **Set execute permissions (macOS/Linux):**

  In the terminal, navigate to the directory containing the scripts and run:

  ```bash
  chmod +x program_a.py
  chmod +x program_b.py
  ```

### 2. Running the Controller (Program B)

Open a terminal or command prompt, navigate to the directory containing the programs, and run:

```bash
python3 program_b.py program_a.py

