import re


def get_game_id(line):
    m = re.match(r"Game (\d+):", line)
    return int(m.group(1))


def get_min_cubes_power(line):
    red_cubes = re.findall(r"(\d+)\s*red", line)
    red_cubes = [int(x) for x in red_cubes]
    if not red_cubes:
        min_red_cubes = 0
    else:
        min_red_cubes = max(red_cubes)

    green_cubes = re.findall(r"(\d+)\s*green", line)
    green_cubes = [int(x) for x in green_cubes]
    if not green_cubes:
        min_green_cubes = 0
    else:
        min_green_cubes = max(green_cubes)

    blue_cubes = re.findall(r"(\d+)\s*blue", line)
    blue_cubes = [int(x) for x in blue_cubes]
    if not blue_cubes:
        min_blue_cubes = 0
    else:
        min_blue_cubes = max(blue_cubes)

    print(f"Min Red = {min_red_cubes}, Min Green = {min_green_cubes}, Min Blue = {min_blue_cubes}")
    power = min_red_cubes * min_green_cubes * min_blue_cubes
    print(f"Power = {power}")
    return power


def is_game_possible(line):
    rolls = line.split(";")

    for roll in rolls:
        red_cubes = re.search(r"(\d+)\s*red", roll)
        if red_cubes is None:
            red_cubes = "(0,0)"
        if int(red_cubes[1]) > 12:
            return False

        blue_cubes = re.search(r"(\d+)\s*blue", roll)
        if blue_cubes is None:
            blue_cubes = "(0,0)"
        if int(blue_cubes[1]) > 14:
            return False

        green_cubes = re.search(r"(\d+)\s*green", roll)
        if green_cubes is None:
            green_cubes = "(0,0)"
        if int(green_cubes[1]) > 13:
            return False

    return True


def problem_2(file_name) -> int:
    ans = 0

    with open(file_name) as f:
        for line in f:
            line = line.rstrip()
            power = get_min_cubes_power(line)
            ans = ans + power
    print(f"Total power, {ans}")
    return ans


def problem_1(file_name):
    ans = 0
    with open(file_name) as f:
        for line in f:
            line = line.rstrip()
            game_id = get_game_id(line)
            game_status = is_game_possible(line)
            if game_status is True:
                ans = ans + game_id
            print(f"Game ID: {game_id} is possible? {game_status}")
    print(f"Answer for P1: {ans}")


if __name__ == "__main__":
    # problem_1("input.txt")
    problem_2("input.txt")
