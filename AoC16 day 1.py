"The Document indicates that you should start at the given coordinates (where you just landed) and face North. \
Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, \
then walk forward the given number of blocks, ending at a new intersection."

#How many blocks away is Easter Bunny HQ?

#import csv
#with open('C:\Users\Diane\Desktop\Advent of code 2016\day 1 input.csv', 'rb') as f:
#    reader = csv.reader(f)
#    Game_input = list(reader)
array = ['R4', 'R5', 'L5', 'L5', 'L3','R2', 'R1', 'R1', 'L5', 'R5', 'R2', 'L1', 'L3', 'L4', 'R3', 'L1', 'L1', 'R2', 'R3', 'R3', 'R1', 'L3', 'L5', 'R3', 'R1', 'L1', 'R1', 'R2', 'L1', 'L4', 'L5', 'R4', 'R2', 'L192', 'R5', 'L2', 'R53', 'R1', 'L5', 'R73', 'R5', 'L5', 'R186', 'L3', 'L2', 'R1', 'R3', 'L3', 'L3', 'R1', 'L4', 'L2', 'R3', 'L5', 'R4', 'R3', 'R1', 'L1', 'R5', 'R2', 'R1', 'R1', 'R1', 'R3', 'R2', 'L1', 'R5', 'R1', 'L5', 'R2', 'L2', 'L4', 'R3', 'L1', 'R4', 'L5', 'R4', 'R3', 'L5', 'L3', 'R4', 'R2', 'L5', 'L5', 'R2', 'R3', 'R5', 'R4', 'R2', 'R1', 'L1', 'L5', 'L2', 'L3', 'L4', 'L5', 'L4', 'L5', 'L1', 'R3', 'R4', 'R5', 'R3', 'L5', 'L4', 'L3', 'L1', 'L4', 'R2', 'R5', 'R5', 'R4', 'L2', 'L4', 'R3', 'R1', 'L2', 'R5', 'L5', 'R1', 'R1', 'L1', 'L5', 'L5', 'L2', 'L1', 'R5', 'R2', 'L4', 'L1', 'R4', 'R3', 'L3', 'R1', 'R5', 'L1', 'L4', 'R2', 'L3', 'R5', 'R3', 'R1', 'L3']

import pandas
#import csv
#dirty_input = csv.reader(open("C:\Users\Diane\Desktop\Advent of code 2016\day 1 input.csv", "rb"), delimiter=",", quotechar='|')

#Game_input = []
#for row in dirty_input:
    #for value in enumerate(row):
 #   if row[0] == "":
    #    break
  #  Game_input.append(row[0])

#print Game_input



#for line in dirty_input.splitlines():
 #   Game_input.append(tuple(line.split(",")))

#print Game_input
#my_direction = "N"

def PLAY_GAME(input):
############### INITIALIZE
    my_direction = "N"
    turn_direction = ""
    x_cord = 0
    y_cord = 0
    location = [[0,0]]
    visited_x = 0
    visited_y = 0
    #final_distance = 0
########################
    x = 0
    while x < 143:
        turn_direction = str(input[x][0]) #checks turn direction
        #print turn_direction
        steps = int(input[x][1:])
        #print steps
        #change_direction(my_direction, turn_direction)
        if my_direction == "N":
            #print "I am facing North"
            if turn_direction == "R":
                #print "I need to turn Right"
                my_direction = "E"
                #print "I am now facing East"
            elif turn_direction == "L":
                #print "I need to turn Left"
                my_direction = "W"
                #return my_direction
        elif my_direction == "S":
            #print "I am facing South"
            if turn_direction == "R":
                my_direction = "W"
            elif turn_direction == "L":
                my_direction = "E"
        elif my_direction == "E":
            #print "I am facing East"
            if turn_direction == "R":
                my_direction = "S"
            elif turn_direction == "L":
                my_direction = "N"
        elif my_direction == "W":
            #print "I am facing West"
            if turn_direction == "R":
                my_direction = "N"
            elif turn_direction == "L":
                my_direction = "S"
        #print "My new direction is %s" % (my_direction)
        #print my_direction
        ########################### WALK
        #take_steps(my_direction, steps, x, y)
        if my_direction == "N":
            #######
            to_add = steps
            while to_add > 0:
                visited_y = visited_y + 1
                new_loc = [visited_x, visited_y]
                print new_loc
                if new_loc in location:
                    print "I have visited %s" %(new_loc)
                    return abs(visited_x) + abs(visited_y)
                    break
                else:
                    location.append(new_loc)
                to_add = to_add - 1
            #############
            y_cord = y_cord + steps
        elif my_direction == "S":
            #######
            to_add = steps
            while to_add > 0:
                visited_y = visited_y - 1
                new_loc = [visited_x, visited_y]
                print new_loc
                if new_loc in location:
                    print "I have visited %s" %(new_loc)
                    return abs(visited_x) + abs(visited_y)
                    break
                else:
                    location.append(new_loc)
                to_add = to_add - 1

            y_cord = y_cord - steps
        elif my_direction == "E":
            #######
            to_add = steps
            while to_add > 0:
                visited_x = visited_x + 1
                new_loc = [visited_x, visited_y]
                print new_loc
                if new_loc in location:
                    print "I have visited %s" %(new_loc)
                    return abs(visited_x) + abs(visited_y)
                    break
                else:
                    location.append(new_loc)
                to_add = to_add - 1

            x_cord = x_cord + steps
        elif my_direction == "W":
            #######
            to_add = steps
            while to_add > 0:
                visited_x = visited_x - 1
                new_loc = [visited_x, visited_y]
                print new_loc
                if new_loc in location:
                    print "I have visited %s" %(new_loc)
                    return abs(visited_x) + abs(visited_y)
                    break
                else:
                    location.append(new_loc)
                to_add = to_add - 1

            x_cord = x_cord - steps
        #print x_cord, y_cord
        #new_loc = [int(x_cord), int(y_cord)]
        #if new_loc in location:
        #    print location.index(new_loc)
        #    #return new_loc
        #    print abs(x_cord) + abs(y_cord)
        #    break
        #else:
        #    location.append(new_loc)
        #    print location
        x = x +1
        print x
    #print abs(x_cord) + abs(y_cord)
    #print final_distance

def change_direction(my_direction, turn_direction):
    if my_direction == "N":
        print "I am facing North"
        if turn_direction == "R":
            print "I need to turn Right"
            my_direction = "E"
            print "I am now facing East"
#
        elif turn_direction == "L":
            print "I need to turn Left"
            my_direction = "W"
            return my_direction
    elif my_direction == "S":
        print "I am facing South"
        if turn_direction == "R":
            my_direction = "W"
        elif turn_direction == "L":
            my_direction = "E"
    elif my_direction == "E":
        print "I am facing East"
        if turn_direction == "R":
            my_direction = "S"
        elif turn_direction == "L":
            my_direction = "N"
    elif my_direction == "W":
        print "I am facing West"
        if turn_direction == "R":
            my_direction = "N"
        elif turn_direction == "L":
            my_direction = "S"
    print "My new direction is %s" % (my_direction)

def take_steps(my_direction, steps, x_cord, y_cord):
    if my_direction == "N":
        y_cord = y_cord + steps
    elif my_direction =="S":
        y_cord = y_cord - steps
    elif my_direction == "E":
        x_cord = x_cord + steps
    elif my_direction == "W":
        x_cord = x_cord - steps
    return x_cord, y_cord

solution = PLAY_GAME(array)
print solution