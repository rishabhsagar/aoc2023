def get_calibration_digits(line):
    nums = [x for x in line if x.isdigit() ]
    val = int(nums[0] + nums[-1])
    return val

def fix_chars(line):
    print(f"Received line: {line}")
    positions = list()
    r = {
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9}

    for p in r.keys():
        pos = line.find(p)
        if pos > -1:
            positions.append((str(r[p]), pos))
    # Now deal with numbers
    nums = [ x for x in line if x.isdigit() ]
    for num in nums:
        pos = line.find(num)
        if pos > -1:
            positions.append((num, pos))

    sorted_positions = sorted(positions, key=lambda p: p[1])
    line = "".join([x[0] for x in sorted_positions ])
    print(f"Returning line: {line}")
    return line

def p1(filename):
    final = list()

    with open(filename) as f:
        for line in f:
            val = get_calibration_digits(line)
            final.append(val)
    return sum(final)

def p2(filename):
    final = list()

    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            line = fix_chars(line)
            val = get_calibration_digits(line)
            final.append(val)
    print(f"value of final is: {final}")
    return sum(final)

if __name__ == "__main__":
    #problem_file = "sample.txt"
    #ans_p1 = p1(problem_file)
    #print(f"Solution for p1: {ans_p1}")

    problem_file = "input.txt"
    ans_p2 = p2(problem_file)
    print(f"Soluton for p2: {ans_p2}")
