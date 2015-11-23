from __future__ import division
import math 

def center(vals):
    return [val/2 for val in vals]
 

def ray(p, m, b, x_0=None):
    """add ray to figure p with formula y = mx + b
       assumes scale of x axis is same as scale of y axis """
    if x_0 is None:
        x_0 = p.x_range.start
    y = m * x_0 + b 
    print a, b
    print math.tan(a), math.tan(b)
    p.ray(x=[x_0], y=[y], length=0, angle=math.atan2(1,m), line_color="red", line_width=2)