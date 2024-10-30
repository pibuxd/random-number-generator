import sys
import subprocess
import statistics

def main():
    """
    Launches Program A as a subprocess, interacts with it, and processes random numbers.
    Steps:
    1. Send 'Hi' command and verify the response.
    2. Retrieve 100 random numbers by sending 'GetRandom' command 100 times.
    3. Send 'Shutdown' command to terminate Program A.
    4. Sort the numbers, calculate the median and average, and print the results.
    """
    if len(sys.argv) != 2:
        print('Usage: python program_b.py path_to_program_a')
        sys.exit(1)
    
    path_to_program_a = sys.argv[1]

    # Launch Program A as a subprocess
    process = subprocess.Popen(
        [sys.executable, path_to_program_a],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Function to send a command and get a response
    def send_command(command):
        """
        Sends a command to Program A and returns the response.
        """
        try:
            process.stdin.write(command + '\n')
            process.stdin.flush()
            response = process.stdout.readline().strip()
            return response
        except Exception as e:
            print('Error communicating with Program A:', e)
            process.terminate()
            sys.exit(1)

    # Send 'Hi' command and verify response
    response = send_command('Hi')
    if response != 'Hi':
        print('Unexpected response from Program A:', response)
        process.terminate()
        sys.exit(1)

    # Retrieve 100 random numbers
    random_numbers = []
    for _ in range(100):
        response = send_command('GetRandom')
        try:
            number = int(response)
            random_numbers.append(number)
        except ValueError:
            print('Invalid number received:', response)
            process.terminate()
            sys.exit(1)

    # Send 'Shutdown' command
    send_command('Shutdown')
    process.stdin.close()
    process.wait()

    # Sort and print the list of random numbers
    sorted_numbers = sorted(random_numbers)
    print('Sorted Random Numbers:')
    print(sorted_numbers)

    # Calculate and print median and average
    median = statistics.median(sorted_numbers)
    average = statistics.mean(sorted_numbers)
    print('Median:', median)
    print('Average:', average)

if __name__ == '__main__':
    main()

