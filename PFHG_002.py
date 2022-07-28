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