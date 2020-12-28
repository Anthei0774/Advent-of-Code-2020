# Preprocessing

input = open("4.txt").read()
input = input.split("\n\n")

passes = []
for i in range(len(input)):

    input[i] = input[i].replace("\n", " ")
    input[i] = input[i].split(" ")

    p = {}
    for field in input[i]:
        p[ field.split(":")[0] ] = field.split(":")[1]

    passes.append(p)

all_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])

###################################################################################################

# Part 1

V = 0
for p in passes:

    missing_fields = all_fields.difference( set(p) )

    if ( len(missing_fields) == 0 ) or ( len(missing_fields) == 1 and "cid" in missing_fields ):
        V += 1

print("Number of valid passes:", V)

###################################################################################################

# Part 2

V = 0
for p in passes:

    missing_fields = all_fields.difference( set(p) )
    seems_V = ( len(missing_fields) == 0 ) or ( len(missing_fields) == 1 and "cid" in missing_fields )

    if seems_V:
        # If the pass seems valid, then need to check the fields further

        # birth-issue-expiration years must lie within their specified ranges
        byr_ok = int(p["byr"]) in range(1920, 2002 + 1)
        iyr_ok = int(p["iyr"]) in range(2010, 2020 + 1)
        eyr_ok = int(p["eyr"]) in range(2020, 2030 + 1)

        # height is given either in centimeters or in inches, each lying in a proper range
        hgt_ok = p["hgt"] in ([str(i) + "cm" for i in range(150, 193 + 1)] + [str(i) + "in" for i in range(59, 76 + 1)])

        # hair color: a # followed by exactly six characters 0-9 or a-f
        hcl_ok = ( len(p["hcl"]) == 7 and p["hcl"][0] == "#" )
        if hcl_ok:
            for c in p["hcl"]:
                if c not in (list(map(str, range(0, 10))) + list("abcdef") + ["#"]):
                    hcl_ok = False
                    break

        # eye color: exactly one of --- amber blue brown gray green hazel other
        ecl_ok = p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        # passport id: a nine-digit number, including leading zeroes
        pid_ok = (len(p["pid"]) == 9)
        if pid_ok:
            for c in p["pid"]:
                if int(c) not in list(range(0, 10)):
                    pid_ok = False
                    break

        # also the field cid is ignored

        # Iff all fields are OK, then it is a valid passport
        if byr_ok and iyr_ok and eyr_ok and hgt_ok and hcl_ok and ecl_ok and pid_ok:
            V += 1

print("Number of valid passes:", V)
