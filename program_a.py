import sys
import random

def main():
    """
    Reads commands from stdin and responds accordingly.
    Available commands:
    - Hi: Responds with 'Hi'.
    - GetRandom: Responds with a pseudo-random integer.
    - Shutdown: Gracefully terminates the program.
    Any unknown commands are ignored.
    """
    for line in sys.stdin:
        command = line.strip()
        if command == 'Hi':
            print('Hi')
            sys.stdout.flush()
        elif command == 'GetRandom':
            random_number = random.randint(1, 100)
            print(random_number)
            sys.stdout.flush()
        elif command == 'Shutdown':
            break
        else:
            # Ignore unknown commands
            pass
    # Gracefully terminate
    sys.exit(0)

if __name__ == '__main__':
    main()

