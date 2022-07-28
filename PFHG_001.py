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


@hops.component(
    "/binmult",
    inputs=[hs.HopsNumber("A"), hs.HopsNumber("B")],
    outputs=[hs.HopsNumber("Multiply")],
)
def BinaryMultiply(a: float, b: float):
    return a * b

@hops.component(
    "/squares",
    inputs=[hs.HopsNumber("x"), hs.HopsNumber("y")],
    outputs=[hs.HopsNumber("Squares")],
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

"""
add = x + y
minus = x - y
times = x * y
divide = x / y
divideDown = x // y
modulus = x % y
negative = -x
castInt = int(3.9)
castFloat = float(x) #strange, works in output but not in castFloat output
print(x)
print(float(x))
exponent = x ** y
"""

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

"""
add = x + y
minus = x - y
times = x * y
divide = x / y
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


"""
divideDown = x // y
modulus = x % y
negative = -x
castInt = int(3.9)
castFloat = float(x) #strange, works in output but not in castFloat output
print(x)
print(float(x))
exponent = x ** y
"""


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