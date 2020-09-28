def get_file_lines(filename):
    #return a list of strings containing the lines of the file.
    file = open(filename, "r")
    print(file.read())
get_file_lines("Poem.txt") 
def lines_printed_backwards(lines_list):
    #print the lines of the poem in reverse. Include the original line number at the beginning of each line.
    pass

def lines_printed_random(lines_list):
    #print the lines of your poem in randomly order. Repeats are ok, but make sure the number of lines printed is equal to the original lines in the poem (Line numbers do not need to be printed.) Hint: try using a loop and randint() from the random module
    pass

def lines_printed_custom(lines_list):
    # should print the poem in a unique way, be creative!
    #carefully comment your custom function so it’s clear what it does.
    pass

####Stretch########
#Modify your program to write your poems to a file.
#Modify your program to have a menu that the user can select from rather than printing all the options at once
#Modify your program to read the poem from user input
#Modify your program to randomly rearrange the words on each line