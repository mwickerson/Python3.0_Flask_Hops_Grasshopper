"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm


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

# annonymous function
@hops.component(
    "/cube",
    name="cube",
    nickname="cube",
    description="Work with cube with CPython",
    inputs=[
        hs.HopsNumber("num", "num", "start with num", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("cube", "cube", "cube", access = hs.HopsParamAccess.ITEM),
        hs.HopsNumber("cube_v2", "cube_v2", "cube_v2", access = hs.HopsParamAccess.ITEM)
    ]
)
def cube(x):
    cube_v2 = lambda x: x*x*x
    return cube_v2


"""
 ________  _______  _________  ________      
|\   ____\|\  ___ \|\___   ___\\   ____\     
\ \  \___|\ \   __/\|___ \  \_\ \  \___|_    
 \ \_____  \ \  \_|/__  \ \  \ \ \_____  \   
  \|____|\  \ \  \_|\ \  \ \  \ \|____|\  \  
    ____\_\  \ \_______\  \ \__\  ____\_\  \ 
   |\_________\|_______|   \|__| |\_________\
   \|_________|                  \|_________|
"""



if __name__ == "__main__":
    app.run(debug=True)
