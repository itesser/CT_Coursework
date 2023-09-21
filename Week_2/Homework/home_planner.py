from math import pi

def home_sqfts(r=6):
    '''
    To help calculate the square footage of a home

    Starting Input: number of rooms
    User Inputs: lenght and width of each room 
    (**numbers only**)(**unit-of-measure agnostic**)

    Output: total sq footage


    '''
    area = []
    for i in range(r):
        l = float(input(f"How long is room {i+1}? "))
        w = float(input(f"How wide is room {i+1}? "))
        area.append(round(l*w, 2))
    return sum(area)


def hole_measure(n, radius = True):
    '''
    Given a radius OR diameter (see second argument), calculates the circumfrence of a circle
    Input: n = numerical value of known measurement
        radius = True -> calculates with n as radius
        raduis = False -> calculates with n as diameter
    Output: circumfrence of the circle, rounded to 3 decimal points
    ** unit-of-measure agnostic**
    '''
    if radius == True:
        return round(2*n*pi,3)
    else:
        return round(n*pi, 3)
    

def dodecameter(f):
    '''
    input: a number
    output: a larger number 
    '''
    return f*12