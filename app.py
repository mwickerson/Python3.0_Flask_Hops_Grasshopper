"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm

import math
import re
import urllib.request
import collections
from collections import Counter
from collections import OrderedDict
import os
from os import path
import random

import numpy as np
import numpy.linalg

# import matplotlib
# import matplotlib.pyplot as plt

import pandas as pd
import io

# import scipy
# import seaborn
# import sklearn

from lxml import objectify

# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"

"""
import json
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
███╗   ███╗ ██████╗███╗   ██╗███████╗███████╗██╗                   
████╗ ████║██╔════╝████╗  ██║██╔════╝██╔════╝██║                   
██╔████╔██║██║     ██╔██╗ ██║█████╗  █████╗  ██║                   
██║╚██╔╝██║██║     ██║╚██╗██║██╔══╝  ██╔══╝  ██║                   
██║ ╚═╝ ██║╚██████╗██║ ╚████║███████╗███████╗███████╗              
╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝              
                                                                   
███████╗██╗  ██╗ █████╗ ███╗   ███╗██████╗ ██╗     ███████╗███████╗
██╔════╝╚██╗██╔╝██╔══██╗████╗ ████║██╔══██╗██║     ██╔════╝██╔════╝
█████╗   ╚███╔╝ ███████║██╔████╔██║██████╔╝██║     █████╗  ███████╗
██╔══╝   ██╔██╗ ██╔══██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ╚════██║
███████╗██╔╝ ██╗██║  ██║██║ ╚═╝ ██║██║     ███████╗███████╗███████║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚══════╝  
"""

@hops.component(
    "/binmult",
    name="BinMult",
    description="BinMult",
    category="Math",
    subcategory="Math",
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
    category="Math",
    subcategory="Math",
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
    category="Rhino3dm",
    subcategory="Rhino3dm",
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
    category="Rhino3dm",
    subcategory="Rhino3dm",
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
    category="Rhino3dm",
    subcategory="Rhino3dm",
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
    category="Rhino3dm",
    subcategory="Rhino3dm",
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
    category="Matplotlib",
    subcategory="Matplotlib",
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
    category="test",
    subcategory="test",
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
██╗    ██╗██╗ ██████╗██╗  ██╗███████╗██████╗ ███████╗ ██████╗ ███╗   ██╗
██║    ██║██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝██╔═══██╗████╗  ██║
██║ █╗ ██║██║██║     █████╔╝ █████╗  ██████╔╝███████╗██║   ██║██╔██╗ ██║
██║███╗██║██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║██║   ██║██║╚██╗██║
╚███╔███╔╝██║╚██████╗██║  ██╗███████╗██║  ██║███████║╚██████╔╝██║ ╚████║
 ╚══╝╚══╝ ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                        
███████╗████████╗██╗   ██╗██████╗ ██╗ ██████╗ ███████╗                  
██╔════╝╚══██╔══╝██║   ██║██╔══██╗██║██╔═══██╗██╔════╝                  
███████╗   ██║   ██║   ██║██║  ██║██║██║   ██║███████╗                  
╚════██║   ██║   ██║   ██║██║  ██║██║██║   ██║╚════██║                  
███████║   ██║   ╚██████╔╝██████╔╝██║╚██████╔╝███████║                  
╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝ ╚══════╝                  
                                                                        
███████╗██╗  ██╗ █████╗ ███╗   ███╗██████╗ ██╗     ███████╗███████╗     
██╔════╝╚██╗██╔╝██╔══██╗████╗ ████║██╔══██╗██║     ██╔════╝██╔════╝     
█████╗   ╚███╔╝ ███████║██╔████╔██║██████╔╝██║     █████╗  ███████╗     
██╔══╝   ██╔██╗ ██╔══██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ╚════██║     
███████╗██╔╝ ██╗██║  ██║██║ ╚═╝ ██║██║     ███████╗███████╗███████║     
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚══════╝     
"""
@hops.component(
    "/squares",
    name="Squares",
    description="Squares",
    category="Math",
    subcategory="Math",
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
    name="Squares",
    description="Squares",
    category="Math",
    subcategory="Math",
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
    category="Math",
    subcategory="Math",
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
    category="Math",
    subcategory="Math",
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
    category="Math",
    subcategory="Math",
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
    category="Math",
    subcategory="Math",
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
    category="Conditions",
    subcategory="Conditions",
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
    category="Conditions",
    subcategory="Conditions",
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
    category="Test",
    subcategory="Test",
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
███████╗████████╗██████╗ ██╗███╗   ██╗ ██████╗ ███████╗
██╔════╝╚══██╔══╝██╔══██╗██║████╗  ██║██╔════╝ ██╔════╝
███████╗   ██║   ██████╔╝██║██╔██╗ ██║██║  ███╗███████╗
╚════██║   ██║   ██╔══██╗██║██║╚██╗██║██║   ██║╚════██║
███████║   ██║   ██║  ██║██║██║ ╚████║╚██████╔╝███████║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
"""

@hops.component(
    "/strings",
    name="strings",
    nickname="strings",
    description="Work with strings with CPython",
    category="Strings",
    subcategory="Strings",
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
██╗     ██╗███████╗████████╗███████╗
██║     ██║██╔════╝╚══██╔══╝██╔════╝
██║     ██║███████╗   ██║   ███████╗
██║     ██║╚════██║   ██║   ╚════██║
███████╗██║███████║   ██║   ███████║
╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝
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
███████╗████████╗ █████╗  ██████╗██╗  ██╗███████╗
██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝
███████╗   ██║   ███████║██║     █████╔╝ ███████╗
╚════██║   ██║   ██╔══██║██║     ██╔═██╗ ╚════██║
███████║   ██║   ██║  ██║╚██████╗██║  ██╗███████║
╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝
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
 ██████╗ ██████╗ ███╗   ██╗████████╗██████╗  ██████╗ ██╗     
██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██║     
██║     ██║   ██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║     
██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║     
╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████╗
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                                             
███████╗██╗      ██████╗ ██╗    ██╗                          
██╔════╝██║     ██╔═══██╗██║    ██║                          
█████╗  ██║     ██║   ██║██║ █╗ ██║                          
██╔══╝  ██║     ██║   ██║██║███╗██║                          
██║     ███████╗╚██████╔╝╚███╔███╔╝                          
╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝      
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
██╗      ██████╗  ██████╗ ██████╗ ███████╗
██║     ██╔═══██╗██╔═══██╗██╔══██╗██╔════╝
██║     ██║   ██║██║   ██║██████╔╝███████╗
██║     ██║   ██║██║   ██║██╔═══╝ ╚════██║
███████╗╚██████╔╝╚██████╔╝██║     ███████║
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝
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
██╗      ██████╗  ██████╗ ██████╗ ██╗███╗   ██╗ ██████╗                         
██║     ██╔═══██╗██╔═══██╗██╔══██╗██║████╗  ██║██╔════╝                         
██║     ██║   ██║██║   ██║██████╔╝██║██╔██╗ ██║██║  ███╗                        
██║     ██║   ██║██║   ██║██╔═══╝ ██║██║╚██╗██║██║   ██║                        
███████╗╚██████╔╝╚██████╔╝██║     ██║██║ ╚████║╚██████╔╝                        
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝                         
                                                                                
████████╗███████╗ ██████╗██╗  ██╗███╗   ██╗██╗ ██████╗ ██╗   ██╗███████╗███████╗
╚══██╔══╝██╔════╝██╔════╝██║  ██║████╗  ██║██║██╔═══██╗██║   ██║██╔════╝██╔════╝
   ██║   █████╗  ██║     ███████║██╔██╗ ██║██║██║   ██║██║   ██║█████╗  ███████╗
   ██║   ██╔══╝  ██║     ██╔══██║██║╚██╗██║██║██║▄▄ ██║██║   ██║██╔══╝  ╚════██║
   ██║   ███████╗╚██████╗██║  ██║██║ ╚████║██║╚██████╔╝╚██████╔╝███████╗███████║
   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝
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
███╗   ███╗██╗███████╗ ██████╗███████╗██╗     ██╗      █████╗ ███╗   ██╗███████╗ ██████╗ ██╗   ██╗███████╗
████╗ ████║██║██╔════╝██╔════╝██╔════╝██║     ██║     ██╔══██╗████╗  ██║██╔════╝██╔═══██╗██║   ██║██╔════╝
██╔████╔██║██║███████╗██║     █████╗  ██║     ██║     ███████║██╔██╗ ██║█████╗  ██║   ██║██║   ██║███████╗
██║╚██╔╝██║██║╚════██║██║     ██╔══╝  ██║     ██║     ██╔══██║██║╚██╗██║██╔══╝  ██║   ██║██║   ██║╚════██║
██║ ╚═╝ ██║██║███████║╚██████╗███████╗███████╗███████╗██║  ██║██║ ╚████║███████╗╚██████╔╝╚██████╔╝███████║
╚═╝     ╚═╝╚═╝╚══════╝ ╚═════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝"""

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

██╗      █████╗ ███╗   ███╗██████╗ ██████╗  █████╗ 
██║     ██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔══██╗
██║     ███████║██╔████╔██║██████╔╝██║  ██║███████║
██║     ██╔══██║██║╚██╔╝██║██╔══██╗██║  ██║██╔══██║
███████╗██║  ██║██║ ╚═╝ ██║██████╔╝██████╔╝██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═════╝ ╚═╝  ╚═╝
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
███████╗██╗██████╗ ███████╗████████╗                                      
██╔════╝██║██╔══██╗██╔════╝╚══██╔══╝                                      
█████╗  ██║██████╔╝███████╗   ██║                                         
██╔══╝  ██║██╔══██╗╚════██║   ██║                                         
██║     ██║██║  ██║███████║   ██║                                         
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝                                         
                                                                          
 ██████╗██╗      █████╗ ███████╗███████╗                                  
██╔════╝██║     ██╔══██╗██╔════╝██╔════╝                                  
██║     ██║     ███████║███████╗███████╗                                  
██║     ██║     ██╔══██║╚════██║╚════██║                                  
╚██████╗███████╗██║  ██║███████║███████║                                  
 ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝                                  
                                                                          
███████╗██╗   ██╗███╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔════╝██║   ██║████╗  ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
█████╗  ██║   ██║██╔██╗ ██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗
██╔══╝  ██║   ██║██║╚██╗██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║
██║     ╚██████╔╝██║ ╚████║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║
╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝                                                                            \|_________|
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
 ██████╗██╗      █████╗ ███████╗███████╗███████╗███████╗    
██╔════╝██║     ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝    
██║     ██║     ███████║███████╗███████╗█████╗  ███████╗    
██║     ██║     ██╔══██║╚════██║╚════██║██╔══╝  ╚════██║    
╚██████╗███████╗██║  ██║███████║███████║███████╗███████║    
 ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝    
                                                            
 █████╗ ███╗   ██╗██████╗                                   
██╔══██╗████╗  ██║██╔══██╗                                  
███████║██╔██╗ ██║██║  ██║                                  
██╔══██║██║╚██╗██║██║  ██║                                  
██║  ██║██║ ╚████║██████╔╝                                  
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝                                   
                                                            
 ██████╗ ██████╗      ██╗███████╗ ██████╗████████╗███████╗  
██╔═══██╗██╔══██╗     ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝  
██║   ██║██████╔╝     ██║█████╗  ██║        ██║   ███████╗  
██║   ██║██╔══██╗██   ██║██╔══╝  ██║        ██║   ╚════██║  
╚██████╔╝██████╔╝╚█████╔╝███████╗╚██████╗   ██║   ███████║  
 ╚═════╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝  
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
 █████╗ ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗██████╗ 
██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗
███████║██║  ██║██║   ██║███████║██╔██╗ ██║██║     █████╗  ██║  ██║
██╔══██║██║  ██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔══╝  ██║  ██║
██║  ██║██████╔╝ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗██████╔╝
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ 
                                                                   
 ██████╗██╗      █████╗ ███████╗███████╗███████╗███████╗           
██╔════╝██║     ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝           
██║     ██║     ███████║███████╗███████╗█████╗  ███████╗           
██║     ██║     ██╔══██║╚════██║╚════██║██╔══╝  ╚════██║           
╚██████╗███████╗██║  ██║███████║███████║███████╗███████║           
 ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝   
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
███████╗██╗  ██╗ ██████╗███████╗██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝╚██╗██╔╝██╔════╝██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
█████╗   ╚███╔╝ ██║     █████╗  ██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
██╔══╝   ██╔██╗ ██║     ██╔══╝  ██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║
███████╗██╔╝ ██╗╚██████╗███████╗██║        ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                       
██╗  ██╗ █████╗ ███╗   ██╗██████╗ ██╗     ██╗███╗   ██╗ ██████╗        
██║  ██║██╔══██╗████╗  ██║██╔══██╗██║     ██║████╗  ██║██╔════╝        
███████║███████║██╔██╗ ██║██║  ██║██║     ██║██╔██╗ ██║██║  ███╗       
██╔══██║██╔══██║██║╚██╗██║██║  ██║██║     ██║██║╚██╗██║██║   ██║       
██║  ██║██║  ██║██║ ╚████║██████╔╝███████╗██║██║ ╚████║╚██████╔╝       
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝     """

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
███████╗██╗██╗     ███████╗                                     
██╔════╝██║██║     ██╔════╝                                     
█████╗  ██║██║     █████╗                                       
██╔══╝  ██║██║     ██╔══╝                                       
██║     ██║███████╗███████╗                                     
╚═╝     ╚═╝╚══════╝╚══════╝                                     
                                                                
██╗  ██╗ █████╗ ███╗   ██╗██████╗ ██╗     ██╗███╗   ██╗ ██████╗ 
██║  ██║██╔══██╗████╗  ██║██╔══██╗██║     ██║████╗  ██║██╔════╝ 
███████║███████║██╔██╗ ██║██║  ██║██║     ██║██╔██╗ ██║██║  ███╗
██╔══██║██╔══██║██║╚██╗██║██║  ██║██║     ██║██║╚██╗██║██║   ██║
██║  ██║██║  ██║██║ ╚████║██████╔╝███████╗██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝                                                                                            
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
██████╗  █████╗ ██████╗ ████████╗    ████████╗██╗    ██╗ ██████╗ 
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ╚══██╔══╝██║    ██║██╔═══██╗
██████╔╝███████║██████╔╝   ██║          ██║   ██║ █╗ ██║██║   ██║
██╔═══╝ ██╔══██║██╔══██╗   ██║          ██║   ██║███╗██║██║   ██║
██║     ██║  ██║██║  ██║   ██║          ██║   ╚███╔███╔╝╚██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝          ╚═╝    ╚══╝╚══╝  ╚═════╝ 
                                                                 
"""

"""
██████╗ ███████╗ ██████╗ ███████╗██╗  ██╗
██╔══██╗██╔════╝██╔════╝ ██╔════╝╚██╗██╔╝
██████╔╝█████╗  ██║  ███╗█████╗   ╚███╔╝ 
██╔══██╗██╔══╝  ██║   ██║██╔══╝   ██╔██╗ 
██║  ██║███████╗╚██████╔╝███████╗██╔╝ ██╗
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
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
def _match1(string, pattern):
    return re.match(pattern, string)

# match start end and return the match
@hops.component(
    "/start_end2",
    name="Match Start",
    nickname="MatchStart",
    description="Match start end and return the match",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("String", "S", "String to search"),
        hs.HopsString("Pattern", "P", "Pattern to search for"),
    ],
    outputs=[
        hs.HopsString("Start", "S", "Start"),
        hs.HopsString("End", "E", "End"),
    ],
)
def start_end(string, pattern):
    s = re.search(pattern, string)
    return s.start(), s.end()

# zero-or-one
# the asterisk regex
# the + regex
# the ? regex
# the {n} regex
# the {n,} regex
# the {n,m} regex
# the . regex
# the ^ regex
# the $ regex
# the | regex
# the ( regex
# the ) regex
# the [ regex
# the ] regex
# the { regex
# the } regex

# web scraping and scraping regex
@hops.component(
    "/_web_scrape",
    name="Web Scrape",
    nickname="WebScrape",
    description="Web scrape a website",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("URL", "U", "URL to scrape"),
        hs.HopsString("Pattern", "P", "Pattern to search for"),
    ],
    outputs=[
        hs.HopsString("Matches", "M", "All matches"),
    ],
)
def _web_scrape(url, pattern):
    return re.findall(pattern, url)

# urllib.request.urlopen(url)
# urllib.request.urlretrieve(url, filename)
# urllib.request.urlcleanup()
# urllib.request.urlencode(data)
# urllib.request.urlparse(url)
# urllib.request.urlunparse(parsed)
# urllib.request.urlretrieve(url, filename)

@hops.component(
    "/_url_retrieve",
    name="URL Retrieve",
    nickname="URLRetrieve",
    description="URL retrieve a website",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("URL", "U", "URL to retrieve"),
        hs.HopsString("Filename", "F", "Filename to save to"),
    ],
    outputs=[
        hs.HopsString("Filename", "F", "Filename to save to"),
    ],
)
def _url_retrieve(url, filename):
    urllib.request.urlretrieve(url, filename)
    return filename

@hops.component(
    "/_url_cleanup",
    name="URL Cleanup",
    nickname="URLCleanup",
    description="URL cleanup",
    category="String",
    subcategory="Regex",
    inputs=[],
    outputs=[],
)
def _url_cleanup():
    urllib.request.urlcleanup()
    return None

@hops.component(
    "/_url_encode",
    name="URL Encode",
    nickname="URLEncode",
    description="URL encode",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("Data", "D", "Data to encode"),
    ],
    outputs=[
        hs.HopsString("Encoded", "E", "Encoded data"),
    ],
)
def _url_encode(data):
    return urllib.request.urlencode(data)

@hops.component(
    "/_url_parse",
    name="URL Parse",
    nickname="URLParse",
    description="URL parse",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("URL", "U", "URL to parse"),
    ],
    outputs=[
        hs.HopsString("Parsed", "P", "Parsed URL"),
    ],
)
def _url_parse(url):
    return urllib.request.urlparse(url)

@hops.component(
    "/_url_unparse",
    name="URL Unparse",
    nickname="URLUnparse",
    description="URL unparse",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("Parsed", "P", "Parsed URL"),
    ],
    outputs=[
        hs.HopsString("URL", "U", "URL"),
    ],
)
def _url_unparse(parsed):
    return urllib.request.urlunparse(parsed)

# analysis hyperlink regex

@hops.component(
    "/_analysis_hyperlink",
    name="Analysis Hyperlink",
    nickname="AnalysisHyperlink",
    description="Analysis hyperlink",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("URL", "U", "URL to parse"),
    ],
    outputs=[
        hs.HopsString("Analysis", "A", "Analysis"),
    ],
)
def _analysis_hyperlink(url):
    return re.findall(r"https://www.analysis.com/([^/]+)", url)

# !DOCTYPE html regex
@hops.component(
    "/_doctype_html",
    name="DOCTYPE HTML",
    nickname="DOCTYPEHTML",
    description="DOCTYPE HTML",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("HTML", "H", "HTML to parse"),
    ],
    outputs=[
        hs.HopsString("DOCTYPE", "D", "DOCTYPE"),
    ],
)
def _doctype_html(html):
    return re.findall(r"<!DOCTYPE html>", html)

# Extract all hyperlinks from HTML
@hops.component(
    "/_extract_hyperlinks",
    name="Extract Hyperlinks",
    nickname="ExtractHyperlinks",
    description="Extract hyperlinks",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("HTML", "H", "HTML to parse"),
    ],
    outputs=[
        hs.HopsString("Hyperlinks", "H", "Hyperlinks"),
    ],
)
def _extract_hyperlinks(html):
    return re.findall(r"<a href=\"([^\"]+)\"", html)

# Extract dollars from a string
@hops.component(
    "/_extract_dollars",
    name="Extract Dollars",
    nickname="ExtractDollars",
    description="Extract dollars",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Dollars", "D", "Dollars"),
    ],
)
def _extract_dollars(string):
    return re.findall(r"\$[0-9]+", string)

# Finding Nonsecure HTTP URLs
@hops.component(
    "/_find_nonsecure_http_urls",
    name="Find Nonsecure HTTP URLs",
    nickname="FindNonsecureHTTPURLs",
    description="Find nonsecure HTTP URLs",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("HTML", "H", "HTML to parse"),
    ],
    outputs=[
        hs.HopsString("Nonsecure HTTP URLs", "N", "Nonsecure HTTP URLs"),
    ],
)
def _find_nonsecure_http_urls(html):
    return re.findall(r"http://[^s]", html)

# Validating the Time Format of User inputs
@hops.component(
    "/_validate_time_format",
    name="Validate Time Format",
    nickname="ValidateTimeFormat",
    description="Validate time format",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("Time", "T", "Time to validate"),
    ],
    outputs=[
        hs.HopsString("Valid", "V", "Valid"),
    ],
)
def _validate_time_format(time):
    inputs_ok = re.findall(r"^[0-9]{2}:[0-9]{2}:[0-9]{2}$", time)
    if inputs_ok:
        return True
    else:
        return False

# detacting duplicate lines in a file
@hops.component(
    "/_detect_duplicate_lines",
    name="Detect Duplicate Lines",
    nickname="DetectDuplicateLines",
    description="Detect duplicate lines",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("File", "F", "File to parse"),
    ],
    outputs=[
        hs.HopsString("Duplicate Lines", "D", "Duplicate Lines"),
    ],
)
def _detect_duplicate_lines(file):
    with open(file, "r") as f:
        lines = f.readlines()
        return list(set(lines))

# Detecting word repetition in a string with regex
@hops.component(
    "/_detect_word_repetition",
    name="Detect Word Repetition",
    nickname="DetectWordRepetition",
    description="Detect word repetition",
    category="String",
    subcategory="Regex",    
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Repetition", "R", "Repetition"),
    ],
)
def _detect_word_repetition(string):
    return re.findall(r"(\w+)\1+", string)

# Modifying regex patterns in a multi-line string
@hops.component(
    "/_modify_regex_patterns",
    name="Modify Regex Patterns",
    nickname="ModifyRegexPatterns",
    description="Modify regex patterns",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Modified", "M", "Modified"),
    ],
)
def _modify_regex_patterns(string):
    return re.sub(r"(\w+)\1+", r"\1", string)


# sub() regex
@hops.component(
    "/_sub_regex",
    name="Sub Regex",
    nickname="SubRegex",
    description="Sub regex",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Subbed", "S", "Subbed"),
    ],
)
def _sub_regex(string):
    return re.sub(r"(\w+)\1+", r"\1", string)

# subn() regex
@hops.component(
    "/_subn_regex",
    name="Subn Regex",
    nickname="SubnRegex",
    description="Subn regex",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Subbed", "S", "Subbed"),
    ],
)
def _subn_regex(string):
    return re.subn(r"(\w+)\1+", r"\1", string)

# escape() regex
@hops.component(
    "/_escape_regex",
    name="Escape Regex",
    nickname="EscapeRegex",
    description="Escape regex",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Escaped", "E", "Escaped"),
    ],
)
def _escape_regex(string):
    return re.escape(string)

# password check regex
@hops.component(
    "/_password_check_regex",
    name="Password Check Regex",
    nickname="PasswordCheckRegex",
    description="Password check regex",
    category="String",
    subcategory="Regex",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Password Check", "P", "Password Check"),
    ],
)
def _password_check_regex(string):
    return re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", string)


"""
 ██████╗ ██████╗ ██╗     ██╗     ███████╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔════╝██╔═══██╗██║     ██║     ██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
██║     ██║   ██║██║     ██║     █████╗  ██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗
██║     ██║   ██║██║     ██║     ██╔══╝  ██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║
╚██████╗╚██████╔╝███████╗███████╗███████╗╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║
 ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                                                        
███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗                                   
████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝                                   
██╔████╔██║██║   ██║██║  ██║██║   ██║██║     █████╗                                     
██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══╝                                     
██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗███████╗                                   
╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝   
"""

# python collections module
# ways to create a counter
@hops.component(
    "/_create_counter",
    name="Create Counter",
    nickname="CreateCounter",
    description="Create counter",
    category="Collections",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Counter", "C", "Counter"),
    ],
)
def _create_counter(string):
    return collections.Counter(string)

# ordered dictionary collections
@hops.component(
    "/ordered_dict",
    name="Ordered Dictionary",
    nickname="OrderedDictionary",
    description="Ordered dictionary",
    category="Collections",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Ordered Dictionary", "D", "Ordered Dictionary"),
    ],
)
def _ordered_dict(string):
    d = {}
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    return collections.OrderedDict(d)

# ordered dictionary collections
@hops.component(
    "/ordered_dict2",
    name="Ordered Dictionary",
    nickname="OrderedDictionary",
    description="Ordered dictionary",
    category="Collections",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Ordered Dictionary", "D", "Ordered Dictionary"),
    ],
)
def _ordered_dict2(string):
    od = collections.OrderedDict()
    od['a'] = 1
    od['b'] = 2
    od['c'] = 3
    for k, v in od.items():
        print(k, v)
    return od

# defaultdict collections
@hops.component(
    "/default_dict",
    name="Default Dictionary",
    nickname="DefaultDictionary",
    description="Default dictionary",
    category="Collections",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Default Dictionary", "D", "Default Dictionary"),
    ],
)
def _default_dict(string):
    d = collections.defaultdict(int)
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    for i in d.items():
        print(i)
    return d

# chainmap collections
@hops.component(
    "/chain_map",
    name="Chain Map",
    nickname="ChainMap",
    description="Chain map",
    category="Collections",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Chain Map", "D", "Chain Map"),
    ],
)
def _chain_map(string):
    d = collections.ChainMap({'a': 1}, {'b': 2}, {'c': 3})
    for i in d.items():
        print(i)
    return d

# accessing keys and values from collections    
@hops.component(
    "/access_keys_values",
    name="Access Keys Values",
    nickname="AccessKeysValues",
    description="Access keys and values from collections",
    category="Collections",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Access Keys Values", "D", "Access Keys Values"),
    ],
)
def _access_keys_values(string):
    d = collections.ChainMap({'a': 1}, {'b': 2}, {'c': 3})
    for k, v in d.items():
        print(k, v)
    return d

# namedtuple collections
@hops.component(
    "/named_tuple",
    name="Named Tuple",
    nickname="NamedTuple",
    description="Named tuple",
    category="Collections",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Named Tuple", "D", "Named Tuple"),
    ],
)
def _named_tuple(string):
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(11, y=22)
    return p

# conversion operations on collections
@hops.component(
    "/conversion_operations",
    name="Conversion Operations",
    nickname="ConversionOperations",
    description="Conversion operations on collections",
    category="Collections",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Conversion Operations", "D", "Conversion Operations"),
    ],
)
def _conversion_operations(string):
    d = collections.ChainMap({'a': 1}, {'b': 2}, {'c': 3})
    for k, v in d.items():
        print(k, v)
    return d

# deque collections
@hops.component(
    "/deque",
    name="Deque",
    nickname="Deque",
    description="Deque",
    category="Collections",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Deque", "D", "Deque"),
    ],
)
def _deque(string):
    d = collections.deque(['a', 'b', 'c'])
    d.append('x')
    d.appendleft('y')
    for i in d:
        print(i)
    return d

# inserting elements into collections
@hops.component(
    "/insert_elements",
    name="Insert Elements",
    nickname="InsertElements",
    description="Insert elements into collections",
    category="Collections",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Insert Elements", "D", "Insert Elements"),
    ],
)
def _insert_elements(string):
    d = collections.deque(['a', 'b', 'c'])
    d.append('x')
    d.appendleft('y')
    for i in d:
        print(i)
    return d

# removing elements from collections
@hops.component(
    "/remove_elements",
    name="Remove Elements",
    nickname="RemoveElements",
    description="Remove elements from collections",
    category="Collections",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("Remove Elements", "D", "Remove Elements"),
    ],  
)
def _remove_elements(string):
    d = collections.deque(['a', 'b', 'c'])
    d.append('x')
    d.appendleft('y')
    d.pop()
    d.popleft()
    for i in d:
        print(i)
    return d

# userdict userlist userstring collections
@hops.component(
    "/user_dict",
    name="User Dictionary",
    nickname="UserDictionary",
    description="User dictionary",
    category="Collections",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("User Dictionary", "D", "User Dictionary"),
    ],
)
def _user_dict(string):
    from collections import UserDict
    d = UserDict({'a': 1, 'b': 2, 'c': 3})
    for k, v in d.items():
        print(k, v)
    return d

@hops.component(
    "/user_list",
    name="User List",
    nickname="UserList",
    description="User list",
    category="Collections",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("User List", "D", "User List"),
    ],
)
def _user_list(string):
    from collections import UserList
    d = UserList([1, 2, 3])
    for i in d:
        print(i)
    return d

@hops.component(
    "/user_string",
    name="User String",
    nickname="UserString",
    description="User string",
    category="Collections",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("User String", "D", "User String"),
    ],
)
def _user_string(string):
    from collections import UserString
    d = UserString('hello')
    return d

"""
 ██████╗ ███████╗    ███╗   ███╗ ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗
██╔═══██╗██╔════╝    ████╗ ████║██╔═══██╗██╔══██╗██║   ██║██║     ██╔════╝
██║   ██║███████╗    ██╔████╔██║██║   ██║██║  ██║██║   ██║██║     █████╗  
██║   ██║╚════██║    ██║╚██╔╝██║██║   ██║██║  ██║██║   ██║██║     ██╔══╝  
╚██████╔╝███████║    ██║ ╚═╝ ██║╚██████╔╝██████╔╝╚██████╔╝███████╗███████╗
 ╚═════╝ ╚══════╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
"""

# OS module - operating system functions
@hops.component(
    "/_os",
    name="OS",
    nickname="OS",
    description="Operating system functions",
    category="OS",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("OS", "D", "OS"),
        ],
)
def _os(string):
    return os.name

# OS module - operating system functions
@hops.component(
    "/_os_path",
    name="OS Path",
    nickname="OSPath",
    description="Operating system path functions",
    category="OS",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("OS Path", "D", "OS Path"),
        ],
)
def _os_path(string):
    return os.path.abspath(os.path.dirname(__file__))

# OS module - operating system functions
@hops.component(
    "/_os_system",
    name="OS System",
    nickname="OSSystem",
    description="Operating system system functions",
    category="OS",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("OS System", "D", "OS System"),
        ],
)
def _os_system(string):
    print(os.system('ls'))
    return os.system('ls')

# os.getcwd() - get current working directory
@hops.component(
    "/_os_getcwd",
    name="OS Getcwd",
    nickname="OSGetcwd",
    description="Get current working directory",
    category="OS",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("OS Getcwd", "D", "OS Getcwd"),
        ],
)
def _os_getcwd(string):
    return os.getcwd()

# os.chdir() - change current working directory
@hops.component(
    "/_os_chdir",
    name="OS Chdir",
    nickname="OSChdir",
    description="Change current working directory",
    category="OS",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("OS Chdir", "D", "OS Chdir"),
        ],
)
def _os_chdir(string):
    os.chdir('/')
    return os.getcwd()

# os.mkdir() and os.makedirs() - create a directory
@hops.component(
    "/_os_mkdir",
    name="OS Mkdir",
    nickname="OSMkdir",
    description="Create a directory",
    category="OS",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("OS Mkdir", "D", "OS Mkdir"),
        ],
)
def _os_mkdir(string):
    os.mkdir('/tmp/test')
    return os.getcwd()

@hops.component(
    "/_os_makedirs",
    name="OS Makedirs",
    nickname="OSMakedirs",
    description="Create a directory",
    category="OS",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("OS Makedirs", "D", "OS Makedirs"),
        ],
)
def _os_makedirs(string):
    os.makedirs('/tmp/test/test2')
    return os.getcwd()

# os.mkdir() and os.makedirs() - create a directory advanced
@hops.component(
    "/mkdir_advanced",
    name="OS Mkdir Advanced",
    nickname="OSMkdirAdvanced",
    description="Create a directory advanced",
    category="OS",
    subcategory="Python",
    inputs=[
        hs.HopsString("directory", "dir", "Directory to create"),
        hs.HopsString("parent_directory", "pdir", "Parent directory to create"),
        hs.HopsString("path", "path", "Path to create"),
    ],
    outputs=[
        hs.HopsString("OS Mkdir Advanced", "D", "OS Mkdir Advanced"),
        ],
)
def _os_mkdir_advanced(directory, parent_directory, path):
    os.mkdir(os.path.join(parent_directory, path, directory))
    return os.getcwd()


# os.listdir() - list files in a directory
@hops.component(
    "/listdir",
    name="OS Listdir",
    nickname="OSListdir",
    description="List files in a directory",
    category="OS",
    subcategory="Python",
    inputs=[
        hs.HopsString("String", "S", "String to parse"),
    ],
    outputs=[
        hs.HopsString("OS Listdir", "D", "OS Listdir"),
        ],
)
def _os_listdir(string):
    path = "/"
    dir_list = os.listdir(path)
    return dir_list

# os.remove() - remove a file
# os.rmdir() - remove a directory
# os.removedirs() - remove a directory and all its contents

# os.join() - join path components together
# os.sep - path separator
# os.pathsep - path separator
# os.linesep - newline separator
# os.curdir - current directory
# os.pardir - parent directory
# os.extsep - extension separator
# os.altsep - alternate extension separator
# os.path.split() - split a path into [head, tail]
# os.path.splitext() - split a path into [path, ext]
# os.path.splitdrive() - split a path into [head, tail]
# os.path.splitext() - split a path into [path, ext]
# os.path.splitunc() - split a path into [head, tail]

# commonly used os functions
# name = os.path.basename(path) - return the base name of a pathname
# error = os.path.exists(path) - return true if path exists
# close = os.path.isfile(path) - return true if path is a file
# close = os.path.isdir(path) - return true if path is a directory
# rename = os.path.join(path1, path2) - join two pathname components
# remove = os.path.split(path) - split a path into [head, tail] 
# exists = os.path.exists(path) - return true if path exists

"""
██╗███╗   ██╗████████╗███████╗██████╗ ███╗   ███╗██╗███████╗███████╗██╗ ██████╗ ███╗   ██╗
██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║██╔════╝██╔════╝██║██╔═══██╗████╗  ██║
██║██╔██╗ ██║   ██║   █████╗  ██████╔╝██╔████╔██║██║███████╗███████╗██║██║   ██║██╔██╗ ██║
██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║╚════██║╚════██║██║██║   ██║██║╚██╗██║
██║██║ ╚████║   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║███████║███████║██║╚██████╔╝██║ ╚████║
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                          
 █████╗ ██╗      ██████╗  ██████╗ ██████╗ ██╗████████╗██╗  ██╗███╗   ███╗███████╗         
██╔══██╗██║     ██╔════╝ ██╔═══██╗██╔══██╗██║╚══██╔══╝██║  ██║████╗ ████║██╔════╝         
███████║██║     ██║  ███╗██║   ██║██████╔╝██║   ██║   ███████║██╔████╔██║███████╗         
██╔══██║██║     ██║   ██║██║   ██║██╔══██╗██║   ██║   ██╔══██║██║╚██╔╝██║╚════██║         
██║  ██║███████╗╚██████╔╝╚██████╔╝██║  ██║██║   ██║   ██║  ██║██║ ╚═╝ ██║███████║         
╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                                                                                                          
"""
# algorithms   
# https://www.geeksforgeeks.org/bubble-sort/
# https://www.geeksforgeeks.org/selection-sort/
# https://www.geeksforgeeks.org/insertion-sort/
# https://www.geeksforgeeks.org/shell-sort/
# https://www.geeksforgeeks.org/merge-sort/
# https://www.geeksforgeeks.org/quick-sort/
# https://www.geeksforgeeks.org/counting-sort/
# https://www.geeksforgeeks.org/radix-sort/
# https://www.geeksforgeeks.org/bucket-sort/

@hops.component(
    "/bubble",
    name=("Bubble Sort"),
    description=("Bubble Sort"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
)
def bubble_sort(num_list):
    """
    Bubble Sort
    """
    for i in range(len(num_list)):
        for j in range(0, len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list

@hops.component(
    "/selection",
    name=("Selection Sort"),
    description=("Selection Sort"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
)
def selection_sort(num_list):
    """
    Selection Sort
    """
    for i in range(len(num_list)):
        min_index = i
        for j in range(i + 1, len(num_list)):
            if num_list[min_index] > num_list[j]:
                min_index = j
        num_list[i], num_list[min_index] = num_list[min_index], num_list[i]
    return num_list

@hops.component(
    "/insertion",
    name=("Insertion Sort"),
    description=("Insertion Sort"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
)
def insertion_sort(num_list):
    """
    Insertion Sort
    """
    for i in range(1, len(num_list)):
        key = num_list[i]
        j = i - 1
        while j >= 0 and num_list[j] > key:
            num_list[j + 1] = num_list[j]
            j -= 1
        num_list[j + 1] = key
    return num_list

@hops.component(
    "/shell",
    name=("Shell Sort"),
    description=("Shell Sort"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
)
def shell_sort(num_list):
    """
    Shell Sort
    """
    n = len(num_list)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = num_list[i]
            j = i
            while j >= gap and num_list[j - gap] > temp:
                num_list[j] = num_list[j - gap]
                j -= gap
            num_list[j] = temp
        gap //= 2
    return num_list

@hops.component(
    "/merge",
    name=("Merge Sort"),
    description=("Merge Sort"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
)
def merge_sort(num_list):
    """
    Merge Sort
    """
    if len(num_list) > 1:
        mid = len(num_list) // 2
        left = num_list[:mid]
        right = num_list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                num_list[k] = left[i]
                i += 1
            else:
                num_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            num_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            num_list[k] = right[j]
            j += 1
            k += 1
    return num_list

@hops.component(
    "/quick",
    name=("Quick Sort"),
    description=("Quick Sort"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
)
def quick_sort(num_list):
    """
    Quick Sort
    """
    if len(num_list) > 1:
        pivot = num_list[0]
        i = 0
        for j in range(1, len(num_list)):
            if num_list[j] < pivot:
                i += 1
                num_list[i], num_list[j] = num_list[j], num_list[i]
        num_list[0], num_list[i] = num_list[i], num_list[0]
        quick_sort(num_list[:i])
        quick_sort(num_list[i + 1:])
    return num_list

@hops.component(
    "/radix",
    name=("Radix Sort"),
    description=("Radix Sort"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
)
def radix_sort(num_list):
    """
    Radix Sort
    """
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    return num_list

@hops.component(
    "/quick_sort_3way",
    name=("Quick Sort 3 Way"),
    description=("Quick Sort 3 Way"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
)
def quick_sort_3way(num_list):
    """
    Quick Sort 3 Way
    """
    if len(num_list) > 1:
        pivot = num_list[0]
        i = 0
        j = len(num_list) - 1
        k = 1
        while k <= j:
            if num_list[k] < pivot:
                num_list[k], num_list[i] = num_list[i], num_list[k]
                i += 1
                k += 1
            elif num_list[k] > pivot:
                num_list[k], num_list[j] = num_list[j], num_list[k]
                j -= 1
            else:
                k += 1
        quick_sort_3way(num_list[:i])
        quick_sort_3way(num_list[i:j])
        quick_sort_3way(num_list[j:])
    return num_list

@hops.component(
    "/bucket",
    name=("Bucket Sort"),
    description=("Bucket Sort"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
)
def bucket_sort(num_list):
    """
    Bucket Sort
    """
    n = len(num_list)
    if n == 0:
        return num_list
    max_num = max(num_list)
    bucket = [0] * (max_num + 1)
    for i in range(n):
        bucket[num_list[i]] += 1
    i = 0
    for j in range(max_num + 1):
        while bucket[j] > 0:
            num_list[i] = j
            i += 1
            bucket[j] -= 1
    return num_list

@hops.component(
    "/heap",
    name=("Heap Sort"),
    description=("Heap Sort"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
)
def heap_sort(num_list):
    """
    Heap Sort
    """
    n = len(num_list)
    for i in range(n, -1, -1):
        heapify(num_list, n, i)
    for i in range(n - 1, 0, -1):
        num_list[i], num_list[0] = num_list[0], num_list[i]
        heapify(num_list, i, 0)
    return num_list

@hops.component(
    "/cocktail",
    name=("Cocktail Sort"),
    description=("Cocktail Sort"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
)
def cocktail_sort(num_list):
    """
    Cocktail Sort
    """
    n = len(num_list)
    swapped = True
    start = 0
    end = n - 1
    while (start < end) and swapped:
        swapped = False
        for i in range(start, end):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
                swapped = True
        end -= 1
        if not swapped:
            break
        swapped = False
        for i in range(end - 1, start - 1, -1):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
                swapped = True
        start += 1
    return num_list

@hops.component(
    "/comb",
    name=("Comb Sort"),
    description=("Comb Sort"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
)
def comb_sort(num_list):
    """
    Comb Sort
    """
    n = len(num_list)
    gap = n
    swapped = True
    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False
        for i in range(n - gap):
            if num_list[i] > num_list[i + gap]:
                num_list[i], num_list[i + gap] = num_list[i + gap], num_list[i]
                swapped = True
    return num_list

@hops.component(
    "/gnome",
    name=("Gnome Sort"),
    description=("Gnome Sort"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
)
def gnome_sort(num_list):
    """
    Gnome Sort
    """
    n = len(num_list)
    i = 0
    while i < n:
        if i == 0 or num_list[i - 1] <= num_list[i]:
            i += 1
        else:
            num_list[i], num_list[i - 1] = num_list[i - 1], num_list[i]
            i -= 1
    return num_list

@hops.component(
    "/fisher",
    name=("Fisher Yates Shuffle"),
    description=("Fisher Yates Shuffle"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("num_list", "Number List", "number list", access = hs.HopsParamAccess.LIST),
    ],
)
def fisher_yates_shuffle(num_list):
    """
    Fisher Yates Shuffle
    """
    n = len(num_list)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        num_list[i], num_list[j] = num_list[j], num_list[i]
    return num_list



# finding anagrams with lambda functions and sorting and list comprehension
# https://www.geeksforgeeks.org/python-lambda-anonymous-function/
# https://www.geeksforgeeks.org/python-list-comprehension/
# https://www.geeksforgeeks.org/python-sorting-list-of-dictionaries-by-key/

@hops.component(
    "/anagram1",
    name=("Anagram"),
    description=("Anagram"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsString("string", "String", "string"),
       
    ],
    outputs=[
        hs.HopsString("string", "String", "string"),
    ],
)   
def anagram(string):
    """
    Anagram
    """
    # import permutations
    from itertools import permutations

    # sort the string
    string = sorted(string)
    
    # create a list of all possible anagrams
    anagrams = [''.join(sorted(word)) for word in permutations(string)]
    
    # remove duplicates
    anagrams = list(set(anagrams))
    
    # sort the list
    anagrams.sort()
    
    return anagrams

# finding palindromes with lambda functions and sorting and list comprehension

@hops.component(
    "/palindrome1",
    name=("Palindrome"),
    description=("Palindrome"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsString("string", "String", "string"),
       
    ],
    outputs=[
        hs.HopsString("string", "String", "string"),
    ],
)
def palindrome(string):
    """
    Palindrome
    """
    # import permutations
    from itertools import permutations

    # sort the string
    string = sorted(string)
    
    # create a list of all possible palindromes
    palindromes = [''.join(sorted(word)) for word in permutations(string)]
    
    # remove duplicates
    palindromes = list(set(palindromes))
    
    # sort the list
    palindromes.sort()
    
    return palindromes

# finding prime numbers with the sieve of eratosthenes
# https://www.geeksforgeeks.org/sieve-of-eratosthenes/
@hops.component(
    "/_prime100",
    name=("Prime"),
    description=("Prime"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsInteger("num", "Number", "number"),
    ],
    outputs=[
        hs.HopsInteger("num_out", "num_out", "num_out"),
    ]
)
def prime(n):
    import functools
    from functools import reduce
    primes = reduce(lambda r, x: r - set(range(x**2, n, x)) if x in r else r, range(2, int(n**0.5) + 1), set(range(2, n)))
    return list(primes)

# calculating the Fibonacci sequence with reduce() and lambda functions
# https://www.geeksforgeeks.org/python-reduce-function/
@hops.component(
    "/_fibonacci",
    name=("Fibonacci"),
    description=("Fibonacci"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsInteger("num", "Number", "number"),
    ],
    outputs=[
        hs.HopsInteger("num_out", "num_out", "num_out"),
    ]
)
def fibonacci(n):
    """
    Fibonacci
    """
    import functools
    from functools import reduce
    return reduce(lambda a, b: a + b, [0] + [1] * (n - 1))



"""
███╗   ███╗███████╗████████╗ █████╗                                                           
████╗ ████║██╔════╝╚══██╔══╝██╔══██╗                                                          
██╔████╔██║█████╗     ██║   ███████║                                                          
██║╚██╔╝██║██╔══╝     ██║   ██╔══██║                                                          
██║ ╚═╝ ██║███████╗   ██║   ██║  ██║                                                          
╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝                                                          
                                                                                              
██████╗ ██████╗  ██████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗███╗   ███╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║████╗ ████║██║████╗  ██║██╔════╝ 
██████╔╝██████╔╝██║   ██║██║  ███╗██████╔╝███████║██╔████╔██║██╔████╔██║██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██╔══██╗██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║
██║     ██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                              
██╗  ██╗ █████╗ ██████╗ ██████╗                                                               
██║  ██║██╔══██╗██╔══██╗██╔══██╗                                                              
███████║███████║██████╔╝██║  ██║                                                              
██╔══██║██╔══██║██╔══██╗██║  ██║                                                              
██║  ██║██║  ██║██║  ██║██████╔╝                                                              
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝   """
# meta programming - functions that can be passed as arguments to other functions


"""
███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ██╗   ██╗
████╗  ██║██║   ██║████╗ ████║██╔══██╗╚██╗ ██╔╝
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝ ╚████╔╝ 
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔═══╝   ╚██╔╝  
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║        ██║   
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝   
"""

# creating a 1D array of random numbers with numpy
@hops.component(
    "/randarr",
    name=("Random Array"),
    description=("Random Array"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsInteger("num", "Number", "number"),
    ],
    outputs=[
        hs.HopsNumber("array", "array", "array", access = hs.HopsParamAccess.LIST), 
    ]
)
def random_array(n):
    """
    Random Array
    """
    import numpy as np
    arr = np.random.randint(0, 100, n)
    arr = arr.tolist()
    return arr

@hops.component(
    "/randarr5",
    name=("Random Array"),
    description=("Random Array"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsInteger("amount", "amount", "amount"),
        hs.HopsInteger("num", "Number", "number", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("array", "array", "array", access = hs.HopsParamAccess.LIST),
    ]
)
def random_array5(amount, num):
    """
    Random Array
    """
    import numpy as np
    arr = np.random.randint(0, amount, num)
    arr = arr.tolist()
    return arr

# from ghpython remote work summer 2021, Wickerson Studios
"""
a = np.arange(range).reshape((x,y))
a = ghpythonremote.obtain(a.tolist())
a = list_to_tree(a, source=[0,0])  
"""

# basic array characteristics
@hops.component(
    "/array_stats",
    name=("Array Stats"),
    description=("Array Stats"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST), 
    ],
    outputs=[
        hs.HopsNumber("mean", "mean", "mean"),
        hs.HopsNumber("std", "std", "std"),
    ]
)
def array_stats(aList):
    """
    Array Stats
    """
    import numpy as np
    a = np.array(aList)
    mean = np.mean(a)
    std = np.std(a)
    return mean, std

@hops.component(
    "/array_stats4",
    name=("Array Stats"),
    description=("Array Stats"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("aList3", "aList2", "aList2", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("mean", "mean", "mean"),
        hs.HopsNumber("std", "std", "std"),
        hs.HopsNumber("min", "min", "min"),
        hs.HopsNumber("max", "max", "max"),
        hs.HopsNumber("median", "median", "median"),
    ]
)
def array_stats2(aList, aList2):
    """
    Array Stats
    """
    import numpy as np
    a = np.array([aList, aList2])
    mean = np.mean(a)
    std = np.std(a)
    min = np.min(a)
    max = np.max(a)
    median = np.median(a)
    return mean, std, min, max, median

@hops.component(
    "/array_stats7",
    name=("Array Stats"),
    description=("Array Stats"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("aList2", "aList2", "aList2", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("dim", "dim", "dim"),
        hs.HopsNumber("shape", "shape", "shape"),
        hs.HopsNumber("size", "size", "size"),
    ]
)
def array_stats3(aList, aList2):
    """
    Array Stats
    """
    import numpy as np
    a = np.array([aList, aList2])
    dim = a.ndim
    shape = a.shape
    size = a.size
    return dim, shape, size

# array creation
# creating array from list with concatenate
@hops.component(
    "/array_list44",
    name=("Array Stats"),
    description=("Array Stats"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("array1", "array1", "array1", access = hs.HopsParamAccess.LIST),
    ]
)
def array_stats11(aList, bList):
    """
    Array Stats
    """
    import numpy as np
    a = np.array(aList)
    b = np.array(bList)
    array1 = np.concatenate((a, b), axis=0)
    return array1.tolist()

# creating array from list with type float
@hops.component(
    "/array_list",
    name=("Array Stats"),
    description=("Array Stats"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("array1", "array1", "array1", access = hs.HopsParamAccess.LIST),
    ]
)
def array_stats111(aList):
    """
    Array Stats
    """
    import numpy as np
    a = np.array(aList)
    array1 = np.array(aList, dtype=np.float)
    return array1.tolist()

# numpy
# creating an array from three lists with type float
@hops.component(
    "/array_3lists",
    name=("Array Stats"),
    description=("Array Stats"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("cList", "cList", "cList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("array1", "array1", "array1", access = hs.HopsParamAccess.TREE),
    ]
)
def array_stats1111(aList, bList, cList):
    """
    Array Stats
    """
    import numpy as np
    a = np.array(aList)
    b = np.array(bList)
    c = np.array(cList)
    array1 = np.array([a, b, c], dtype=np.float)
    return array1.tolist()

# ONES AND ZEROS arrays in numpy
@hops.component(
    "/array_ones",
    name=("Array Stats"),
    description=("Array Stats"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("array1", "array1", "array1", access = hs.HopsParamAccess.LIST),
    ]
)
def array_stats1111(aList):
    """
    Array Stats
    """
    import numpy as np
    a = np.array(aList)
    array1 = np.ones(a.shape, dtype=np.float)
    return array1.tolist()

@hops.component(
    "/array_zeros",
    name=("Array Stats"),
    description=("Array Stats"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("array1", "array1", "array1", access = hs.HopsParamAccess.LIST),
    ]
)
def array_stats1111(aList):
    """
    Array Stats
    """
    import numpy as np
    a = np.array(aList)
    array1 = np.zeros(a.shape, dtype=np.float)
    return array1.tolist()

# full array in numpy
@hops.component(
    "/array_full",
    name=("Array Stats"),
    description=("Array Stats"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("array1", "array1", "array1", access = hs.HopsParamAccess.LIST),
    ]
)
def array_stats1111(aList, bList):
    """
    Array Stats
    """
    import numpy as np
    a = np.array(aList)
    b = np.array(bList)
    array1 = np.full(a.shape, b, dtype=np.float)
    return array1.tolist()


    

# + - * / numpy array operations
@hops.component(
    "/array_operations",
    name=("Array Operations"),
    description=("Array Operations"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("array_add", "array_add", "array_add", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("array_sub", "array_sub", "array_sub", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("array_mul", "array_mul", "array_mul", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("array_div", "array_div", "array_div", access = hs.HopsParamAccess.LIST),
    ]
)
def array_operations(aList, bList):
    """
    Array Operations
    """
    import numpy as np
    a = np.array(aList)
    b = np.array(bList)
    array_add = a + b
    array_sub = a - b
    array_mul = a * b
    array_div = a / b
    return array_add.tolist(), array_sub.tolist(), array_mul.tolist(), array_div.tolist()

#Lucky one
@hops.component(
    "/randarr55",
    name=("Random Array"),
    description=("Random Array"),
    category="algorithms",
    subcategory="sorting",
    inputs=[
        hs.HopsInteger("amount", "amount", "amount"),
        hs.HopsInteger("num", "Number", "number", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("array", "array", "array", access = hs.HopsParamAccess.LIST),
    ]
)
def random_array55(amount, num):
    """
    Random Array
    """
    import numpy as np
    arr = np.random.randint(0, amount, num)
    arr = arr.tolist()
    return arr

# conditional array searches in numpy
@hops.component(
    "/array_conditional",
    name=("Array Conditional"),
    description=("Array Conditional"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("array_conditional", "array_conditional", "array_conditional", access = hs.HopsParamAccess.LIST),
    ]
)
def array_conditional(aList, bList):
    """
    Array Conditional
    """
    import numpy as np
    a = np.array(aList)
    b = np.array(bList)
    array_conditional = np.where(a > b, a, b)
    return array_conditional.tolist()

# reshape array in numpy
@hops.component(
    "/array_reshape",
    name=("Array Reshape"),
    description=("Array Reshape"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("array_reshape", "array_reshape", "array_reshape", access = hs.HopsParamAccess.LIST),
    ]
)
def array_reshape(aList):
    """
    Array Reshape
    """
    import numpy as np
    a = np.array(aList)
    array_reshape = a.reshape(3, 3)
    return array_reshape.tolist()
    
# transpose array in numpy
@hops.component(
    "/array_transpose",
    name=("Array Transpose"),
    description=("Array Transpose"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("array_transpose", "array_transpose", "array_transpose", access = hs.HopsParamAccess.LIST),
    ]
)
def array_transpose(aList):
    """
    Array Transpose
    """
    import numpy as np
    a = np.array
    array_transpose = a.transpose(aList)
    return array_transpose.tolist()

"""
███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ██╗   ██╗                           
████╗  ██║██║   ██║████╗ ████║██╔══██╗╚██╗ ██╔╝                           
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝ ╚████╔╝                            
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔═══╝   ╚██╔╝                             
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║        ██║                              
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝                              
                                                                          
 ██████╗ ██████╗ ███╗   ██╗████████╗██╗███╗   ██╗██╗   ██╗███████╗██████╗ 
██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██║████╗  ██║██║   ██║██╔════╝██╔══██╗
██║     ██║   ██║██╔██╗ ██║   ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██║  ██║
██║     ██║   ██║██║╚██╗██║   ██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██║  ██║
╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║██║ ╚████║╚██████╔╝███████╗██████╔╝
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═════╝ 
"""

# Array creation using lists
# create array from list
@hops.component(
    "/array_from_listWS",
    name=("Array From List Part 2"),
    description=("Array From List Part 2"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("array_from_listPart2", "array_from_listPart2", "array_from_listPart2", access = hs.HopsParamAccess.LIST),
    ]
)
def array_from_listWS(aList):
    """
    Array From List Part 2
    """
    import numpy as np
    listOut = []
    arr = np.array(aList)
    for i in arr:
        print(i)
        listOut.append(i)
    return listOut

@hops.component(
    "/array_from_listWSb",
    name=("Array From List Part 2b"),
    description=("Array From List Part 2b"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("array_from_listPart2b", "array_from_listPart2b", "array_from_listPart2b", access = hs.HopsParamAccess.LIST),
    ]
)
def array_from_listWSb(aList):
    """
    Array From List Part 2b
    """
    import numpy as np
    arr = np.array(aList)
    for i in arr:
        print(i)
    print(arr)
    return aList

# create an array from 2 lists
@hops.component(
    "/_2lists9",
    name=("Array From List Part 3"),
    description=("Array From List Part 3"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
    ]
)
def _2lists9(aList, bList):
    """
    Array From List Part 3
    """
    import numpy as np
    arr = np.array([aList, bList])
    print(arr)
    print(arr.tolist())
    print(arr.tolist()[0])
    print(arr.tolist()[1])
    #print(arr.list_to_tree()) not working
    # use entwine node in gh to convert lists to tree
    return arr.tolist()[0], arr.tolist()[1]


# transpose array
# create an array from 2 lists
@hops.component(
    "/_2lists_Transpose",
    name=("Array From List Part 3"),
    description=("Array From List Part 3"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
    ]
)
def _2lists_Transpose(aList, bList):
    """
    Array From List Part 3
    """
    import numpy as np
    arr = np.array([aList, bList])
    arr = arr.transpose()
    print(arr)
    print(arr.tolist())
    print(arr.tolist()[0])
    print(arr.tolist()[1])
    #print(arr.list_to_tree()) not working in grasshopper canvas
    # use entwine node in gh to convert lists to tree
    return arr.tolist()[0], arr.tolist()[1]

# create an array from 3 lists
@hops.component(
    "/_3list_array",
    name=("Array From List Part 3"),
    description=("Array From List Part 3"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("cList", "cList", "cList", access = hs.HopsParamAccess.LIST),

    ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
    ]
)
def _3list_array(aList, bList, cList):
    """
    Array From List Part 3
    """
    import numpy as np
    arr = np.array([aList, bList, aList])
    #arr = arr.transpose()
    print(arr)
    print(arr.tolist())
    print(arr.tolist()[0])
    print(arr.tolist()[1])
    print(arr.tolist()[2])
    #print(arr.list_to_tree()) not working in grasshopper canvas
    # use entwine node in gh to convert lists to tree
    return arr.tolist()[0], arr.tolist()[1], arr.tolist()[2]

# create an array from 3 lists
@hops.component(
    "/_3list_transpose",
    name=("Array From List Part 3"),
    description=("Array From List Part 3"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("cList", "cList", "cList", access = hs.HopsParamAccess.LIST),

    ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
    ]
)
def _3list_transpose(aList, bList, cList):
    """
    Array From List Part 3
    """
    import numpy as np
    arr = np.array([aList, bList, cList])
    arr = arr.transpose()
    print(arr)
    print(arr.tolist())
    print(arr.tolist()[0])
    print(arr.tolist()[1])
    print(arr.tolist()[2])
    #print(arr.list_to_tree()) not working in grasshopper canvas
    # use entwine node in gh to convert lists to tree
    return arr.tolist()[0], arr.tolist()[1], arr.tolist()[2]

# reshape array
# create an array from 3 lists
@hops.component(
    "/_reshape3",
    name=("Array From List Part 3"),
    description=("Array From List Part 3"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("cList", "cList", "cList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST),
    ]
)
def _reshape3(aList, bList, cList):
    """
    Array From List Part 3
    """
    import numpy as np
    arr = np.array([aList, bList, cList])
    arr = arr.reshape(2,2,3)
    print(arr)
    print(arr.tolist())
    print(arr.tolist()[0][0])
    print(arr.tolist()[0][1])
    print(arr.tolist()[1][0])
    print(arr.tolist()[1][1])
    #print(arr.list_to_tree()) not working in grasshopper canvas
    # use entwine node in gh to convert lists to tree
    return arr.tolist()[0][0], arr.tolist()[0][1], arr.tolist()[1][0], arr.tolist()[1][1]

# flatten array
# create an array from 3 lists
@hops.component(
    "/_flatten2",
    name=("Array From List Part 3"),
    description=("Array From List Part 3"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("cList", "cList", "cList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
    ]
)
def _flatten2(aList, bList, cList):
    """
    Array From List Part 3
    """
    import numpy as np
    arr = np.array([aList, bList, aList])
    arr = arr.flatten()
    print(arr)
    print(arr.tolist())
    listOut = []
    for i in arr.tolist():
        print(i)
        listOut.append(i)
    return listOut


"""
██╗███╗   ██╗██████╗ ███████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
██║████╗  ██║██╔══██╗██╔════╝╚██╗██╔╝██║████╗  ██║██╔════╝ 
██║██╔██╗ ██║██║  ██║█████╗   ╚███╔╝ ██║██╔██╗ ██║██║  ███╗
██║██║╚██╗██║██║  ██║██╔══╝   ██╔██╗ ██║██║╚██╗██║██║   ██║
██║██║ ╚████║██████╔╝███████╗██╔╝ ██╗██║██║ ╚████║╚██████╔╝
╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                           
███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ██╗   ██╗            
████╗  ██║██║   ██║████╗ ████║██╔══██╗╚██╗ ██╔╝            
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝ ╚████╔╝             
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔═══╝   ╚██╔╝              
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║        ██║               
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝   

"""
# indexing array in numpy
@hops.component(
    "/_indexing2",
    name=("Array From List Part 3"),
    description=("Array From List Part 3"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("aList", "aList", "aList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("bList", "bList", "bList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("cList", "cList", "cList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("dList", "dList", "dList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("L0", "L0", "L0", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L1", "L1", "L1", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L2", "L2", "L2", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("L3", "L3", "L3", access = hs.HopsParamAccess.LIST),
    ]
)
def _indexing2(aList, bList, cList, dList):
    arr = np.array([aList, bList, cList, dList])
    print(arr)
    temp = arr[:2, ::2]
    # array with first 2 rows and alternative columns(0and2)
    print(temp)
    print(temp.tolist())
    print(temp.tolist()[0][0])
    print(temp.tolist()[0][1])
    print(temp.tolist()[1][0])
    print(temp.tolist()[1][1])
    #print(temp.list_to_tree()) not working in grasshopper canvas
    # use entwine node in gh to convert lists to tree
    return temp.tolist()[0][0], temp.tolist()[0][1], temp.tolist()[1][0], temp.tolist()[1][1]

# there is so much to do with numpy
# indexing
# cond is a booleaen array
# basic operations
# square
# modify array
# transpose
# min and max
# element wise operations
# matrix multiplication
# matrix division
# create an array of sin values
# create an array of cos values
# exponential and logarithmic value arrays
# square root and power arrays

# sorted array
# row-wise and column-wise sorted arrays
# merge sorted arrays
# put in values in sorted order
# find the index of a value in an array

"""
 █████╗ ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗██████╗     
██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗    
███████║██║  ██║██║   ██║███████║██╔██╗ ██║██║     █████╗  ██║  ██║    
██╔══██║██║  ██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔══╝  ██║  ██║    
██║  ██║██████╔╝ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗██████╔╝    
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝     
                                                                       
███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ██╗   ██╗                        
████╗  ██║██║   ██║████╗ ████║██╔══██╗╚██╗ ██╔╝                        
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝ ╚████╔╝                         
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔═══╝   ╚██╔╝                          
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║        ██║                           
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝  

"""
# numpy methods
# all, any, argmax, argmin, argsort, astype, average, byteswap, clip, compress, conj, copy, cumprod, cumsum, diagonal, dot, dump, dumps, empty, empty_like, expand_dims, fill, flatten, getfield, item, itemset, max, mean, min, nbytes, newbyteorder, nonzero, prod, put, ravel, repeat, reshape, resize, searchsorted, setfield, setflags, sort, squeeze, std, sum, swapaxes, take, tobytes, tofile
# transpose, trace, transpose, var, view, where, zeros, zeros_like,
# arange, array, asarray, ascontiguousarray, asfarray, asmatrix, asstrided,
# atleast_1d, atleast_2d, atleast_3d, broadcast, broadcast_arrays, broadcast_to,
# can_cast, compare_chararrays, concatenate, copyto, cross, cumproduct,
# dtype, empty_like, equal, eye, fill_diagonal, flags, flatiter, flatten,
# frombuffer, fromfile, fromiter, fromstring, getbuffer, getfield,
# inner, int_asbuffer, interp, is_busday, is_busdaycalendar, isclose,
# iscomplex, iscomplexobj, iscontiguous, isdatetime, isfortran,
# ishollow, ismasked, ismatrix, ismaskedarray, isne, issequence, issubclass_,
# issubdtype, isscalar, issubclass, item, itemset, itemsize, iterable,
# lexsort, mat, matrix, max, may_share_memory, mean, min, ndarray,
# nditer, ndim, newaxis, nonzero

@hops.component(
    "/_all3",
    name=("all"),
    description=("all"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("a", "a", "a", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("b", "b", "b", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("c", "c", "c", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("d", "d", "d", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsBoolean("all", "all", "all", access = hs.HopsParamAccess.LIST),
    ]
)
def _all3(a, b, c, d):
    arr = np.all([a, b, c, d])
    print(arr)
    return arr.tolist()

@hops.component(
    "/_any",
    name=("any"),
    description=("any"),
    category="numpy",
    subcategory="array",
    inputs=[
        hs.HopsNumber("a", "a", "a", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("b", "b", "b", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("c", "c", "c", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("d", "d", "d", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsBoolean("any", "any", "any", access = hs.HopsParamAccess.LIST),
    ]
)
def _any(a, b, c, d):
    arr = np.any([a, b, c, d])
    print(arr)
    return arr.tolist()






# """
# ███╗   ███╗ █████╗ ████████╗██████╗ ██╗      ██████╗ ████████╗██╗     ██╗██████╗ 
# ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║     ██╔═══██╗╚══██╔══╝██║     ██║██╔══██╗
# ██╔████╔██║███████║   ██║   ██████╔╝██║     ██║   ██║   ██║   ██║     ██║██████╔╝
# ██║╚██╔╝██║██╔══██║   ██║   ██╔═══╝ ██║     ██║   ██║   ██║   ██║     ██║██╔══██╗
# ██║ ╚═╝ ██║██║  ██║   ██║   ██║     ███████╗╚██████╔╝   ██║   ███████╗██║██████╔╝
# ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝╚═════╝ 
# """
# # matplotlib    and numpy for plotting

# # linear regrassion using least squares nethod
# # w1x + w2 = y
# # w1 = (x1 * y - x2 * y) / (x1^2 + x2^2)
# # x co-ordinates
# @hops.component(
#     "/linear_regression",
#     name=("Linear Regression"),
#     description=("Linear Regression"),
#     category="numpy",
#     subcategory="array",
#     inputs=[
#         hs.HopsNumber("xList", "xList", "xList", access = hs.HopsParamAccess.LIST),
#         hs.HopsNumber("yList", "yList", "yList", access = hs.HopsParamAccess.LIST),
#     ],
#     outputs=[
#         hs.HopsNumber("linear_regression", "linear_regression", "linear_regression", access = hs.HopsParamAccess.LIST),
#     ]
# )
# def linear_regression(xList, yList):
#     """
#     Linear Regression
#     """
#     import matplotlib.pyplot as plt
#     import numpy as np
#     x = np.array(xList)
#     y = np.array(yList)
#     x1 = x[0]
#     x2 = x[1]
#     y1 = y[0]
#     y2 = y[1]
#     w1 = (x1 * y1 - x2 * y2) / (x1**2 + x2**2)
#     w2 = (x1 * y2 - x2 * y1) / (x1**2 + x2**2)
#     linear_regression = [w1, w2]
#     return linear_regression    

# @hops.component(
#     "/linear_regression_plot",
#     name=("Linear Regression Plot"),
#     description=("Linear Regression Plot"),
#     category="numpy",
#     subcategory="array",
#     inputs=[
#         hs.HopsNumber("xList", "xList", "xList", access = hs.HopsParamAccess.LIST),
#         hs.HopsNumber("yList", "yList", "yList", access = hs.HopsParamAccess.LIST),
#     ],
#     outputs=[
#         hs.HopsBoolean("linear_regression_plot", "linear_regression_plot", "linear_regression_plot", access = hs.HopsParamAccess.LIST),
#     ]
# )
# def linear_regression_plot(xList, yList):
#     """
#     Linear Regression Plot
#     """
#     import matplotlib.pyplot as plt
#     import numpy as np
#     x = np.array(xList)
#     A = np.array([x, np.ones(len(x))])
#     # linearly generated sequence
#     y = np.array(yList)
#     # obtaining the parameters of the regression line
#     w = np.linalg.lstsq(A.T, y)[0]
#     # plotting the regression line
#     line = w[0] * x + w[1] # regression line
#     plt.plot(x, line, 'r-', label='Linear regression')
#     plt.plot(x, y, 'o', label='Original data')
#     plt.show()
#     return True

# # matplotlib functions for plotting
# @hops.component(
#     "/plot_scatter1",
#     name=("Plot Scatter"),
#     description=("Plot Scatter"),
#     category="numpy",
#     subcategory="array",
#     inputs=[
#         hs.HopsNumber("xList", "xList", "xList", access = hs.HopsParamAccess.LIST),
#         hs.HopsNumber("yList", "yList", "yList", access = hs.HopsParamAccess.LIST),
#     ],
#     outputs=[
#         hs.HopsBoolean("plot_scatter", "plot_scatter", "plot_scatter", access = hs.HopsParamAccess.LIST),
#     ]
# )
# def plot_scatter(xList, yList):

#     import matplotlib.pyplot as plt
#     import numpy as np
#     x = np.array(xList)
#     y = np.array(yList)
#     plt.scatter(x, y)
#     plt.show()
#     return True

# # matplotlib functions for plotting
# @hops.component(
#     "/plot_graph",
#     name=("Plot Graph"),
#     description=("Plot Graph"),
#     category="numpy",
#     subcategory="array",
#     inputs=[
#         hs.HopsNumber("xList", "xList", "xList", access = hs.HopsParamAccess.LIST),
#         hs.HopsNumber("yList", "yList", "yList", access = hs.HopsParamAccess.LIST),
#     ],
#     outputs=[
#         hs.HopsBoolean("plot_graph", "plot_graph", "plot_graph", access = hs.HopsParamAccess.LIST),
#     ]
# )
# def plot_graph(xList, yList):
    
#         import matplotlib.pyplot as plt
#         import numpy as np
#         x = np.array(xList)
#         y = np.array(yList)
#         plt.plot(x, y)
#         plt.show()
#         return True

# # bar graph for plotting matplotlib
# @hops.component(
#     "/plot_bar",
#     name=("Plot Bar"),
#     description=("Plot Bar"),
#     category="numpy",
#     subcategory="array",
#     inputs=[
#         hs.HopsNumber("xList", "xList", "xList", access = hs.HopsParamAccess.LIST),
#         hs.HopsNumber("yList", "yList", "yList", access = hs.HopsParamAccess.LIST),
#     ],
#     outputs=[
#         hs.HopsBoolean("plot_bar", "plot_bar", "plot_bar", access = hs.HopsParamAccess.LIST),
#     ]
# )
# def plot_bar(xList, yList):
        
#             import matplotlib.pyplot as plt
#             import numpy as np
#             x = np.array(xList)
#             y = np.array(yList)
#             plt.bar(x, y)
#             plt.show()
#             return True

# @hops.component(
#     "/plot_pie",
#     name=("Plot Pie"),
#     description=("Plot Pie"),
#     category="numpy",
#     subcategory="array",
#     inputs=[
#         hs.HopsNumber("xList", "xList", "xList", access = hs.HopsParamAccess.LIST),
#         hs.HopsNumber("yList", "yList", "yList", access = hs.HopsParamAccess.LIST),
#     ],
#     outputs=[
#         hs.HopsBoolean("plot_pie", "plot_pie", "plot_pie", access = hs.HopsParamAccess.LIST),
#     ]
# )
# def plot_pie(xList, yList):
#             import matplotlib.pyplot as plt
#             import numpy as np
#             x = np.array(xList)
#             y = np.array(yList)
#             plt.pie(y, labels=x)
#             plt.show()
#             return True

# @hops.component(
#     "/plot_donut",
#     name=("Plot Donut"),
#     description=("Plot Donut"),
#     category="numpy",
#     subcategory="array",
#     inputs=[
#         hs.HopsNumber("xList", "xList", "xList", access = hs.HopsParamAccess.LIST),
#         hs.HopsNumber("yList", "yList", "yList", access = hs.HopsParamAccess.LIST),
#     ],
#     outputs=[
#         hs.HopsBoolean("plot_donut", "plot_donut", "plot_donut", access = hs.HopsParamAccess.LIST),
#     ]
# )
# def plot_donut(xList, yList):
#             import matplotlib.pyplot as plt
#             import numpy as np
#             x = np.array(xList)
#             y = np.array(yList)
#             plt.pie(y, labels=x, autopct='%1.1f%%', startangle=90)
#             plt.show()
#             return True

# @hops.component(
#     "/plot_scatter_3d",
#     name=("Plot Scatter 3D"),
#     description=("Plot Scatter 3D"),
#     category="numpy",
#     subcategory="array",
#     inputs=[
#         hs.HopsNumber("xList", "xList", "xList", access = hs.HopsParamAccess.LIST),
#         hs.HopsNumber("yList", "yList", "yList", access = hs.HopsParamAccess.LIST),
#         hs.HopsNumber("zList", "zList", "zList", access = hs.HopsParamAccess.LIST),
#     ],
#     outputs=[
#         hs.HopsBoolean("plot_scatter_3d", "plot_scatter_3d", "plot_scatter_3d", access = hs.HopsParamAccess.LIST),
#     ]
# )
# def plot_scatter_3d(xList, yList, zList):
#             import matplotlib.pyplot as plt
#             import numpy as np
#             x = np.array(xList)
#             y = np.array(yList)
#             z = np.array(zList)
#             plt.scatter(x, y, z)
#             plt.show()
#             return True




"""
██████╗  █████╗ ███╗   ██╗██████╗  █████╗ ███████╗
██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔════╝
██████╔╝███████║██╔██╗ ██║██║  ██║███████║███████╗
██╔═══╝ ██╔══██║██║╚██╗██║██║  ██║██╔══██║╚════██║
██║     ██║  ██║██║ ╚████║██████╔╝██║  ██║███████║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚══════╝

"""
# Pandas in Python
# panda functions
# series and dataframe

@hops.component(
    "/panda_series",
    name=("Panda Series"),
    description=("Panda Series"),
    category="panda",
    subcategory="series",
    inputs=[
        hs.HopsNumber("xList", "xList", "xList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("panda_series", "panda_series", "panda_series", access = hs.HopsParamAccess.LIST),
    ]
)
def panda_series(xList):
    import pandas as pd
    x = pd.Series(xList)
    print(x)
    return x

@hops.component(
    "/panda_dataframe",
    name=("Panda Dataframe"),
    description=("Panda Dataframe"),
    category="panda",
    subcategory="dataframe",
    inputs=[
        hs.HopsNumber("xList", "xList", "xList", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("yList", "yList", "yList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("panda_dataframe", "panda_dataframe", "panda_dataframe", access = hs.HopsParamAccess.LIST),
    ]
)
def panda_dataframe(xList, yList):
    import pandas as pd
    x = pd.DataFrame(xList, yList)
    print(x)
    return x

# csv files for pandas
# panda methods
# read_csv
# read_excel
# read_json
# read_html
# read_sql


# index() - returns a new dataframe with the given index
@hops.component(
    "/panda_series_index",
    name=("Panda Series Index"),
    description=("Panda Series Index"),
    category="panda",
    subcategory="series",
    inputs=[
        hs.HopsNumber("xList", "xList", "xList", access = hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("panda_series", "panda_series", "panda_series", access = hs.HopsParamAccess.LIST),
    ]
)
def panda_series(xList):
    import pandas as pd
    x = pd.Series(xList)
    print(x)
    seriesOut = (x[:5])
    print(seriesOut)
    return seriesOut

# insert() - inserts a new row in the dataframe at the given index
# add() - adds a new row to the dataframe
# sub()
# mul()
# div()
# unique() - returns a new dataframe with the unique rows of the dataframe
# value_counts() - returns a new dataframe with the counts of each unique row of the dataframe
# columns() - returns a list of the columns in the dataframe
# isnull() - returns a new dataframe with the null values of the dataframe
# notnull() - returns a new dataframe with the non-null values of the dataframe
# between() - returns a new dataframe with the rows that are between the given values
# isin() - returns a new dataframe with the rows that are in the given list
# dtypes() - returns a list of the data types of the columns in the dataframe
# drop() - drops the given columns from the dataframe
# pop() - removes the given column from the dataframe and returns it
# sample() - returns a new dataframe with the given number of rows randomly sampled from the dataframe
# ndim() - returns the number of dimensions of the dataframe
# query() - returns a new dataframe with the rows that match the given query
# copy() - returns a copy of the dataframe
# drop_duplicates() - returns a new dataframe with the duplicate rows removed

# create a dataframe from a csv file using pandas
@hops.component(
    "/panda_dataframe_csv4",
    name=("Panda Dataframe CSV"),
    description=("Panda Dataframe CSV"),
    category="panda",
    subcategory="dataframe",
    inputs=[
        hs.HopsString("csvFile", "csvFile", "csvFile", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsNumber("panda_dataframe", "panda_dataframe", "panda_dataframe", access = hs.HopsParamAccess.LIST),
    ]
)   
def panda_dataframe4(csvFile):
    import pandas as pd
    x = pd.read_csv(csvFile)
    print(x)
    return x

# create a series from a csv file using pandas
@hops.component(
    "/series_csv4",
    name=("Panda Series CSV"),
    description=("Panda Series CSV"),
    category="panda",
    subcategory="series",
    inputs=[
        hs.HopsString("csvFile", "csvFile", "csvFile", access = hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("panda_series", "panda_series", "panda_series", access = hs.HopsParamAccess.LIST),
    ]
)
def series4(csvFile):
    import pandas as pd
    x = pd.read_csv(csvFile)
    print(x)
    listOut = []
    for i in x:
        print(x[i])
        listOut.append(x[i])
    return listOut




    # buffer = io.StringIO(csvFile)
    # loaded_df = pd.read_csv(buffer)
    # #(filepath_or_buffer=buffer, skipinitionalspace=True, lineterminator='@')
    # print(type(loaded_df))
    # print(loaded_df)
    # return loaded_df 

# create a dataframe from a csv file using pandas
# @hops.component(
#     "/panda_dataframe_csv9",
#     name=("Panda Dataframe CSV"),
#     description=("Panda Dataframe CSV"),
#     category="panda",
#     subcategory="dataframe",
#     inputs=[
#         hs.HopsString("csvFile", "csvFile", "csvFile", access = hs.HopsParamAccess.ITEM),
#     ],
#     outputs=[
#         hs.HopsString("panda_dataframe", "panda_dataframe", "panda_dataframe", access = hs.HopsParamAccess.ITEM),
#     ]
# )   
# def csv_to_df(df1):
#     """load df from a csv, with special line-"""
#     buffer = io.StringIO(df1)
#     loaded_df = pd.read_csv(filepath_or_buffer=buffer, skipinitionalspace=True, lineterminator='@')
#     return loaded_df 
    # The whenever you have done with you needed with your DF,
    # you need to convert it back to a csv, 
    # with the same custom separator
    #return the_actual_dataframe.to_csv(index=False, line_terminator='@')




# create a dataframe from a excel file using pandas
# create a dataframe from a json file using pandas
# create a dataframe from a html file using pandas
# create a dataframe from a sql file using pandas



"""\
█████╗ ███╗   ██╗████████╗ ██████╗ ██╗███╗   ██╗███████╗
██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗██║████╗  ██║██╔════╝
███████║██╔██╗ ██║   ██║   ██║   ██║██║██╔██╗ ██║█████╗  
██╔══██║██║╚██╗██║   ██║   ██║   ██║██║██║╚██╗██║██╔══╝  
██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║██║ ╚████║███████╗
╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
                                                         
███╗   ███╗ █████╗ ███████╗███████╗                      
████╗ ████║██╔══██╗██╔════╝██╔════╝                      
██╔████╔██║███████║█████╗  ███████╗                      
██║╚██╔╝██║██╔══██║██╔══╝  ╚════██║                      
██║ ╚═╝ ██║██║  ██║███████╗███████║                      
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝   
"""
# import pandas as pd

# #import all_graphs
# from utils import *

# @hops.component(
#     "/dt_to_df",
#     name="datatree to dataframe",
#     nickname="dtdf",
#     description="Converts any str,int,float datatree to a csv representation of a dataframe",
#     inputs=[
#         hs.HopsString("Data as tree", "Dt", "Data tree to convert", hs.HopsParamAccess.TREE),
#         hs.HopsString("Tree structure labels", "L", "List of the path labels (what the tree structure represent)",
#                       hs.HopsParamAccess.LIST),
#         hs.HopsString("Datatype", "D", "What does the data represent? Number of elements should match the number of"
#                                        "elements in each branches of the datatree", hs.HopsParamAccess.LIST),
#     ],
#     outputs=[
#         hs.HopsString("DfCSV", "Df", "Dataframe as a csv."
#                                      "\nNote that you might not be able to use panel on this output."),
#     ]
# )
# def better(data_tree: dict, path_labels: list, data_type: list):

#     if len(list(data_tree.keys())[0]) != len(data_type):
#         # THROW A WARNING !!
#         # Hops limitation. If needed, just print stuff, and keep checking terminal window
#         pass

#     clean_tree = clean_dict_datatype(data_tree)
#     renamed_key = temp_rename_dict(clean_tree)
#     temp_list = list_key_path(renamed_key)
#     partitioned = sub_lister(temp_list, len(path_labels))

#     transposed = list(map(lambda *a: list(a), *partitioned))

#     path_dict = label_dict(transposed, path_labels)
#     dict_list = dicts_for_datatypes(data_tree, data_type)
#     final_dict = dict_merger(path_dict, dict_list)
#     the_dataframe = pd.DataFrame.from_dict(final_dict)

#     # format incompatibility fix
#     the_actual_dataframe = fix_one_item_list(the_dataframe, data_type)

#     return the_actual_dataframe.to_csv(index=False, line_terminator='@')

# # ----------------------------------------------------------------------------------
"""
██████╗  █████╗ ████████╗ █████╗                                      
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗                                     
██║  ██║███████║   ██║   ███████║                                     
██║  ██║██╔══██║   ██║   ██╔══██║                                     
██████╔╝██║  ██║   ██║   ██║  ██║                                     
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝                                     
                                                                      
███████╗ ██████╗██╗███████╗███╗   ██╗ ██████╗███████╗                 
██╔════╝██╔════╝██║██╔════╝████╗  ██║██╔════╝██╔════╝                 
███████╗██║     ██║█████╗  ██╔██╗ ██║██║     █████╗                   
╚════██║██║     ██║██╔══╝  ██║╚██╗██║██║     ██╔══╝                   
███████║╚██████╗██║███████╗██║ ╚████║╚██████╗███████╗                 
╚══════╝ ╚═════╝╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝                 
                                                                      
██╗  ██╗    ██████╗ ██╗   ██╗███╗   ███╗███╗   ███╗██╗███████╗███████╗
██║  ██║    ██╔══██╗██║   ██║████╗ ████║████╗ ████║██║██╔════╝██╔════╝
███████║    ██║  ██║██║   ██║██╔████╔██║██╔████╔██║██║█████╗  ███████╗
╚════██║    ██║  ██║██║   ██║██║╚██╔╝██║██║╚██╔╝██║██║██╔══╝  ╚════██║
     ██║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║ ╚═╝ ██║██║███████╗███████║
     ╚═╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚═╝╚══════╝╚══════╝
"""
# working with real data
# manipulating data streams
# working with flat and unstructured files
# interacting with relational databases
# Using NoSQL as a data source
# interacting with web-based data
# working with data in the cloud

# real world data
# uploading, streaming, adn Sampling Data

# features and variables are columns
# cases or rows are observations
# data is stored in a table
# data is stored in a database
# data is stored in a file

# ----------------------------------------------------------------------------------

@hops.component(
    "/open_txt",
    description="Opens a text file",
    inputs=[
        hs.HopsString("File path", "F", "File path", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("File content", "C", "File content"),
    ]
)
def open_txt(file_path: str):
    with open(file_path, 'r') as f:
        return f.read()

@hops.component(
    "/open_txt_int",
    description="Opens a csv file",
    inputs=[
        hs.HopsString("File path", "F", "File path", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("count", "C", "Number of chars to read", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("File content", "C", "File content"),
    ]
)
def open_txt_int(file_path: str, count: int):
    with open(file_path, 'r') as f:
        return f.read(count)

# streaming large amounts of data into memory
@hops.component(
    "/open_txt_stream4",
    description="Opens a csv file",
    inputs=[
        hs.HopsString("File path", "F", "File path", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("File content", "C", "File content"),
    ]
)   
def open_txt_stream4(file_path: str):
    with open(file_path, 'r') as f:
        listOut = []
        for observation in f:
            print(observation)
            listOut.append(observation)
        return listOut

# generating variations on image data

# import matplotlib.image as image
# import matplotlib.pyplot as plt
# #%matplotlib inline

# @hops.component(
#     "/open_image3",
#     description="Opens a image file",
#     inputs=[
#         hs.HopsString("File path", "F", "File path", hs.HopsParamAccess.ITEM),
#     ],
#     outputs=[
#     ]
# )
# def open_image3(file_path: str):
#     shape = image.imread(file_path).shape
#     size = image.imread(file_path).size
#     image_show = plt.imshow(image.imread(file_path))
#     plt.show()
#     return image_show

# @hops.component(
#     "/open_image5",
#     description="Opens a image file",
#     inputs=[
#         hs.HopsString("File path", "F", "File path", hs.HopsParamAccess.ITEM),
#     ],
#     outputs=[
#         hs.HopsNumber("Shape", "Shape", "Shape", hs.HopsParamAccess.ITEM),
#         hs.HopsNumber("Size", "Size", "Size")
#     ],
# )
# def open_image5(file_path: str):
#     shape = image.imread(file_path).shape
#     size = image.imread(file_path).size
#     image_show = plt.imshow(image.imread(file_path))
#     plt.show()
#     return shape, size

#----------------------------------------------------------------------------------
#sampling data in different ways
@hops.component(
    "/open_txt_sample5",
    description="Opens a txt file",
    inputs=[
        hs.HopsString("File path", "F", "File path", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("File content", "C", "File content"),
    ]
)
def open_txt_sample5(file_path: str):
    with open(file_path, 'r') as f:
        listOut = []
        n = 2
        for i, observation in enumerate(f):
            if (i % n == 0):
                listOut.append(observation)
    return listOut

@hops.component(
    "/open_txt_mod",
    description="Opens a txt file",
    inputs=[
        hs.HopsString("File path", "F", "File path", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("mod", "M", "Modulo", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("File content", "C", "File content"),
    ]
)
def open_txt_mod(file_path: str, mod: int):
    with open(file_path, 'r') as f:
        listOut = []
        n = mod
        for i, observation in enumerate(f):
            if (i % n == 0):
                listOut.append(observation)
    return listOut

# random sampling
@hops.component(
    "/open_txt_random2",
    description="Opens a txt file",
    inputs=[
        hs.HopsString("File path", "F", "File path", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("prob", "P", "Probability", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("File content", "C", "File content"),
    ]
)
def open_txt_random2(file_path: str, prob: float):
    import random
    with open(file_path, 'r') as f:
        sample_size = prob
        listOut = []
        for i, observation in enumerate(f):
            if (random.random() < sample_size):
                print(observation)
                listOut.append(observation)
    return listOut


# Accessing Data in Structured Flat-File Form 
# read_table() with pandas
# read_csv() with pandas
# read_excel() with pandas
# read_json() with pandas
# read_html() with pandas
# read_sql() with pandas

@hops.component(
    "/read_table6",
    description="Reads a table",
    inputs=[
        hs.HopsString("File path", "F", "File path", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("Table", "T", "Table"),
    ]
)   
def read_table6(file_path: str):
    import pandas as pd
    #listOut = []
    color_table = pd.io.parsers.read_table(file_path)
    print(color_table)
    print(type(color_table))
    #listOut.append(color_table)
    return color_table
# what to do with a df in grasshopper string output? SEE read_csv_list2

# reading from a txt file
@hops.component(
    "/read_txt_file4D",
    description="Reads a txt file",
    inputs=[
        hs.HopsString("File path", "F", "File path", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("File content", "C", "File content"),
    ]
)
def read_txt_file4D(file_path: str):
    #listOut = []
    color_table = pd.io.parsers.read_table(file_path)
    print(color_table)
    print(type(color_table))
    #listOut.append(color_table)
    return color_table

# reading from a csv file
@hops.component(
    "/read_csv_list2",
    description="Reads a csv file",
    inputs=[
        hs.HopsString("File path", "F", "File path", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("File content", "C", "File content"),
    ]
)
def read_csv_list2(file_path: str):
    listOut = []
    titanic = pd.io.parsers.read_csv(file_path)
    #X = titanic[['age']]
    # simply change to this to output at list!!!!
    X = titanic[['age']].values
    print(X)
    print(type(X))
    X.tolist()
    print(X.tolist())
    print(type(X.tolist()))
    listOut.append(X.tolist())
    return listOut

@hops.component(
    "/read_csv_list4",
    description="Reads a csv file",
    inputs=[
        hs.HopsString("File path", "F", "File path", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("File content", "C", "File content"),
    ]
)
def read_csv_list4(file_path: str):
    listOut = []
    titanic = pd.io.parsers.read_csv(file_path)
    #X = titanic[['age']]
    # simply change to this to output at list!!!!
    X = titanic['age'].values
    print(X)
    print(type(X))
    X.tolist()
    print(X.tolist())
    print(type(X.tolist()))
    listOut.append(X.tolist())
    return listOut

# need to get rid of the string "'s for the HopsNumber output 
import xlrd
# Reading Excel and other Microsoft Office files
@hops.component(
    "/read_excel_list",
    description="Reads an excel file",
    inputs=[
        hs.HopsString("File path", "F", "File path", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("File content", "C", "File content"),
    ]
)
def read_excel_list(file_path: str):
    listOut = []
    xls = pd.ExcelFile(file_path)
    trig_values = xls.parse('Sheet1', index_col=None, na_values=['NA']).values # creates an array of the values in the sheet
    print(trig_values)
    print(type(trig_values))
    listOut.append(trig_values.tolist())
    return listOut

# Sending Data in Unstructured File Form
# http://scipy-lectures.org/packages/scikit-image/
# from skimage.io import imread
# save for a later date

#Managing Data from Relational Databases

# SQL
# The Structured Query Language:
# from sqalchemy import create_engine
# engine = create_engine('sqlite:///memory:')

# read_sql_table(): read a table from a database
# read_sql_query(): read a query from a database
# read_sql_frame(): read a query from a database
# read_sql(): read a query from a database
# DataFrame.to_sql(): write a DataFrame to a SQL database

# SQLite
# MySQL
# PostgreSQL
# SQL Server
# Other relational databases, such as Oracle, Microsoft SQL Server, etc.

# Interacting with Data from NoSQL Databases
# Other NoSQL databases, such as MongoDB, CouchDB, Redis, Cassandra, etc.
# MongoDB relies heavily on find() method

# Accessing Data from the Web
# web services and APIs
# jquery and other libraries

# XML and HTML
# XMLData.xml 
# use XMLData.xml file in the book

@hops.component(
    "/XMLDataCopy",
    description="XMLData.xml",
    inputs=[
        hs.HopsString("File path", "F", "File path", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("XMLData.xml", "X", "XMLData.xml"),
    ]
)
def XMLDataCopy(file_path: str):
    from lxml import objectify
    import pandas as pd

    xml = objectify.parse(open(file_path))
    root = xml.getroot()

    df = pd.DataFrame(columns=['Number', 'String', 'Boolean'])
    for i in range(0, 4):
        obj = root.getchildren()[i].getchildren()
        row = dict(zip(['Number', 'String', 'Boolean'], [obj[0].text, obj[1].text, obj[2].text]))
        row_s = pd.Series(row)
        row_s.name = i
        df = df.append(row_s)
       
    print(df)
    print(type(df))
    return df


@hops.component(
    "/XMLDataCopy5",
    description="XMLData.xml",
    inputs=[
        hs.HopsString("File path", "F", "File path", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsString("XMLData.xml", "X", "XMLData.xml"),
    ]
)
def XMLDataCopy5(file_path: str):
    from lxml import objectify
    import pandas as pd

    xml = objectify.parse(open(file_path))
    root = xml.getroot()

    df = pd.DataFrame(columns=['Number', 'String', 'Boolean'])
    for i in range(0, 4):
        obj = root.getchildren()[i].getchildren()
        row = dict(zip(['Number', 'String', 'Boolean'], [obj[0].text, obj[1].text, obj[2].text]))
        row_s = pd.Series(row)
        row_s.name = i
        df = df.append(row_s)
       
    print(df)
    print(type(df))
    df = df.values
    listOut = []
    print(df)
    print(type(df))
    df.tolist()
    print(df.tolist())
    print(type(df.tolist()))
    listOut.append(df.tolist())
    print(listOut)
    return listOut


# JSON

# Copnditioning your Data
# numpy and pandas

# It is all about the preparation of the data
# get the data 
# aggregate the data
# create data subsets
# clean the data
# develop a single dataset by merging various datasets together

# Validating Your Data

# gh plugin for data science
# Lunchbox plugin for data science




"""
██╗     ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗██████╗  ██████╗ ██╗  ██╗
██║     ██║   ██║████╗  ██║██╔════╝██║  ██║██╔══██╗██╔═══██╗╚██╗██╔╝
██║     ██║   ██║██╔██╗ ██║██║     ███████║██████╔╝██║   ██║ ╚███╔╝ 
██║     ██║   ██║██║╚██╗██║██║     ██╔══██║██╔══██╗██║   ██║ ██╔██╗ 
███████╗╚██████╔╝██║ ╚████║╚██████╗██║  ██║██████╔╝╚██████╔╝██╔╝ ██╗
╚══════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                    
██████╗ ██╗     ██╗   ██╗ ██████╗       ██╗███╗   ██╗               
██╔══██╗██║     ██║   ██║██╔════╝       ██║████╗  ██║               
██████╔╝██║     ██║   ██║██║  ███╗█████╗██║██╔██╗ ██║               
██╔═══╝ ██║     ██║   ██║██║   ██║╚════╝██║██║╚██╗██║               
██║     ███████╗╚██████╔╝╚██████╔╝      ██║██║ ╚████║               
╚═╝     ╚══════╝ ╚═════╝  ╚═════╝       ╚═╝╚═╝  ╚═══╝ 
"""




"""
███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗        
████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝        
██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗          
██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝          
██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗        
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝        
                                                                
██╗     ███████╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗ 
██║     ██╔════╝██╔══██╗██╔══██╗████╗  ██║██║████╗  ██║██╔════╝ 
██║     █████╗  ███████║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
██║     ██╔══╝  ██╔══██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║
███████╗███████╗██║  ██║██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
"""




if __name__ == "__main__":
    app.run(debug=True)
