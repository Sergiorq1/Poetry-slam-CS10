import random
def get_file_lines(filename):
    #return a list of strings containing the lines of the file.
    file = open(filename, "r")
    return (file.readlines())

def lines_printed_backwards(lines_list):
    #print the lines of the poem in reverse. Include the original line number at the beginning of each line.
    ####I saw this reverse strategy in stack overflow#####
    print("***THIS IS THE POEM BACKWARDS***")
    lines_list = lines_list[::-1]
    for (index, item) in enumerate(lines_list):
        index = len(lines_list) - index
        print(index, item)

# lines_printed_backwards(get_file_lines("Poem.txt"))

def lines_printed_random(lines_list):
    #print the lines of your poem in randomly order. Repeats are ok, but make sure the number of lines printed is equal to the original lines in the poem (Line numbers do not need to be printed.) Hint: try using a loop and randint() from the random module
    print("***THIS IS THE POEM IN RANDOM ORDER***")
    random.shuffle(lines_list)
    for i in lines_list:
        print(i)
# lines_printed_random(get_file_lines("Poem.txt"))
def lines_printed_custom(lines_list):
    # should print the poem in a unique way, be creative!
    #carefully comment your custom function so it’s clear what it does.
    while True:
        is_sorted = True
        for index in range(len(arr)-1):
# lines_printed_custom(get_file_lines("Poem.txt"))




def sorter(arr):
    while True:
        is_sorted = True 
        for index in range(len(arr) - 1):
            if arr[index] > arr[index + 1]:
                is_sorted = False
                (arr[index], arr[index + 1]) = (arr[index + 1], arr[index])

        if is_sorted == True:
            return arr
            
print(sorter(get_file_lines("Poem.txt")))
