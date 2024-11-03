import subprocess
from statistics import median, mean

QUERIES = {
    "Hi": 1,
    "GetRandom": 100,
    "Shutdown": 1
}

gotten_numbers = []
random_tries = 1

process = subprocess.Popen(
    ["python3", "program_a.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)
'''
Program B will launch Program A as a separate process, provided as an argument. Once Program A is running, Program B should: D
Send the Hi command to Program A and verify the correct response. D
Retrieve 100 random numbers by sending the GetRandom command to Program A 100 times. D
Send the Shutdown command to Program A to terminate it gracefully. D
Sort the list of retrieved random numbers and print the sorted list to the console. D
Calculate and print the median and average of the numbers. D
'''


def process_response(query, res):
    global gotten_numbers
    global random_tries
    if query == "Hi" and res == "Hi":
        print("Hi Successful")
    elif query == "GetRandom":
        try:
            num = float(res)
            print(f"{random_tries}. GetNumber Successful")
            random_tries += 1
            gotten_numbers.append(num)
        except ValueError:
            print("ERR|GetRandom not valid float number")
    elif res == "":
        pass
    else:
        print("ERR|Not known answer!", res)


for KEY in QUERIES.keys():
    for i in range(QUERIES[KEY]):
        process.stdin.write(KEY + "\n")
        process.stdin.flush()

        response = process.stdout.readline().strip()
        process_response(KEY, response)

print("Sorted numbers:\n", sorted(gotten_numbers))
print("Median\n", median(gotten_numbers))
print("Average\n", mean(gotten_numbers))

process.stdin.close()
process.stdout.close()
process.wait()
