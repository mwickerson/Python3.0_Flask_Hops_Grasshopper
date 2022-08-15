"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm

import math
import re

# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"

"""
import numpy as np
import scipy
import numpy.linalg
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib_inline
python 
import pandas as pd
import sklearn as skl
import sklearn.linear_model as linm
import sklearn.cluster as cluster
import sklearn.neighbors as nb
import sklearn.neural_network as MLP
import sklearn.tree
import sklearn.svm
import sklearn.ensemble
"""


"""
 _______      ___    ___ ________  _____ ______   ________  ___       _______   ________           ________  ________      
|\  ___ \    |\  \  /  /|\   __  \|\   _ \  _   \|\   __  \|\  \     |\  ___ \ |\   ____\         |\   __  \|\   ___  \    
\ \   __/|   \ \  \/  / | \  \|\  \ \  \\\__\ \  \ \  \|\  \ \  \    \ \   __/|\ \  \___|_        \ \  \|\  \ \  \\ \  \   
 \ \  \_|/__  \ \    / / \ \   __  \ \  \\|__| \  \ \   ____\ \  \    \ \  \_|/_\ \_____  \        \ \  \\\  \ \  \\ \  \  
  \ \  \_|\ \  /     \/   \ \  \ \  \ \  \    \ \  \ \  \___|\ \  \____\ \  \_|\ \|____|\  \        \ \  \\\  \ \  \\ \  \ 
   \ \_______\/  /\   \    \ \__\ \__\ \__\    \ \__\ \__\    \ \_______\ \_______\____\_\  \        \ \_______\ \__\\ \__\
    \|_______/__/ /\ __\    \|__|\|__|\|__|     \|__|\|__|     \|_______|\|_______|\_________\        \|_______|\|__| \|__|
             |__|/ \|__|                                                          \|_________|                             
                                                                                                                           
                                                                                                                           
 _____ ______   ________  ________   _______   _______   ___       ________                                                
|\   _ \  _   \|\   ____\|\   ___  \|\  ___ \ |\  ___ \ |\  \     |\   ____\                                               
\ \  \\\__\ \  \ \  \___|\ \  \\ \  \ \   __/|\ \   __/|\ \  \    \ \  \___|_                                              
 \ \  \\|__| \  \ \  \    \ \  \\ \  \ \  \_|/_\ \  \_|/_\ \  \    \ \_____  \                                             
  \ \  \    \ \  \ \  \____\ \  \\ \  \ \  \_|\ \ \  \_|\ \ \  \____\|____|\  \                                            
   \ \__\    \ \__\ \_______\ \__\\ \__\ \_______\ \_______\ \_______\____\_\  \                                           
    \|__|     \|__|\|_______|\|__| \|__|\|_______|\|_______|\|_______|\_________\                                          
                                                                     \|_________|   
"""

@hops.component(
    "/binmult",
    inputs=[hs.HopsNumber("A"), hs.HopsNumber("B")],
    outputs=[hs.HopsNumber("Multiply")],
)
def BinaryMultiply(a: float, b: float):
    return a * b


@hops.component(
    "/add",
    name="Add",
    nickname="Add",
    description="Add numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[hs.HopsNumber("Sum", "S", "A + B")]
)
def add(a: float, b: float):
    return a + b


@hops.component(
    "/pointat",
    name="PointAt",
    nickname="PtAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate")
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")]
)
def pointat(curve: rhino3dm.Curve, t=0.0):
    return curve.PointAt(t)


@hops.component(
    "/srf4pt",
    name="4Point Surface",
    nickname="Srf4Pt",
    description="Create ruled surface from four points",
    inputs=[
        hs.HopsPoint("Corner A", "A", "First corner"),
        hs.HopsPoint("Corner B", "B", "Second corner"),
        hs.HopsPoint("Corner C", "C", "Third corner"),
        hs.HopsPoint("Corner D", "D", "Fourth corner")
    ],
    outputs=[hs.HopsSurface("Surface", "S", "Resulting surface")]
)
def ruled_surface(a: rhino3dm.Point3d,
                  b: rhino3dm.Point3d,
                  c: rhino3dm.Point3d,
                  d: rhino3dm.Point3d):
    edge1 = rhino3dm.LineCurve(a, b)
    edge2 = rhino3dm.LineCurve(c, d)
    return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)


@hops.component(
    "/curve_end_points",
    name="EndPoints",
    nickname="EndPoints",
    description="Get curve start/end points",
    #icon="beamupUserObjects/icons/bmd_level.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate")
    ],
    outputs=[
        hs.HopsPoint("S"),
        hs.HopsPoint("E"),
        #hs.HopsNumber("EE", "EE", "test")
    ]
)
def end_points(curve: rhino3dm.Curve):
    start = curve.PointAt(0)
    end = curve.PointAt(1)
    return (end, start) #return (end, start, {"{0}": end.X, "{1}": start.X})

@hops.component(
    "/pointsat",
    name="PointsAt",
    nickname="PtsAt",
    description="Get points along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameters on Curve to evaluate", hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsPoint("P", "P", "Points on curve at t")
    ]
)
def pointsat(curve, t):
    points = [curve.PointAt(item) for item in t]
    return points

""".vscode\
@hops.component(
    "/multi_plot",
    name="Multiple plots",
    nickname="Multi_plot",
    description="Tries to plot multiple lists into one graph using Matplotlib",
    inputs=[
        hs.HopsNumber("Numbers", "N", "Datatree of numbers to plot", hs.HopsParamAccess.TREE),
        hs.HopsBoolean("Plot", "P", "Plot me")
    ],
    outputs=[]
)
def multi_plotter(datatree, show):
    if show:
        for elem in datatree.keys():
            plt.plot(range(len(datatree[elem])), datatree[elem])

        plt.show()
"""

@hops.component(
    "/test",
    name="test",
    description="test point",
    #icon="examples/pointat.png",
    inputs=[
        hs.HopsPoint("Points", "Point", "Points of the mesh",  access = hs.HopsParamAccess.LIST),
        hs.HopsInteger('Integer', "I",  access = hs.HopsParamAccess.LIST)
    ],
    outputs=[
        hs.HopsPoint("x", "x", "Points of the mesh",  access = hs.HopsParamAccess.LIST)
    ]
)
def test(p,i):
    x = p
    #print(i)
    return x

"""
 ___       __   ___  ________  ___  __    _______   ________  ________  ________  ________          
|\  \     |\  \|\  \|\   ____\|\  \|\  \ |\  ___ \ |\   __  \|\   ____\|\   __  \|\   ___  \        
\ \  \    \ \  \ \  \ \  \___|\ \  \/  /|\ \   __/|\ \  \|\  \ \  \___|\ \  \|\  \ \  \\ \  \       
 \ \  \  __\ \  \ \  \ \  \    \ \   ___  \ \  \_|/_\ \   _  _\ \_____  \ \  \\\  \ \  \\ \  \      
  \ \  \|\__\_\  \ \  \ \  \____\ \  \\ \  \ \  \_|\ \ \  \\  \\|____|\  \ \  \\\  \ \  \\ \  \     
   \ \____________\ \__\ \_______\ \__\\ \__\ \_______\ \__\\ _\ ____\_\  \ \_______\ \__\\ \__\    
    \|____________|\|__|\|_______|\|__| \|__|\|_______|\|__|\|__|\_________\|_______|\|__| \|__|    
                                                                \|_________|                        
                                                                                                    
                                                                                                    
 ________  _________  ___  ___  ________  ___  ________  ________                                   
|\   ____\|\___   ___\\  \|\  \|\   ___ \|\  \|\   __  \|\   ____\                                  
\ \  \___|\|___ \  \_\ \  \\\  \ \  \_|\ \ \  \ \  \|\  \ \  \___|_                                 
 \ \_____  \   \ \  \ \ \  \\\  \ \  \ \\ \ \  \ \  \\\  \ \_____  \                                
  \|____|\  \   \ \  \ \ \  \\\  \ \  \_\\ \ \  \ \  \\\  \|____|\  \                               
    ____\_\  \   \ \__\ \ \_______\ \_______\ \__\ \_______\____\_\  \                              
   |\_________\   \|__|  \|_______|\|_______|\|__|\|_______|\_________\                             
   \|_________|                                            \|_________|                             
                                                                                                    
                                                                                                    
 _______      ___    ___ ________  _____ ______   ________  ___       _______   ________            
|\  ___ \    |\  \  /  /|\   __  \|\   _ \  _   \|\   __  \|\  \     |\  ___ \ |\   ____\           
\ \   __/|   \ \  \/  / | \  \|\  \ \  \\\__\ \  \ \  \|\  \ \  \    \ \   __/|\ \  \___|_          
 \ \  \_|/__  \ \    / / \ \   __  \ \  \\|__| \  \ \   ____\ \  \    \ \  \_|/_\ \_____  \         
  \ \  \_|\ \  /     \/   \ \  \ \  \ \  \    \ \  \ \  \___|\ \  \____\ \  \_|\ \|____|\  \        
   \ \_______\/  /\   \    \ \__\ \__\ \__\    \ \__\ \__\    \ \_______\ \_______\____\_\  \       
    \|_______/__/ /\ __\    \|__|\|__|\|__|     \|__|\|__|     \|_______|\|_______|\_________\      
             |__|/ \|__|                                                          \|_________|     
"""
@hops.component(
    "/squares",
    inputs=[
        hs.HopsNumber("x"), hs.HopsNumber("y")
    ],
    outputs=[
        hs.HopsNumber("Squares")
    ],
)
def Squares(x: float, y: float):
    return x * x + y * y


@hops.component(
    "/squares2",
    inputs=[hs.HopsNumber("x")],
    outputs=[hs.HopsNumber("Squares")],
)
def Squares2(x: float):
    squares = []      
    for i in range(10):
        squares.append(i**x)  
    #after oneliner
    #print([i**y for i in range(10)])
    return squares

@hops.component(
    "/minus",
    name="Minus",
    nickname="Minus",
    description="Minus numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[hs.HopsNumber("Subtraction", "S", "A - B")]
)
def minus(a: float, b: float):
    return a - b


@hops.component(
    "/times",
    name="Times",
    nickname="Times",
    description="Times numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[hs.HopsNumber("Multiplication", "S", "A * B")]
)
def times(a: float, b: float):
    return a * b


@hops.component(
    "/calculator",
    name="Calculator",
    nickname="Calculator",
    description="Calculate numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[
        hs.HopsNumber("Addition", "A", "A + B"),
        hs.HopsNumber("Subtraction", "S", "A - B"),
        hs.HopsNumber("Multiplication", "M", "A * B"),
        hs.HopsNumber("Division", "D", "A / B")
    ]
)
def calculator(a: float, b: float):
    add1 = (a + b)
    minus1 = (a - b)
    times1 = (a * b)
    divide1 = (a / b)
    return (add1, minus1, times1, divide1)

@hops.component(
    "/advanced_calculator",
    name="AdvCalculator",
    nickname="AdvCalculator",
    description="Calculate advanced numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[
        hs.HopsNumber("DivideDown", "DD", "A // B"),
        hs.HopsNumber("Modulus", "Mod", "A % B"),
        hs.HopsNumber("Negative", "N", "A * (-1)"),
        hs.HopsNumber("CastInt", "CInt", "int(A)"),
        hs.HopsNumber("CastFloat", "CFloat", "float(A)"),
        hs.HopsNumber("Exponent", "Exp", "A ** B"),
    ]
)
def advanced_calculator(a: float, b: float):
    divide_down = (a // b)
    modulus = (a % b)
    negative = (a * (-1))
    cast_int = int(a)
    cast_float = float(a)
    exponent = (a ** b)
    return (divide_down, modulus, negative, cast_int, cast_float, exponent)

@hops.component(
    "/booleans",
    name="Booleans",
    nickname="Booleans",
    description="Calculate booleans with CPython",
    inputs=[
        hs.HopsBoolean("BoolA", "boolA", "First boolean"),
        hs.HopsBoolean("BoolB", "boolB", "Second boolean"),
    ],
    outputs=[
        hs.HopsBoolean("boolOut", "boolOut", "boolA == boolB"),
    ]
)
def booleans (a: float, b: float):
    equality = (a == b)
    return (equality)

@hops.component(
    "/advanced_booleans",
    name="advanced_booleans",
    nickname="advanced_booleans",
    description="Calculate advanced_booleans with CPython",
    inputs=[
        hs.HopsNumber("Num1", "num1", "first number"),
        hs.HopsNumber("Num2", "num2", "second number"),
    ],
    outputs=[
        hs.HopsBoolean("less", "less", "num1 < num2"),
        hs.HopsBoolean("greater", "greater", "num1 > num2"),
    ]
)
def advanced_booleans (a: float, b: float):
    less_than = (a < b)
    greater_than = (a > b)
    return (less_than, greater_than)

@hops.component(
    "/deadCode",
    name="deadCode",
    nickname="deadCode",
    description="Calculate deadCode with CPython",
    inputs=[
        hs.HopsString("A", "A", "string"),
    ],
    outputs=[
        hs.HopsString("out", "out", "checkDeadCode"),
        hs.HopsString("aOut", "aOut", "aOut"),
    ]
)
def deadCode (a: str):
    # if condition evaluates to False
    if a == (None or 0 or 0.0 or '' or [] or {} or set()):
        check = print("Dead Code") #Not Reached
    else:
        check = print("oh, yeah!")
    return (check, a)

"""
 ________  _________  ________  ___  ________   ________  ________      
|\   ____\|\___   ___\\   __  \|\  \|\   ___  \|\   ____\|\   ____\     
\ \  \___|\|___ \  \_\ \  \|\  \ \  \ \  \\ \  \ \  \___|\ \  \___|_    
 \ \_____  \   \ \  \ \ \   _  _\ \  \ \  \\ \  \ \  \  __\ \_____  \   
  \|____|\  \   \ \  \ \ \  \\  \\ \  \ \  \\ \  \ \  \|\  \|____|\  \  
    ____\_\  \   \ \__\ \ \__\\ _\\ \__\ \__\\ \__\ \_______\____\_\  \ 
   |\_________\   \|__|  \|__|\|__|\|__|\|__| \|__|\|_______|\_________\
   \|_________|                                             \|_________|
"""

@hops.component(
    "/strings",
    name="strings",
    nickname="strings",
    description="Work with strings with CPython",
    inputs=[
        hs.HopsString("A", "A", "First string"),
        hs.HopsString("B", "B", "Second string"),
    ],
    outputs=[
        hs.HopsString("      A\t\n   "),
        hs.HopsString("Concat", "Concat", "A + B"),
        hs.HopsString("Length", "Length", "len(A)"),
        hs.HopsString("Upper", "Upper", "A.upper()"),
        hs.HopsString("Lower", "Lower", "A.lower()"),
        hs.HopsString("Split", "Split", "A.split(' ')"),
        hs.HopsString("Join", "Join", "', '.join(A)"),
        hs.HopsString("Replace", "Replace", "A.replace('a', 'b')"),
        hs.HopsString("Strip", "Strip", "A.strip('a')"),
        hs.HopsString("Startswith", "Startswith", "A.startswith('Double')"),
        hs.HopsString("Endswith", "Endswith", "A.endswith('content')"),
        hs.HopsString("Find", "Find", "A.find('click')"),
        hs.HopsString("Count", "Count", "A.count('a')"),
        hs.HopsString("Index", "Index", "A.index('a')"),
    ]
)
def strings (a: str, b: str):
    print(a)
    print(b)
    print(a + b)
    print(len(a))
    print(a.upper())
    print(a.lower())
    print(a.split(' '))
    print(', '.join(a))
    print(a.replace('a', 'b'))
    print(a.strip('a'))
    print(a.startswith('Double'))
    print(a.endswith('content...'))
    print(a.find('click'))
    print(a.count('a'))
    print(a.index('a'))
    return (a, a + b, len(a), a.upper(), a.lower(), a.split(' '), ', '.join(a), a.replace('a', 'b'), a.strip('a'), a.startswith('Double'), a.endswith('content...'), a.find('click'), a.count('a'), a.index('a'))
    
"""
 ___       ___  ________  _________  ________      
|\  \     |\  \|\   ____\|\___   ___\\   ____\     
\ \  \    \ \  \ \  \___|\|___ \  \_\ \  \___|_    
 \ \  \    \ \  \ \_____  \   \ \  \ \ \_____  \   
  \ \  \____\ \  \|____|\  \   \ \  \ \|____|\  \  
   \ \_______\ \__\____\_\  \   \ \__\  ____\_\  \ 
    \|_______|\|__|\_________\   \|__| |\_________\
                  \|_________|         \|_________|
"""


@hops.component(
    "/kw_List2",
    name="kwList2",
    nickname="kwList2",
    description="Work with keywords and List with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "add num to list"),
        #hs.HopsNumber("num", "num", "add num to list", hs.HopsParamAccess.LIST),
        hs.HopsBoolean("bool", "bool", "add bool to list"),
        #hs.HopsString("str", "str", "add str to list"),
    ],
    outputs=[
        hs.HopsString("aList","aList", "aList")
    ]
)
def ky_List2(a: int, b: bool):
    aList = []
    aList.append(str(a))
    aList.append(str(b))
    #p = q = x
    #b = p is q # True
    #c = [23] is [23] # False
    return (aList)

@hops.component(
    "/append",
    name="append",
    nickname="append",
    description="Work with append with CPython",
    inputs=[
        hs.HopsNumber("numList", "numList", "start with numList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("num", "num", "add num to list"),
    ],
    outputs=[
        hs.HopsNumber("numList", "numList", "numList"),
    ]
)
def append(a: list, b: int):
    a.append(b)
    return (a)

@hops.component(
    "/remove",
    name="remove",
    nickname="remove",
    description="Work with remove with CPython",
    inputs=[
        hs.HopsNumber("numList", "numList", "start with numList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("removeNum", "removeNum", "remove removeNum from numList", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST)
    ]
)   
def remove(a, b):
    bList = a
    bList.remove(b)
    return bList

@hops.component(
    "/insert",
    name="insert",
    nickname="insert",
    description="Work with insert with CPython",
    inputs=[
        hs.HopsNumber("numList", "numList", "start with numList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("insertNum", "insertNum", "insert insertNum to numList", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("index", "index", "insert insertNum to numList at index", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST)
    ]
)
def insert(a, b, c):
    bList = a
    bList.insert(1, b) #insert index bug
    return bList    


@hops.component(
    "/sort",
    name="sort",
    nickname="sort",
    description="Work with sort with CPython",
    inputs=[
        hs.HopsNumber("numList", "numList", "start with numList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST)
    ]
)
def sort(a):
    bList = a
    bList.sort()
    return bList


@hops.component(
    "/reverse",
    name="reverse",
    nickname="reverse",
    description="Work with reverse with CPython",
    inputs=[
        hs.HopsNumber("numList", "numList", "start with numList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST)
    ]
)
def reverse(a):
    bList = a
    bList.reverse()
    return bList


@hops.component(
    "/index",
    name="index",
    nickname="index",
    description="Work with index with CPython",
    inputs=[
        hs.HopsNumber("numList", "numList", "start with numList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("index", "index", "get index from numList", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.ITEM)
    ]
)
def index(a, b):
    bList = a
    return bList[2] #index bug

"""
 ________  _________  ________  ________  ___  __    ________      
|\   ____\|\___   ___\\   __  \|\   ____\|\  \|\  \ |\   ____\     
\ \  \___|\|___ \  \_\ \  \|\  \ \  \___|\ \  \/  /|\ \  \___|_    
 \ \_____  \   \ \  \ \ \   __  \ \  \    \ \   ___  \ \_____  \   
  \|____|\  \   \ \  \ \ \  \ \  \ \  \____\ \  \\ \  \|____|\  \  
    ____\_\  \   \ \__\ \ \__\ \__\ \_______\ \__\\ \__\____\_\  \ 
   |\_________\   \|__|  \|__|\|__|\|_______|\|__| \|__|\_________\
   \|_________|                                        \|_________|
"""

@hops.component(
    "/pop",
    name="pop",
    nickname="pop",
    description="Work with pop with CPython",
    inputs=[
        hs.HopsNumber("numList", "numList", "start with numList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST)
    ]
)
def pop(a):
    bList = a
    bList.pop()
    return bList

"""
 ________  ________  ________   _________  ________  ________  ___          
|\   ____\|\   __  \|\   ___  \|\___   ___\\   __  \|\   __  \|\  \         
\ \  \___|\ \  \|\  \ \  \\ \  \|___ \  \_\ \  \|\  \ \  \|\  \ \  \        
 \ \  \    \ \  \\\  \ \  \\ \  \   \ \  \ \ \   _  _\ \  \\\  \ \  \       
  \ \  \____\ \  \\\  \ \  \\ \  \   \ \  \ \ \  \\  \\ \  \\\  \ \  \____  
   \ \_______\ \_______\ \__\\ \__\   \ \__\ \ \__\\ _\\ \_______\ \_______\
    \|_______|\|_______|\|__| \|__|    \|__|  \|__|\|__|\|_______|\|_______|
                                                                            
                                                                            
                                                                            
 ________ ___       ________  ___       __                                  
|\  _____\\  \     |\   __  \|\  \     |\  \                                
\ \  \__/\ \  \    \ \  \|\  \ \  \    \ \  \                               
  \ \  \_| \ \  \____\ \  \\\  \ \  \|\__\_\  \                             
   \ \__\   \ \_______\ \_______\ \____________\                            
    \|__|    \|_______|\|_______|\|____________|    
"""

@hops.component(
    "/forloop",
    name="forloop",
    nickname="forloop",
    description="Work with forloop with CPython",
    inputs=[
        hs.HopsNumber("numList", "numList", "start with numList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST)
    ]
)
def forloop(a):
    bList = []
    for i in a:
        bList.append(i)
    return bList

@hops.component(
    "/_digitSum",
    name="digitSum",
    nickname="digitSum",
    description="Work with digitSum with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def digitSum(a):
    b = 0
    for i in a:
        b += i
    return b

@hops.component(
    "/nested_If",
    name="nested_If",
    nickname="nestedIf",
    description="Work with nestedIf with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def nestedIf(a):
    b = 0
    if a[0] > 0:
        if a[1] > 0:
            b = a[0] + a[1]
            print("hello Wickerson") #used for debugging in terminal/CMD line
    return b


@hops.component(
    "/if-elif-else",
    name="ifElifElse",
    nickname="ifElifElse",
    description="Work with ifElifElse with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def ifElifElse(a):
    b = 0
    if a[0] > 0:
        b = a[0]
    elif a[1] > 0:
        b = a[1]
    else:
        b = a[2]
    return b


"""
 ___       ________  ________  ________  ________      
|\  \     |\   __  \|\   __  \|\   __  \|\   ____\     
\ \  \    \ \  \|\  \ \  \|\  \ \  \|\  \ \  \___|_    
 \ \  \    \ \  \\\  \ \  \\\  \ \   ____\ \_____  \   
  \ \  \____\ \  \\\  \ \  \\\  \ \  \___|\|____|\  \  
   \ \_______\ \_______\ \_______\ \__\     ____\_\  \ 
    \|_______|\|_______|\|_______|\|__|    |\_________\
                                           \|_________|
"""

@hops.component(
    "/while",
    name="while",
    nickname="while",
    description="Work with while with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def whileLoop(a):
    b = 0
    i = 0
    while i < len(a):
        b += a[i]
        i += 1
    return b

@hops.component(
    "/range",
    name="range",
    nickname="range",
    description="Work with range with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def rangeLoop(a):
    b = 0
    for i in range(len(a)):
        b += a[i]
    return b

@hops.component(
    "/while-count",
    name="whileCount",
    nickname="whileCount",
    description="Work with whileCount with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def whileCount(a):
    count = 0
    while count < len(a):
        count += 1
    return count

@hops.component(
    "/whilepop",
    nickname="whilePop",
    description="Work with whilePop with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def whilePop(a):
    "/while-pop",
    name="whilePop",
    b = 0
    while len(a) > 0:
        b += a.pop()
        print(a.pop()) #debug in python server
    return b

@hops.component(
    "/_while-break",
    name="whileBreak",
    nickname="whileBreak",
    description="Work with whileBreak with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("breakNum", "breakNum", "breakNum", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def whileBreak(a, breakNum):
    i = 0
    while i < breakNum:
        i += 1
        print(i) #debug in python server
        return i
    else: 
        print("No Break\n") #debug in python server
        return 777
    
    i = 0
    while i < breakNum:
        i += 0
        print(i) #debug in python server
        break
    else:
        print("No Break\n") #debug in python server
        return 777

@hops.component(
    "/continue", #buggy
    name="continue", #buggy
    nickname="continue",
    description="Work with continue with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("continueNum", "continueNum", "continueNum", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def continueLoop(a, continueNum):
    i = 0
    while i < continueNum:
        i += 1
        if i == continueNum:
            continue
        print(i)
        return i
    else:
        print("Not continued\n")
    return 777

@hops.component(
    "/sorted2",
    name="sorted",
    nickname="sorted",
    description="Work with sorted with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def sortedLoop(a):
    listOut = []
    for i in sorted(a):
        print(i, end=" ")
        listOut.append(i)
    return listOut
    #for i in sorted(set(a)):
        #print(i, end=" ")
    #return i

@hops.component(
    "/sorted_set2",
    name="sorted_set",
    nickname="sorted_set",
    description="Work with sorted_set with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def sorted_setLoop(a):
    #for i in sorted(a):
        #print(i, end=" ")
    #return i
    listOut = []
    for i in sorted(set(a)):
        print(i, end=" ")
        listOut.append(i)
    return listOut

@hops.component(
    "/_reversed",
    name="reversed",
    nickname="reversed",
    description="Work with reversed with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def reversedLoop(a):
    listOut = []
    for i in reversed(a):
        print(i, end=" ")
        listOut.append(i)
    return listOut


@hops.component(
    "/_rangeComponent",
    name="rangeComponent",
    nickname="rangeComponent",
    description="Work with rangeComponent with CPython",
    inputs=[
        hs.HopsInteger("start", "start", "start with num", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("end", "end", "end with num", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("step", "step", "step with num", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsInteger("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def rangeComponent(start, end, step):
    listOut = []
    for i in (range(start, end, step)):
        print(i)
        listOut.append(i)
    return listOut

@hops.component(
    "/reversed_rangeComponent",
    name="reversed_rangeComponent",
    nickname="reversed_rangeComponent",
    description="Work with reversed_rangeComponent with CPython",
    inputs=[
        hs.HopsInteger("start", "start", "start with num", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("end", "end", "end with num", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("step", "step", "step with num", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsInteger("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def reversed_rangeComponent(start, end, step):
    listOut = []
    for i in reversed(range(start, end, step)):
        print(i)
        listOut.append(i)
    return listOut

"""
 ___       ________  ________  ________  ___  ________   ________          _________  _______   ________  ___  ___         
|\  \     |\   __  \|\   __  \|\   __  \|\  \|\   ___  \|\   ____\        |\___   ___\\  ___ \ |\   ____\|\  \|\  \        
\ \  \    \ \  \|\  \ \  \|\  \ \  \|\  \ \  \ \  \\ \  \ \  \___|        \|___ \  \_\ \   __/|\ \  \___|\ \  \\\  \       
 \ \  \    \ \  \\\  \ \  \\\  \ \   ____\ \  \ \  \\ \  \ \  \  ___           \ \  \ \ \  \_|/_\ \  \    \ \   __  \      
  \ \  \____\ \  \\\  \ \  \\\  \ \  \___|\ \  \ \  \\ \  \ \  \|\  \           \ \  \ \ \  \_|\ \ \  \____\ \  \ \  \ ___ 
   \ \_______\ \_______\ \_______\ \__\    \ \__\ \__\\ \__\ \_______\           \ \__\ \ \_______\ \_______\ \__\ \__\\__\
    \|_______|\|_______|\|_______|\|__|     \|__|\|__| \|__|\|_______|            \|__|  \|_______|\|_______|\|__|\|__\|__|

"""


@hops.component(
    "/_enumerate", #what every panel does
    name="enumerate",
    nickname="enumerate",
    description="Work with enumerate with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def enumerateLoop(a):
    listOut = []
    for i, j in enumerate(a):
        print(i, j, end=" ")
        listOut.append(j)
    return listOut

@hops.component(
    "/zip", #what every panel does
    name="zip",
    nickname="zip",
    description="Work with zip with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("num2", "num2", "start with num2", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsString("b", "b", "b", access = hs.HopsParamAccess.ITEM)
    ]
)
def zipLoop(a, b):
    listOut = []
    for i, j in zip(a, b):
        print(i, j, end=" ")
        listOut.append(i)
        listOut.append(j)
    return listOut




"""
 _____ ______   ___  ________  ________  _______   ___       ___       ________  ________   _______   ________  ___  ___  ________      
|\   _ \  _   \|\  \|\   ____\|\   ____\|\  ___ \ |\  \     |\  \     |\   __  \|\   ___  \|\  ___ \ |\   __  \|\  \|\  \|\   ____\     
\ \  \\\__\ \  \ \  \ \  \___|\ \  \___|\ \   __/|\ \  \    \ \  \    \ \  \|\  \ \  \\ \  \ \   __/|\ \  \|\  \ \  \\\  \ \  \___|_    
 \ \  \\|__| \  \ \  \ \_____  \ \  \    \ \  \_|/_\ \  \    \ \  \    \ \   __  \ \  \\ \  \ \  \_|/_\ \  \\\  \ \  \\\  \ \_____  \   
  \ \  \    \ \  \ \  \|____|\  \ \  \____\ \  \_|\ \ \  \____\ \  \____\ \  \ \  \ \  \\ \  \ \  \_|\ \ \  \\\  \ \  \\\  \|____|\  \  
   \ \__\    \ \__\ \__\____\_\  \ \_______\ \_______\ \_______\ \_______\ \__\ \__\ \__\\ \__\ \_______\ \_______\ \_______\____\_\  \ 
    \|__|     \|__|\|__|\_________\|_______|\|_______|\|_______|\|_______|\|__|\|__|\|__| \|__|\|_______|\|_______|\|_______|\_________\
                       \|_________|                                                                                         \|_________|
"""

@hops.component(
    "/is_prime",
    name="is_prime",
    nickname="is_prime",
    description="Work with is_prime with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsBoolean("is_prime", "is_prime", "is_prime", access = hs.HopsParamAccess.ITEM)
    ]
)
def is_prime(a):
    b = a
    if b == 2 or b == 3:
        return True
    if b < 2 or b % 2 == 0:
        return False
    for i in range(3, int(b**0.5)+1, 2):
        if b % i == 0:
            return False
    return True

@hops.component(
    "/evenOdd",
    name="evenOdd",
    nickname="evenOdd",
    description="Work with evenOdd with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("evenOdd", "evenOdd", "evenOdd", access = hs.HopsParamAccess.ITEM)
    ]
) 
def evenOdd(a):
    b = a
    if b % 2 == 0:
        return "even"
    else:
        return "odd"


@hops.component(
    "/_swap",
    name="swap",
    nickname="swap",
    description="Work with swap with CPython",
    inputs=[
        hs.HopsInteger("numList", "numList", "start with numList", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("index1", "index1", "get index from numList", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("index2", "index2", "get index from numList", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsInteger("bList", "bList", "bList", access = hs.HopsParamAccess.LIST)
    ]
)   
def swap(a: int, index1: int, index2: int):
    bList = a
    bList[index1], bList[index2] = bList[index2], bList[index1]
    return bList


"""
 ___       ________  _____ ______   ________  ________  ________     
|\  \     |\   __  \|\   _ \  _   \|\   __  \|\   ___ \|\   __  \    
\ \  \    \ \  \|\  \ \  \\\__\ \  \ \  \|\ /\ \  \_|\ \ \  \|\  \   
 \ \  \    \ \   __  \ \  \\|__| \  \ \   __  \ \  \ \\ \ \   __  \  
  \ \  \____\ \  \ \  \ \  \    \ \  \ \  \|\  \ \  \_\\ \ \  \ \  \ 
   \ \_______\ \__\ \__\ \__\    \ \__\ \_______\ \_______\ \__\ \__\
    \|_______|\|__|\|__|\|__|     \|__|\|_______|\|_______|\|__|\|__|
"""

@hops.component(
    "/cube1",
    name="cube1",
    nickname="cube1",
    description="Work with cube1 with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("cube", "cube", "cube", access = hs.HopsParamAccess.ITEM)
    ]
)
def cube1(a):
    return a**3

@hops.component(
    "/power",
    name="power",
    nickname="power",
    description="Work with power with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("power", "power", "power", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("power", "power", "power", access = hs.HopsParamAccess.ITEM)
    ]
)   
def power(a, power):

    return a**power

@hops.component(
    "/_filter1",
    name="_filter",
    nickname="_filter",
    description="Work with _filter with CPython",
    inputs=[
        hs.HopsNumber("numList", "numList", "start with numList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("filteredList", "filteredList", "filteredList", access = hs.HopsParamAccess.LIST)
    ]
)
def _filter(a):
    filtered = []
    for i in a:
        if i % 2 == 0:
            filtered.append(i)
    return filtered

@hops.component(
    "/_map3",
    name="_map",
    nickname="map",
    description="Work with map with CPython",
    inputs=[
        hs.HopsNumber("numList", "numList", "start with numList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsBoolean("mappedList", "mappedList", "mappedList", access = hs.HopsParamAccess.LIST)
    ]
)
def _map(a):
    mapped = []
    for i in a:
        mapped = map(lambda x: x % 2 == 0, a)
    return list(mapped)

"""
 ________ ___  ________  ________  _________                                               
|\  _____\\  \|\   __  \|\   ____\|\___   ___\                                             
\ \  \__/\ \  \ \  \|\  \ \  \___|\|___ \  \_|                                             
 \ \   __\\ \  \ \   _  _\ \_____  \   \ \  \                                              
  \ \  \_| \ \  \ \  \\  \\|____|\  \   \ \  \                                             
   \ \__\   \ \__\ \__\\ _\ ____\_\  \   \ \__\                                            
    \|__|    \|__|\|__|\|__|\_________\   \|__|                                            
                           \|_________|                                                    
                                                                                           
                                                                                           
 ________  ___       ________  ________   ________                                         
|\   ____\|\  \     |\   __  \|\   ____\ |\   ____\                                        
\ \  \___|\ \  \    \ \  \|\  \ \  \___|_\ \  \___|_                                       
 \ \  \    \ \  \    \ \   __  \ \_____  \\ \_____  \                                      
  \ \  \____\ \  \____\ \  \ \  \|____|\  \\|____|\  \                                     
   \ \_______\ \_______\ \__\ \__\____\_\  \ ____\_\  \                                    
    \|_______|\|_______|\|__|\|__|\_________\\_________\                                   
                                 \|_________\|_________|                                   
                                                                                           
                                                                                           
 ________ ___  ___  ________   ________ _________  ___  ________  ________   ________      
|\  _____\\  \|\  \|\   ___  \|\   ____\\___   ___\\  \|\   __  \|\   ___  \|\   ____\     
\ \  \__/\ \  \\\  \ \  \\ \  \ \  \___\|___ \  \_\ \  \ \  \|\  \ \  \\ \  \ \  \___|_    
 \ \   __\\ \  \\\  \ \  \\ \  \ \  \       \ \  \ \ \  \ \  \\\  \ \  \\ \  \ \_____  \   
  \ \  \_| \ \  \\\  \ \  \\ \  \ \  \____   \ \  \ \ \  \ \  \\\  \ \  \\ \  \|____|\  \  
   \ \__\   \ \_______\ \__\\ \__\ \_______\  \ \__\ \ \__\ \_______\ \__\\ \__\____\_\  \ 
    \|__|    \|_______|\|__| \|__|\|_______|   \|__|  \|__|\|_______|\|__| \|__|\_________\
                                                                               \|_________|
"""

@hops.component(
    "/assignFuctionToVariable",
    name="assignFuctionToVariable",
    nickname="assignFuctionToVariable",
    description="Work with assignFuctionToVariable with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("cube", "cube", "cube", access = hs.HopsParamAccess.ITEM)
    ]
)
def assignFuctionToVariable(a):
    cube = lambda x: x**3
    return cube(a)  # return the value of the function


@hops.component(
    "/cubeIt",
    name="cubeIt",
    nickname="cubeIt",
    description="Work with cubeIt with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("cube", "cube", "cube", access = hs.HopsParamAccess.ITEM)
    ]
)
def cubeIt(a):
    cubeOut = assignFuctionToVariable(a)
    return cubeOut

@hops.component(
    "/_funcAsArg",
    name="funcAsArg",
    nickname="funcAsArg",
    description="Work with funcAsArg with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("cube", "cube", "cube", access = hs.HopsParamAccess.ITEM)
    ]
)   
def funcAsArg(func):
    funcOut = cubeIt(3)
    return funcOut

@hops.component(
    "/returnFunc5",
    name="returnFunc",
    nickname="returnFunc",
    description="Work with returnFunc with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("adder", "adder", "adder", access = hs.HopsParamAccess.ITEM)
    ]
)
def returnFunc(a):
    def create_adder(a):
        def adder(y):
            return a + y
        return adder
    add_15 = create_adder(15)
    return add_15(a)


"""
 ________  ___       ________  ________   ________  _______   ________      
|\   ____\|\  \     |\   __  \|\   ____\ |\   ____\|\  ___ \ |\   ____\     
\ \  \___|\ \  \    \ \  \|\  \ \  \___|_\ \  \___|\ \   __/|\ \  \___|_    
 \ \  \    \ \  \    \ \   __  \ \_____  \\ \_____  \ \  \_|/_\ \_____  \   
  \ \  \____\ \  \____\ \  \ \  \|____|\  \\|____|\  \ \  \_|\ \|____|\  \  
   \ \_______\ \_______\ \__\ \__\____\_\  \ ____\_\  \ \_______\____\_\  \ 
    \|_______|\|_______|\|__|\|__|\_________\\_________\|_______|\_________\
                                 \|_________\|_________|        \|_________|
                                                                            
                                                                            
 ________  ________   ________                                              
|\   __  \|\   ___  \|\   ___ \                                             
\ \  \|\  \ \  \\ \  \ \  \_|\ \                                            
 \ \   __  \ \  \\ \  \ \  \ \\ \                                           
  \ \  \ \  \ \  \\ \  \ \  \_\\ \                                          
   \ \__\ \__\ \__\\ \__\ \_______\                                         
    \|__|\|__|\|__| \|__|\|_______|                                         
                                                                            
                                                                            
                                                                            
 ________  ________        ___  _______   ________ _________  ________      
|\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\\   ____\     
\ \  \|\  \ \  \|\ /_     \ \  \ \   __/|\ \  \___\|___ \  \_\ \  \___|_    
 \ \  \\\  \ \   __  \  __ \ \  \ \  \_|/_\ \  \       \ \  \ \ \_____  \   
  \ \  \\\  \ \  \|\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \ \|____|\  \  
   \ \_______\ \_______\ \________\ \_______\ \_______\  \ \__\  ____\_\  \ 
    \|_______|\|_______|\|________|\|_______|\|_______|   \|__| |\_________\
                                                                \|_________|

"""

@hops.component(
    "/class",
    name="Class",
    nickname="Class",
    description="Work with Class with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("cube", "cube", "cube", access = hs.HopsParamAccess.ITEM)
    ]
)   
def class_component(a):
    class MyClass(object):
        def __init__(self, num):
            self.num = num
        def cube(self):
            return self.num**3
    my_class = MyClass(a)
    return my_class.cube()


@hops.component(
    "/classWithAttributes",
    name="ClassWithAttributes",
    nickname="ClassWithAttributes",
    description="Work with ClassWithAttributes with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("attr1Out", "attr1Out", "attr1Out", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("attr2Out", "attr2Out", "attr2Out", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("infoOut", "infoOut", "infoOut", access = hs.HopsParamAccess.ITEM),
    ]
)
def classWithAttributes(a):
    class MyClass(object):
        def __init__(self, num):
            self.num = num
        def attr1(self):
            return self.num**3
        def attr2(self):
            return self.num**2
        def info(self):
            return "num: {}".format(self.num)
    my_class = MyClass(a)
    return my_class.attr1(), my_class.attr2(), my_class.info()

@hops.component(
    "/class_calculator",
    name="ClassCalculator",
    nickname="ClassCalculator",
    description="Work with ClassCalculator with CPython",
    inputs=[
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num2", "num2", "start with num2", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("sum", "sum", "sum", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("diff", "diff", "diff", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("prod", "prod", "prod", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("quot", "quot", "quot", access = hs.HopsParamAccess.ITEM),
    ]
)
def class_calculator(a, b):
    class MyClass(object):
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2
        def sum(self):
            return self.num1 + self.num2
        def diff(self):
            return self.num1 - self.num2
        def prod(self):
            return self.num1 * self.num2
        def quot(self):
            return self.num1 / self.num2
    my_class = MyClass(a, b)
    return my_class.sum(), my_class.diff(), my_class.prod(), my_class.quot()


       
@hops.component(
    "/class_calculator_adv",
    name="ClassCalculatorAdv",
    nickname="ClassCalculatorAdv",
    description="Work with ClassCalculatorAdv with CPython",
    inputs=[
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num2", "num2", "start with num2", access = hs.HopsParamAccess.ITEM),
    ],      
    outputs=[
        hs.HopsNumber("mod", "mod", "mod", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("div", "div", "div", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("exp", "exp", "exp", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("pow", "pow", "pow", access = hs.HopsParamAccess.ITEM),
    ]
)
def class_calculator_adv(a, b):
    class MyClass(object):
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2
        def mod(self):
            return self.num1 % self.num2
        def div(self):
            return self.num1 / self.num2
        def exp(self):
            return self.num1 ** self.num2
        def pow(self):
            return self.num1 ** self.num2
    my_class = MyClass(a, b)
    return my_class.mod(), my_class.div(), my_class.exp(), my_class.pow()

@hops.component(
    "/class_calculator_trig",
    name="ClassCalculatorTrig",
    nickname="ClassCalculatorTrig",
    description="Work with ClassCalculatorTrig with CPython",
    inputs=[
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num2", "num2", "start with num2", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("sin", "sin", "sin", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("cos", "cos", "cos", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("tan", "tan", "tan", access = hs.HopsParamAccess.ITEM),   
    ]
)
def class_calculator_trig(a, b):
    class MyClass(object):
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2
        def sin(self):
            return math.sin(self.num1)
        def cos(self):
            return math.cos(self.num1)
        def tan(self):
            return math.tan(self.num1)
    my_class = MyClass(a, b)
    return my_class.sin(), my_class.cos(), my_class.tan()

@hops.component(
    "/class_calculator_trig_adv",
    name="ClassCalculatorTrigAdv",
    nickname="ClassCalculatorTrigAdv",
    description="Work with ClassCalculatorTrigAdv with CPython",
    inputs=[
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num2", "num2", "start with num2", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("asin", "asin", "asin", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("acos", "acos", "acos", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("atan", "atan", "atan", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("atan2", "atan2", "atan2", access = hs.HopsParamAccess.ITEM),
    ]
)
def class_calculator_trig_adv(a, b):
    class MyClass(object):
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2
        def asin(self):
            return math.asin(self.num1)
        def acos(self):
            return math.acos(self.num1)
        def atan(self):
            return math.atan(self.num1)
        def atan2(self):
            return math.atan2(self.num1, self.num2)
    my_class = MyClass(a, b)
    return my_class.asin(), my_class.acos(), my_class.atan(), my_class.atan2()


"""
 ________  ___       ________  ________   ________  _______   ________                  
|\   ____\|\  \     |\   __  \|\   ____\ |\   ____\|\  ___ \ |\   ____\                 
\ \  \___|\ \  \    \ \  \|\  \ \  \___|_\ \  \___|\ \   __/|\ \  \___|_                
 \ \  \    \ \  \    \ \   __  \ \_____  \\ \_____  \ \  \_|/_\ \_____  \               
  \ \  \____\ \  \____\ \  \ \  \|____|\  \\|____|\  \ \  \_|\ \|____|\  \              
   \ \_______\ \_______\ \__\ \__\____\_\  \ ____\_\  \ \_______\____\_\  \             
    \|_______|\|_______|\|__|\|__|\_________\\_________\|_______|\_________\            
                                 \|_________\|_________|        \|_________|            
                                                                                        
                                                                                        
 ________  ________  ___      ___ ________  ________   ________  _______   ________     
|\   __  \|\   ___ \|\  \    /  /|\   __  \|\   ___  \|\   ____\|\  ___ \ |\   ___ \    
\ \  \|\  \ \  \_|\ \ \  \  /  / | \  \|\  \ \  \\ \  \ \  \___|\ \   __/|\ \  \_|\ \   
 \ \   __  \ \  \ \\ \ \  \/  / / \ \   __  \ \  \\ \  \ \  \    \ \  \_|/_\ \  \ \\ \  
  \ \  \ \  \ \  \_\\ \ \    / /   \ \  \ \  \ \  \\ \  \ \  \____\ \  \_|\ \ \  \_\\ \ 
   \ \__\ \__\ \_______\ \__/ /     \ \__\ \__\ \__\\ \__\ \_______\ \_______\ \_______\
    \|__|\|__|\|_______|\|__|/       \|__|\|__|\|__| \|__|\|_______|\|_______|\|_______|

"""

# constructors
@hops.component(
    "/class_Addition",
    name="ClassAddition",
    nickname="ClassAddition",
    description="Work with ClassAddition with CPython",
    inputs=[
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num2", "num2", "start with num2", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("sum", "sum", "sum", access = hs.HopsParamAccess.ITEM),
        ],
)
def class_addition(a, b):
    class Addition:
        first = 0
        second = 0
        answer = 0
        def __init__(self, f, s):
            self.first = f
            self.second = s
        def display(self):
            print("First number: ", self.first)
            print("Second number: ", self.second)
            print("Sum: ", self.answer)
        def calculate(self):
            self.answer = self.first + self.second
            return self.answer
    obj = Addition(a, b)
    return obj.calculate()

    obj.calculate()
    obj.display()

    return obj.answer

#inheritance (string example nonsense)
@hops.component(
    "/Addition_inheritance",
    name="ClassAdditionInheritance",
    nickname="ClassAdditionInheritance",
    description="Work with ClassAdditionInheritance with CPython",
    inputs=[
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num2", "num2", "start with num2", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("sum", "sum", "sum", access = hs.HopsParamAccess.ITEM),
        ],
)
def addition_inheritance(a, b):
    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def display(self):
            print("Name: ", self.name)
            print("Age: ", self.age)    
    emp = Person("John", 36)    
    emp.display()

    class Emp(Person):
        def Print(self):
            print("Emp class called")
    Emp_details = Emp("Mayank", 37)
    Emp_details.display()
    Emp_details.Print()
    return Emp_details.age

@hops.component(
    "/single_inherit",
    name="SingleInheritance",
    nickname="SingleInheritance",
    description="Work with SingleInheritance with CPython",
    inputs=[
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num2", "num2", "start with num2", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("sum", "sum", "sum", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("product", "product", "product", access = hs.HopsParamAccess.ITEM),   

        ],
)
def single_inheritance(a, b):
    class Addition:
        def func1(self, a, b):
            return a + b
    class Multiplication(Addition):
        def func2(self, a, b):
            return a * b
    object = Multiplication()
    object.func1(a, b)
    object.func2(a, b)
    return object.func1(a, b), object.func2(a, b)


@hops.component(
    "/multiple_inherit",
    name="MultipleInheritance",
    nickname="MultipleInheritance",
    description="Work with MultipleInheritance with CPython",
    inputs=[    
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num2", "num2", "start with num2", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("sum", "sum", "sum", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("product", "product", "product", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("addAndProduct", "addAndProduct", "addAndProduct", access = hs.HopsParamAccess.ITEM),
        ],
)
def multiple_inherit(a, b):
    class Addition:
        def func1(self, a, b):
            return a + b
    class Multiplication:
        def func2(self, a, b):
            return a * b
    class AdditionAndMultiplication(Addition, Multiplication):
        def func3(self, a, b):
            return a + b * b
    object = AdditionAndMultiplication()
    object.func1(a, b)
    object.func2(a, b)
    object.func3(a, b)
    return object.func1(a, b), object.func2(a, b), object.func3(a, b)


@hops.component(
    "/multilevel",
    name="MultilevelInheritance",
    nickname="MultilevelInheritance",
    description="Work with MultilevelInheritance with CPython",
    inputs=[    
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num2", "num2", "start with num2", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("finalOut", "finalOut", "finalOut", access = hs.HopsParamAccess.ITEM),
        ],
) 
def multilevel_inherit(a, b):
    #base class
    class Addition:
        def __init__(self, a, b):
            self.a = a
            self.b = b
    # intermediate class
    class Multiplication(Addition):
        def __init__(self, a, b):
            self.a = a
            #invoking constructor of base class
            Addition.__init__(self, a, b)
    #Derived class's constructor
    class AdditionAndMultiplication(Multiplication):
        def __init__(self, c, a, b):
            self.c = c
            #invoking constructor of intermediate class
            Multiplication.__init__(self, a, b)
        def final_answer(self):
            return self.a + self.b * self.b

    #Driver code
    s1 = AdditionAndMultiplication(10, a, b)
    s1.final_answer()
    return s1.final_answer()

# Python program to demonstrate
# Hierarchical Inheritance
@hops.component(
    "/hierarchical",
    name="HierarchicalInheritance",
    nickname="HierarchicalInheritance",
    description="Work with HierarchicalInheritance with CPython",
    inputs=[
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num2", "num2", "start with num2", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("sum", "sum", "sum", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("product", "product", "product", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("addAndProduct", "addAndProduct", "addAndProduct", access = hs.HopsParamAccess.ITEM),
        ],
)
def hierarchical_inherit(a, b):
    #base class
    class Addition:
        def func1(self):
            return a + b
    # Derived class method 2
    class Multiplication(Addition):
        def func2(self):
            return a * b
    # Derived class method 3
    class AdditionAndMultiplication(Multiplication):
        def func3(self):
            return a + b * b
    # Driver code
    object1 = Multiplication()
    object2 = AdditionAndMultiplication()
    object1.func1()
    object1.func2()
    object2.func1()
    object2.func3()
    return object1.func1(), object1.func2(), object2.func3()


# Python program to demonstrate
# hybrid inheritance
@hops.component(
    "/hybrid",
    name="HybridInheritance",
    nickname="HybridInheritance",
    description="Work with HybridInheritance with CPython",
    inputs=[
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num2", "num2", "start with num2", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("sum", "sum", "sum", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("product", "product", "product", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("addAndProduct", "addAndProduct", "addAndProduct", access = hs.HopsParamAccess.ITEM),
        ],
)
def hybrid_inherit(a, b):
    #base class
    class Addition:
        def func1(self):
            return a + b
    # intermediate class
    class Multiplication(Addition):
        def func2(self):
            return a * b
    #Derived class's constructor
    class AdditionAndMultiplication(Multiplication):
        def func3(self):
            return a + b * b
    #Driver code
    object = AdditionAndMultiplication()
    object.func1()
    object.func2()
    return object.func1(), object.func2(), object.func3()

# Python program to demonstrate
# protected members
@hops.component(
    "/protected",
    name="ProtectedMembers",
    nickname="ProtectedMembers",
    description="Work with ProtectedMembers with CPython",
    inputs=[
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("sum", "sum", "sum", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("square", "square", "square", access = hs.HopsParamAccess.ITEM),
        ],
)
def protected_members(a):
    # creating a base class
    class Addition:
        def __init__(self, a):
            #protected member
            self._a = a
    # Creating object of derived class
    class Derived(Addition):
        def __init__(self, a):
            # Calling a constructor of base class
            Addition.__init__(self, a)
            # modifying protected variable:
            self._a = a * a
    object1 = Addition(a)
    object2 = Derived(a)
    return object1._a, object2._a

#Python program to demonstrate
# private members
@hops.component(
    "/private",
    name="PrivateMembers",
    nickname="PrivateMembers",
    description="Work with PrivateMembers with CPython",
    inputs=[
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("sum", "sum", "sum", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("square", "square", "square", access = hs.HopsParamAccess.ITEM),
        ],
)   
def private_members(a):
    # creating a base class
    class Addition:
        def __init__(self, a):
            self.a = a
            self.__c = a * a
    # Creating object of derived class
    class Derived(Addition):
        def __init__(self, a):
            Addition.__init__(self, a)
            self.__c = a * a
    object1 = Addition(a)
    return object1.a, object1.__c


# Python program to demonstrate
# in-built polymorphism functions
# len() being used for a string
@hops.component(
    "/polymorphism",
    name="Polymorphism",
    nickname="Polymorphism",
    description="Work with Polymorphism with CPython",
    inputs=[
        hs.HopsString("str1", "str1", "start with str1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("len", "len", "len", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("len2", "len2", "len2", access = hs.HopsParamAccess.ITEM),   
        ],
)
def polymorphism(str1, num1):
    # len() being used for a string
    return len(str1), len(num1)

# a simple Python function to demonstrate
# polymorphism add
@hops.component(
    "/polymorphism_add",
    name="PolymorphismAdd",
    nickname="PolymorphismAdd",
    description="Work with PolymorphismAdd with CPython",   
    inputs=[
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num2", "num2", "start with num2", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num3", "num3", "start with num3", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("sum", "sum", "sum", access = hs.HopsParamAccess.ITEM),
        ],
)
def polymorphism_add(num1, num2, num3 = 0):
    final = num1 + num2 + num3   
    return final

# polymorphism calculator
@hops.component(
    "/poly_calculator",
    name="PolymorphismCalculator",
    nickname="PolymorphismCalculator",
    description="Work with PolymorphismCalculator with CPython",
    inputs=[
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num2", "num2", "start with num2", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num3", "num3", "start with num3", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num4", "num4", "start with num4", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("sum", "sum", "sum", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("sum2", "sum2", "sum2", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("product", "product", "product", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("product2", "product2", "product2", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("division", "division", "division", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("division2", "division2", "division2", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("subtraction", "subtraction", "subtraction", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("subtraction2", "subtraction2", "subtraction2", access = hs.HopsParamAccess.ITEM),
        ],
)
def polymorphism_calculator(num1, num2, num3, num4):
    class Calc1():
        def addition(self, num1, num2):
            return num1 + num2
        def subtraction(self, num1, num2):
            return num1 - num2
        def multiplication(self, num1, num2):
            return num1 * num2
        def division(self, num1, num2):
            return num1 / num2
    class Calc2():
        def addition(self, num3, num4):
            return num3 + num4
        def subtraction(self, num3, num4):
            return num3 - num4
        def multiplication(self, num3, num4):
            return num3 * num4
        def division(self, num3, num4):
            return num3 / num4
    obj_calc1 = Calc1()
    obj_calc2 = Calc2()
    return obj_calc1.addition(num1, num2), obj_calc2.addition(num3, num4), obj_calc1.multiplication(num1, num2), obj_calc2.multiplication(num3, num4), obj_calc1.division(num1, num2), obj_calc2.division(num3, num4), obj_calc1.subtraction(num1, num2), obj_calc2.subtraction(num3, num4)

# method overriding
@hops.component(
    "/method_override",
    name="MethodOverride",
    nickname="MethodOverride",
    description="Work with MethodOverride with CPython",
    inputs=[
        hs.HopsNumber("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num2", "num2", "start with num2", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("num3", "num3", "start with num3", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("calc1_add1", "calc1_add1", "calc1_add1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("calc1_add2", "calc1_add2", "calc1_add2", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("calc2_add1", "calc2_add1", "calc2_add1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("calc2_add2", "calc2_add2", "calc2_add2", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("calc3_add1", "calc3_add1", "calc3_add1", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("calc3_add2", "calc3_add2", "calc3_add2", access = hs.HopsParamAccess.ITEM),
        ],
)
def method_override(num1, num2, num3):
    class Calc1():
        def addition1(self, num1, num2):
            return num1 + num2
        def addition2(self, num1, num2, num3):
            return num1 + num2 + num3
    class Calc2(Calc1):
        def addition2(self, num1, num2, num3):
            return num1 + num2 + num3 + 1
    class Calc3(Calc1):
        def addition2(self, num1, num2):
            return num1 + num2 + 1
    obj_calc1 = Calc1()
    obj_calc2 = Calc2()
    obj_calc3 = Calc3()
    return obj_calc1.addition1(num1, num2), obj_calc1.addition2(num1, num2, num3), obj_calc2.addition1(num1, num2), obj_calc2.addition2(num1, num2, num3), obj_calc3.addition1(num1, num2), obj_calc3.addition2(num1, num2) 

# Skip Polymorphism with a Function and object, save for later

# Skip Class or Static Variables in Python

# Skip Class Methon vs Static Method in Python

"""
 _______      ___    ___ ________  _______   ________  _________  ___  ________  ________      
|\  ___ \    |\  \  /  /|\   ____\|\  ___ \ |\   __  \|\___   ___\\  \|\   __  \|\   ___  \    
\ \   __/|   \ \  \/  / | \  \___|\ \   __/|\ \  \|\  \|___ \  \_\ \  \ \  \|\  \ \  \\ \  \   
 \ \  \_|/__  \ \    / / \ \  \    \ \  \_|/_\ \   ____\   \ \  \ \ \  \ \  \\\  \ \  \\ \  \  
  \ \  \_|\ \  /     \/   \ \  \____\ \  \_|\ \ \  \___|    \ \  \ \ \  \ \  \\\  \ \  \\ \  \ 
   \ \_______\/  /\   \    \ \_______\ \_______\ \__\        \ \__\ \ \__\ \_______\ \__\\ \__\
    \|_______/__/ /\ __\    \|_______|\|_______|\|__|         \|__|  \|__|\|_______|\|__| \|__|
             |__|/ \|__|                                                                       
                                                                                               
                                                                                               
 ___  ___  ________  ________   ________  ___       ___  ________   ________                   
|\  \|\  \|\   __  \|\   ___  \|\   ___ \|\  \     |\  \|\   ___  \|\   ____\                  
\ \  \\\  \ \  \|\  \ \  \\ \  \ \  \_|\ \ \  \    \ \  \ \  \\ \  \ \  \___|                  
 \ \   __  \ \   __  \ \  \\ \  \ \  \ \\ \ \  \    \ \  \ \  \\ \  \ \  \  ___                
  \ \  \ \  \ \  \ \  \ \  \\ \  \ \  \_\\ \ \  \____\ \  \ \  \\ \  \ \  \|\  \               
   \ \__\ \__\ \__\ \__\ \__\\ \__\ \_______\ \_______\ \__\ \__\\ \__\ \_______\              
    \|__|\|__|\|__|\|__|\|__| \|__|\|_______|\|_______|\|__|\|__| \|__|\|_______|                                                                                               
"""

@hops.component(
    "/_exception1",
    name="Exception",
    nickname="Exception",
    description="Work with Exception with CPython",
    inputs=[
        hs.HopsNumber("numList", "numList", "start with numList", access = hs.HopsParamAccess.LIST),
        hs.HopsInteger("num1", "num1", "start with num1", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("numList", "numList", "numList", access = hs.HopsParamAccess.LIST),
    ],
)
def exception(numList, num1):
    try:
        return numList[num1]
    except IndexError:
        return -1

# skip Specific Exception in Python
# skip Try with Else Clause in Python
# skip Finally Keyword in Python
# skip Raising Exceptions in Python

"""
 ________ ___  ___       _______                                                 
|\  _____\\  \|\  \     |\  ___ \                                                
\ \  \__/\ \  \ \  \    \ \   __/|                                               
 \ \   __\\ \  \ \  \    \ \  \_|/__                                             
  \ \  \_| \ \  \ \  \____\ \  \_|\ \                                            
   \ \__\   \ \__\ \_______\ \_______\                                           
    \|__|    \|__|\|_______|\|_______|                                           
                                                                                 
                                                                                 
                                                                                 
 ___  ___  ________  ________   ________  ___       ___  ________   ________     
|\  \|\  \|\   __  \|\   ___  \|\   ___ \|\  \     |\  \|\   ___  \|\   ____\    
\ \  \\\  \ \  \|\  \ \  \\ \  \ \  \_|\ \ \  \    \ \  \ \  \\ \  \ \  \___|    
 \ \   __  \ \   __  \ \  \\ \  \ \  \ \\ \ \  \    \ \  \ \  \\ \  \ \  \  ___  
  \ \  \ \  \ \  \ \  \ \  \\ \  \ \  \_\\ \ \  \____\ \  \ \  \\ \  \ \  \|\  \ 
   \ \__\ \__\ \__\ \__\ \__\\ \__\ \_______\ \_______\ \__\ \__\\ \__\ \_______\
    \|__|\|__|\|__|\|__|\|__| \|__|\|_______|\|_______|\|__|\|__| \|__|\|_______|                                                                                             
"""
@hops.component(
    "/read_file",
    name="Read File",
    nickname="Read File",
    description="Read File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def read_file(file_name):
    with open(file_name, "r") as f:
        return f.read()

@hops.component(
    "/_read_file2",
    name="Read File",
    nickname="Read File",
    description="Read File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)   
def read_file2(file_name):
    file = open(file_name, "r")
    for each in file:
        return each

@hops.component(
    "/write_file",
    name="Write File",
    nickname="Write File",
    description="Write File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("file_content", "file_content", "start with file_content", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def write_file(file_name, file_content):
    with open(file_name, "w") as f:
        f.write(file_content)
        return file_content

@hops.component(
    "/append_file",
    name="Append File",
    nickname="Append File",
    description="Append File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("file_content", "file_content", "start with file_content", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)   
def append_file(file_name, file_content):
    with open(file_name, "a") as f:
        f.write(file_content)
        return file_content

@hops.component(
    "/read_file_lines",
    name="Read File Lines",
    nickname="Read File Lines",
    description="Read File Lines with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],      
)
def read_file_lines(file_name):
    with open(file_name, "r") as f:
        return f.readlines()

# Python code to illustrate read() mode
@hops.component(
    "/read_file_read",
    name="Read File Read",
#    description="Read File Read with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("numChar", "numChar", "start with numChar", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def read_file_read(file_name, numChar):
    file = open(file_name, "r")
    return file.read(numChar)

# Creating a file using write() mode
@hops.component(
    "/create_file",
    name="Create File",
    nickname="Create File",
    description="Create File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("file_content", "file_content", "start with file_content", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def create_file(file_name, file_content):
    with open(file_name, "w") as f:
        f.write(file_content)
        return file_content
        f.close()


# Python code to illustrate append() mode
@hops.component(
    "/append_file_append",
    name="Append File Append",
    nickname="Append File Append",
    description="Append File Append with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("file_content", "file_content", "start with file_content", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def append_file_append(file_name, file_content):
    with open(file_name, "a") as f:
        f.write(file_content)
        return file_content
        f.close()

# with() methond closes the file automatically

# Pythoncode to illuatrate split() method
@hops.component(
    "/split_file",
    name="Split File",
    nickname="Split File",
    description="Split File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("file_content", "file_content", "start with file_content", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.LIST),
    ],
)
def split_file(file_name, file_content):
    with open(file_name, "r") as f:
        word = []
        data = f.readlines()
        for line in data:
            word.append(line.split())
        return word


# Opening a file
@hops.component(
    "/open_file",
    name="Open File",
    nickname="Open File",
    description="Open File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def open_file(file_name):
    with open(file_name, "r") as f:
        return f.read()


# Open file in append mode
@hops.component(
    "/open_file_append",
    name="Open File Append",
    nickname="Open File Append",
    description="Open File Append with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("file_content", "file_content", "start with file_content", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def open_file_append(file_name, file_content):
    with open(file_name, "a") as f:
        f.write(file_content)
        return file_content
        f.close()

# open file on desktop or anywhere on drive C: or D:
@hops.component(
    "/open_file_desktop",
    name="Open File Desktop",
    nickname="Open File Desktop",
    description="Open File Desktop with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def open_file_desktop(file_name):
    with open(file_name, "r") as f:
        return f.read()
    f.close()

# read, readlines, readline, write, append, split, close

# Python code to illustrate readlines() method
@hops.component(
    "/readlines_file",  
    name="Readlines File",
    nickname="Readlines File",
    description="Readlines File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.LIST),
    ],
)
def readlines_file(file_name):
    with open(file_name, "r") as f:
        return f.readlines()
    f.close()

@hops.component(
    "/readline_file",
    name="Readline File",
    nickname="Readline File",
    description="Readline File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def readline_file(file_name):
    with open(file_name, "r") as f:
        return f.readline()
    f.close()

@hops.component(
    "/write_file",
    name="Write File",
    nickname="Write File",
    description="Write File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("file_content", "file_content", "start with file_content", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def write_file(file_name, file_content):
    with open(file_name, "w") as f:
        f.write(file_content)
        return file_content
        f.close()

@hops.component(
    "/append_file",
    name="Append File",
    nickname="Append File",
    description="Append File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
        hs.HopsString("file_content", "file_content", "start with file_content", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def append_file(file_name, file_content):
    with open(file_name, "a") as f:
        f.write(file_content)
        return file_content
        f.close()

@hops.component(
    "/split_file",
    name="Split File",
    nickname="Split File",
    description="Split File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.LIST),
    ],
)
def split_file(file_name):
    with open(file_name, "r") as f:
        return f.split()
    f.close()

@hops.component(
    "/close_file",
    name="Close File",
    nickname="Close File",
    description="Close File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def close_file(file_name):
    with open(file_name, "r") as f:
        return f.close()
    f.close()

@hops.component(
    "/read_file",
    name="Read File",
    nickname="Read File",
    description="Read File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def read_file(file_name):
    with open(file_name, "r") as f:
        return f.read()
    f.close()

@hops.component(
    "/read_file_binary",
    name="Read File Binary",
    nickname="Read File Binary",
    description="Read File Binary with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def read_file_binary(file_name):
    with open(file_name, "rb") as f:
        return f.read()
    f.close()

@hops.component(
    "/read_file_binary_lines",
    name="Read File Binary Lines",
    nickname="Read File Binary Lines",
    description="Read File Binary Lines with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.LIST),
    ],
)
def read_file_binary_lines(file_name):
    with open(file_name, "rb") as f:
        return f.readlines()
    f.close()   

@hops.component(
    "/read_file_binary_line",
    name="Read File Binary Line",
    nickname="Read File Binary Line",
    description="Read File Binary Line with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def read_file_binary_line(file_name):
    with open(file_name, "rb") as f:
        return f.readline()
    f.close()

@hops.component(
    "/read_file_binary_lines_split",
    name="Read File Binary Lines Split",
    nickname="Read File Binary Lines Split",
    description="Read File Binary Lines Split with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.LIST),
    ],
)
def read_file_binary_lines_split(file_name):
    with open(file_name, "rb") as f:
        return f.readlines().split()
    f.close()

@hops.component(
    "/read_file_binary_line_split",
    name="Read File Binary Line Split",
    nickname="Read File Binary Line Split",
    description="Read File Binary Line Split with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.LIST),
    ],
)
def read_file_binary_line_split(file_name):
    with open(file_name, "rb") as f:
        return f.readline().split()
    f.close()

@hops.component(
    "/read_file_binary_lines_split_int",
    name="Read File Binary Lines Split Int",
    nickname="Read File Binary Lines Split Int",
    description="Read File Binary Lines Split Int with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.LIST),
    ],
)
def read_file_binary_lines_split_int(file_name):
    with open(file_name, "rb") as f:
        return [int(x) for x in f.readlines().split()]
    f.close()

# seek and tell
@hops.component(
    "/seek_file",
    name="Seek File",
    nickname="Seek File",
    description="Seek File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
        hs.HopsInteger("seek_position", "seek_position", "seek_position", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("file_content", "file_content", "file_content", access = hs.HopsParamAccess.ITEM),
    ],
)
def seek_file(file_name, seek_position):
    with open(file_name, "r") as f:
        f.seek(seek_position)
        return f.read()
    f.close()

@hops.component(
    "/tell_file",
    name="Tell File",
    nickname="Tell File",
    description="Tell File with Python",
    inputs=[
        hs.HopsString("file_name", "file_name", "start with file_name", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsInteger("file_position", "file_position", "file_position", access = hs.HopsParamAccess.ITEM),
    ],
)
def tell_file(file_name):
    with open(file_name, "r") as f:
        return f.tell()
    f.close()

"""
 _______    ______   _______  ________        ________  __       __   ______  
|       \  /      \ |       \|        \      |        \|  \  _  |  \ /      \ 
| $$$$$$$\|  $$$$$$\| $$$$$$$\\$$$$$$$$       \$$$$$$$$| $$ / \ | $$|  $$$$$$\
| $$__/ $$| $$__| $$| $$__| $$  | $$            | $$   | $$/  $\| $$| $$  | $$
| $$    $$| $$    $$| $$    $$  | $$            | $$   | $$  $$$\ $$| $$  | $$
| $$$$$$$ | $$$$$$$$| $$$$$$$\  | $$            | $$   | $$ $$\$$\$$| $$  | $$
| $$      | $$  | $$| $$  | $$  | $$            | $$   | $$$$  \$$$$| $$__/ $$
| $$      | $$  | $$| $$  | $$  | $$            | $$   | $$$    \$$$ \$$    $$
 \$$       \$$   \$$ \$$   \$$   \$$             \$$    \$$      \$$  \$$$$$$ 

"""

"""
 ________  _______   ________  ___  ___  ___       ________  ________                                               
|\   __  \|\  ___ \ |\   ____\|\  \|\  \|\  \     |\   __  \|\   __  \                                              
\ \  \|\  \ \   __/|\ \  \___|\ \  \\\  \ \  \    \ \  \|\  \ \  \|\  \                                             
 \ \   _  _\ \  \_|/_\ \  \  __\ \  \\\  \ \  \    \ \   __  \ \   _  _\                                            
  \ \  \\  \\ \  \_|\ \ \  \|\  \ \  \\\  \ \  \____\ \  \ \  \ \  \\  \|                                           
   \ \__\\ _\\ \_______\ \_______\ \_______\ \_______\ \__\ \__\ \__\\ _\                                           
    \|__|\|__|\|_______|\|_______|\|_______|\|_______|\|__|\|__|\|__|\|__|                                          
                                                                                                                    
                                                                                                                    
                                                                                                                    
 _______      ___    ___ ________  ________  _______   ________   ________  ___  ________  ________   ________      
|\  ___ \    |\  \  /  /|\   __  \|\   __  \|\  ___ \ |\   ____\ |\   ____\|\  \|\   __  \|\   ___  \|\   ____\     
\ \   __/|   \ \  \/  / | \  \|\  \ \  \|\  \ \   __/|\ \  \___|_\ \  \___|\ \  \ \  \|\  \ \  \\ \  \ \  \___|_    
 \ \  \_|/__  \ \    / / \ \   ____\ \   _  _\ \  \_|/_\ \_____  \\ \_____  \ \  \ \  \\\  \ \  \\ \  \ \_____  \   
  \ \  \_|\ \  /     \/   \ \  \___|\ \  \\  \\ \  \_|\ \|____|\  \\|____|\  \ \  \ \  \\\  \ \  \\ \  \|____|\  \  
   \ \_______\/  /\   \    \ \__\    \ \__\\ _\\ \_______\____\_\  \ ____\_\  \ \__\ \_______\ \__\\ \__\____\_\  \ 
    \|_______/__/ /\ __\    \|__|     \|__|\|__|\|_______|\_________\\_________\|__|\|_______|\|__| \|__|\_________\
             |__|/ \|__|                                 \|_________\|_________|                        \|_________|

"""
@hops.component(
    "/_findall",
    name="Find All",
    nickname="FindAll",
    description="Find all matches",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("String", "S", "String to search"),
        hs.HopsString("Pattern", "P", "Pattern to search for"),
    ],
    outputs=[
        hs.HopsString("Matches", "M", "All matches"),
    ],
)
def _findall(string, pattern):
    return re.findall(pattern, string)


# match start end and return the match
@hops.component(
    "/_match1",
    name="Match",
    nickname="Match",
    description="Match start end and return the match",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("String", "S", "String to search"),
        hs.HopsString("Pattern", "P", "Pattern to search for"),
    ],
    outputs=[
        hs.HopsString("Match", "M", "Match"),
    ],
)
def _match(string, pattern):
    match = re.search(pattern, string)
    if match:
        return match.group(0)
    else:
        return "bugger all!"

# match start






if __name__ == "__main__":
    app.run(debug=True)

    