# PART 1

input = open("2.txt").read()
input = input.split("\n")

for i in range(len(input)):
    line = input[i].split(" ")
    v_range = line[0].split("-")
    v_range = list(map(int, v_range))
    input[i] = [v_range[0], v_range[1], line[1][0], line[2]]

C = 0
for i in range(len(input)):

    char = input[i][2]
    text = input[i][3]

    # Password is valid, when the number of occurences of the character is in the range
    c = text.count(char)
    if input[i][0] <= c and c <= input[i][1]:
        C += 1

print("Valid passwords count:", C)

###################################################################################################

# PART 2

C = 0
for i in range(len(input)):

    # Must subtract 1, so indexing is proper
    input[i][0] -= 1
    input[i][1] -= 1
    char = input[i][2]
    text = input[i][3]

    # Valid character is present in text, but not in both positions
    if text[ input[i][0] ] == char or text[ input[i][1] ] == char:
        if not (text[ input[i][0] ] == char and text[ input[i][1] ] == char):
            C += 1

print("Valid passwords count:", C)
