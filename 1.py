input = open(main_folder + "1.txt").read()
input = input.split("\n")
input = list(map(int, input))

# Iterate through the input without repeating the same pair
I, J = -1, -1
for i in range(len(input)):
    for j in range(i + 1, len(input)):
        if input[i] + input[j] == 2020:
            I, J = i, j

print("Product:", input[I] * input[J])

###################################################################################################

# The same idea as before
I, J, K = -1, -1, -1
for i in range(len(input)):
    for j in range(i + 1, len(input)):
        for k in range(j + 1, len(input)):
            if input[i] + input[j] + input[k] == 2020:
                I, J, K = i, j, k

print("Product:", input[I] * input[J] * input[K])
