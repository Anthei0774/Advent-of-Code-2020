input = open(main_folder + "3.txt").read()
input = input.split("\n")

trees_hit = 0
j = 0
for i in range(len(input)):

    if len(input[i]) <= j:
        j = j % len(input[i])

    if input[i][j] == "#":
        trees_hit += 1
    
    j += 3

print("Trees hit:", trees_hit)

###################################################################################################

steps = [ {"r" : 1, "d" : 1}, {"r" : 3, "d" : 1}, {"r" : 5, "d" : 1}, {"r" : 7, "d" : 1}, {"r" : 1, "d" : 2} ]

product = 1
for step in steps:

    j = 0
    trees_hit = 0
    for i in range(0, len(input), step["d"]):

        if len(input[i]) <= j:
            j = j % len(input[i])

        if input[i][j] == "#":
            trees_hit += 1

        j += step["r"]

    product *= trees_hit

print("Trajectories trees-hit-product:", product)
