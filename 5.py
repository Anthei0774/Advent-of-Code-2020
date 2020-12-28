# Preprocesing

input = open("5.txt").read()
input = input.split("\n")
for i in range(len(input)):
    input[i] = input[i].replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    input[i] = [ int(input[i][:7], 2), int(input[i][7:], 2) ]
    input[i] = input[i][0] * 8 + input[i][1]

###################################################################################################

# Part 1
print("Max seat number:", max(input))

###################################################################################################

# Part 2

for n in sorted(input):
    if n + 1 not in input:
        print("My seat number:", n + 1)
        break
