# This is a collab between Eric Wilson and Ian Scheffler

import random


def create_plane(rows,cols):
    """

    returns a new plane of size rowsxcols

    A plane is represented by a list of lists.

    This routine marks the empty window seats as "win" and other empties as "avail"
    """
    plane = []
    for r in range(rows):
        s = ["win"]+["avail"]*(cols-2)+["win"]
        plane.append(s)
    return plane

def get_number_economy_sold(economy_sold):
    # how can we use this dictionary to keep families/groups together?
    """
    Input: a dicitonary containing the number of regular economy seats sold.
           the keys are the names for the tickets and the values are how many

    ex:   {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3 seats, the Lee family 2

    Returns: the total number of seats sold
    """
    sold = 0
    for v in economy_sold.values():
        sold = sold + v
    return sold


def get_avail_seats(plane,economy_sold):
    """
    Parameters: plane : a list of lists representing plane
                economy_sold : a dictionary of the economy seats sold but not necessarily assigned

    Returns: the number of unsold seats

    Notes: this loops over the plane and counts the number of seats that are "avail" or "win"
           and removes the number of economy_sold seats
    """
    avail = 0;
    for r in plane:
        for c in r:
            if c == "avail" or c == "win":
                avail = avail + 1
    avail = avail - get_number_economy_sold(economy_sold)
    return avail

def get_total_seats(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane
    """
    return len(plane)*len(plane[0])

def get_plane_string(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing.
    """
    s = ""
    for r in plane:
        r = ["%14s"%x for x in r] # This is a list comprehension - an advanced Python feature
        s = s + " ".join(r)
        s = s + "\n"
    return s


def purchase_economy_plus(plane,economy_sold,name):
    """
    Params: plane - a list of lists representing a plane
            economy_sold - a dictionary representing the economy sold but not assigned
            name - the name of the person purchasing the seat
    """
    rows = len(plane)
    cols = len(plane[0])


    # total unassigned seats
    seats = get_avail_seats(plane,economy_sold)

    # exit if we have no more seats
    if seats < 1:
        return plane


    # 70% chance that the customer tries to purchase a window seat
    # it this by making a list of all the rows, randomizing it
    # and then trying each row to try to grab a seat


    if random.randrange(100) > 30:
        # make a list of all the rows using a list comprehension
        order = [x for x in range(rows)]

        # randomzie it
        random.shuffle(order)

        # go through the randomized list to see if there's an available seat
        # and if there is, assign it and return the new plane
        for row in order:
            if plane[row][0] == "win":
                plane[row][0] = name
                return plane
            elif plane[row][len(plane[0])-1] == "win":
                plane[row][len(plane[0])-1] = name
                return  plane

    # if no window was available, just keep trying a random seat until we find an
    # available one, then assign it and return the new plane
    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True
    return plane


# THIS WILL BE LEFT EMPTY FOR THE FIRST STAGE OF THE PROJECT
def seat_economy(plane,economy_sold,name):
    """
    This is mostly the same as the purchase_economy_plus routine but
    just does the random assignment.

    We use this when we're ready to assign the economy seats after most
    of the economy plus seats are sold

    THIS IS WHAT WE NEED TO CHANGE IF WE DON'T WANT ECONOMY SEATED RANDOMLY

    ideas: add an if statement sort of like with economy plus to model
    seating in groups; use a list comprehension to make a list (like order above)
    but don't randomize, maybe order by largest number of available seats?

    We might also want to order our dictionary of economy sold, so that we can
    have a decreasing list (biggest to smallest) of seat blocks by family size
    and then match family blocks with available blocks of seats.

    WHAT I THINK WE NEED TO DO:


    """
    rows = len(plane)
    cols = len(plane[0])

    # get the value for the key 'name' i.e., the number of seats bought by that party
    requested_number_of_seats = economy_sold.get(name)
    # print("name: " + name + " | " + "requested_number_of_seats: " + requested_number_of_seats)

    # make a list of all the rows using a list comprehension
    order = [x for x in range(rows)]

    # should we order it so that the order goes from most empty seats to least?
    # what would that look like? don't we want to sort it in terms of how many empty seats there are?

    # go through the randomized list to see if there's an available seat
    # and if there is, assign it and return the new plane

    # the above is what's old--what we need to do is somehow match the values in the dictionary
    # to see if the number of values equals the number of avails, then rename those seats
    # using the input name
    # since the name is an input of the function, can we get the value from the dictionary?
    # so are we just testing ONE name--i.e., check the value associated with the name,
    # then see when the value matches the number of avail in the row, replace all
    # the available seats with that name?

    # note: can use the .get method to get the value for the key "name"
    for row in order:
        if plane[row][1] == "avail" and plane[row][2] == "avail" and plane[row][3] == "avail" and requested_number_of_seats == 3: # this if statement will check if it's avail; we also need to make the conditional
            plane[row][1] = name
            plane[row][2] = name
            plane[row][3] = name
            return plane
        elif (plane[row][1] == "avail" and plane[row][2] == "avail") and requested_number_of_seats == 2: # this if statement will check if it's avail; we also need to make the conditional
            plane[row][1] = name
            plane[row][2] = name
            return plane
        elif (plane[row][2] == "avail" and plane[row][3] == "avail") and requested_number_of_seats == 2: # this if statement will check if it's avail; we also need to make the conditional
            plane[row][2] = name
            plane[row][3] = name
            return plane

    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True
    return plane


def purchase_economy_block(plane,economy_sold,number,name):
    # where does number of economy_sold come from? is it random?
    # this is purchasing BLOCkS of seats
    # in other words this is ADDING to the dictionary
    # This function CREATES blocks of seats for families in the dictionary
    """
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary

    """
    seats_avail = get_total_seats(plane)
    seats_avail = seats_avail - get_number_economy_sold(economy_sold)
    #what does this do below?
    if seats_avail >= number: # checks to see if there are enough seats to purchase the block
        economy_sold[name]=number # if there are enough seats, then we
    return economy_sold


def fill_plane(plane):
    """
    Params: plane - a list of lists representing a plane

    comments interspersed in the code

    """


    economy_sold={} #creates the dictionary economy sold - when and how is it filled?
    total_seats = get_total_seats(plane)



    # these are for naming the pasengers and families by
    # appending a number to either "ep" for economy plus or "u" for unassigned economy seat
    ep_number=1 #the word "number" gets replaced by actual numerals below; this is just a template
    u_number=1 #the word "number" gets replaced by actual numerals below; this is just a template

    # MODIFY THIS
    # you will probably want to change parts of this
    # for example, when to stop purchases, the probabilities, maybe the size for the random
    # regular economy size

    max_family_size = 3
    while total_seats > 0: # should this be > 0? Wouldn't this leave one empty seat?
        r = random.randrange(100)
        print("TOTAL SEATS: " + str(total_seats))
        print(" ")
        if r > 30:
            print("r=" + str(r) + ": purchase_economy_plus; economy_sold: " + str(economy_sold) + "; ep_" + str(ep_number))
            plane = purchase_economy_plus(plane,economy_sold,"ep-%d"%ep_number)
            ep_number = ep_number + 1
            total_seats = get_avail_seats(plane,economy_sold)
        else:
            print("r=" + str(r) + ": purchase_economy_block; economy_sold: " + str(economy_sold) + "; u_" + str(u_number))
            economy_sold = purchase_economy_block(plane,economy_sold,1+random.randrange(max_family_size),"u-%d"%u_number)
            u_number = u_number + 1
            print(get_plane_string(plane))
        print(" ")


    # once the plane reaches a certian seating capacity, assign
    # seats to the economy plus passengers
    # you will have to complete the seat_economy function
    # Alternatively you can rewrite this section
    for name in economy_sold.keys():
        # for i in range(economy_sold[name]): # once we modify economy plus, we can probably modify this line
        plane = seat_economy(plane,economy_sold,name)


    return plane



def main():
    plane = create_plane(10,5)
    plane = fill_plane(plane)
    print(get_plane_string(plane))
if __name__=="__main__":
    main()
