# Part 1

# Preprocessing
input = open(main_folder + "3.txt").read()
input = input.replace(".", "0")
input = input.replace("#", "1")
input = input.split("\n")
for i in range(len(input)):
    input[i] = list(input[i])
    input[i] = list(map(int, input[i]))

T = 0

# One loop is enough for a trajectory
j = 0
for i in range(len(input)):

    # Forest-pattern repeats horizontally
    if len(input[i]) <= j:
        j = j % len(input[i])

    T += input[i][j]
    j += 3

print("Trees hit:", T)

###################################################################################################

# Part 2

# Trajectories
steps = [ {"R" : 1, "D" : 1},
          {"R" : 3, "D" : 1},
          {"R" : 5, "D" : 1},
          {"R" : 7, "D" : 1},
          {"R" : 1, "D" : 2} ]

# Init product and iterating through the planned trajectories
P = 1
for step in steps:

    # Same process as in Part 1
    j = 0
    T = 0
    for i in range(0, len(input), step["D"]):

        if len(input[i]) <= j:
            j = j % len(input[i])

        T += input[i][j]
        j += step["R"]

    # Product is multiplied with current-trees-hit result
    P *= T
    print("Trees hit with step", step, ":", T)

print("Trajectories trees-hit-product:", P)
