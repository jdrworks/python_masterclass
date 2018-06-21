ip = input("Please enter an IP Address ")
segments = 1;
length = 0

for char in ip:
    if char == '.':
        print("Segment {0} is {1} numbers long".format(segments, length))
        length = 0
        segments += 1
    else:
        length += 1

if char != '.':
    print("Segment {0} is {1} numbers long".format(segments, length))
print("There are {} segments".format(segments))
