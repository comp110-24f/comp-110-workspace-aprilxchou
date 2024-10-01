"""Import a function from a different file"""

__author__ = "730754347"

from CQs.cq04.concatenation import concat
x:str = "123"
y:str = "abc"

print(concat(x,y))

from CQs.cq04.coordinates import get_coords

get_coords(x,y)