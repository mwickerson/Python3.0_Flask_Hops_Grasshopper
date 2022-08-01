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
        hs.HopsString("Endswith", "Endswith", "A.endswith('content...')"),
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
\n new line
\s new space
\t new tab
a = "    This is lazy\t\n    "
b = a.strip()
c = x.lower()
d = y.upper()
e = "smartphone".startswith("smart")
f = "smartphone".endswith("phone")
g = "another".find("other")
h = "cheat".replace("ch", "m")
i = ",".join(["F", "B", "I"])
k = "ear" in "earth"
l = len(A)
m = len(B)
n = A.split(" ")
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
    "/curve_end_points",
    name="EndPoints",
    nickname="EndPoints",
    description="Get curve start/end points",
    icon="beamupUserObjects/icons/bmd_level.png",
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
    return (end, start)
    #return (end, start, {"{0}": end.X, "{1}": start.X})


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


if __name__ == "__main__":
    app.run(debug=True)