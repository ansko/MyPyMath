#!/usr/bin/env python3

import pprint
pprint=pprint.PrettyPrinter(indent=4).pprint


import mypymath
from mypymath.linalg import Vector
from mypymath.geometry.figures import (Point, Line, Segment, Plane, PolygonRegular,
                                       PrismRegular)
#from mypymath.geometry.functions import DistanceCalculator


def test_inits():
    # vec inits: from 3 floats/ints +
    vec = Vector(1, 1.0, 1)
    # point inits: from pt +
    #              from vec +
    #              from 3 floats/ints +
    pt1 = Point(0, 0, 0)
    pt2 = Point(1, 0, 0)
    pt3 = Point(0, 1, 0)
    pt4 = Point(1, 1, 0)
    pt5 = Point(0, 0, 1)
    pt6 = Point(1, 0, 1)
    pt7 = Point(0, 1, 1)
    pt8 = Point(1, 1, 1)
    pt9 = Point(vec)
    pt10 = Point(1, 1.0, 1.0)
    # line inits: from 2 pts +
    #             from seg +
    #             from pt, vec +
    line = Line(pt1, pt2)
    segment1 = Segment(pt1, pt2)
    line3 = Line(segment1)
    line1 = Line(pt1, vec)
    # segment inits: from 2 pts +
    #                from vec +
    #                from 3 floats/ints +
    segment = Segment(pt1, pt2)
    segment3 = Segment(vec)
    segment4 = Segment(1.0, 1, 1.0)
    # plane inits: from 3 pts +
    #              from pt, vec +
    #              from 4 floats/ints +
    #              from 2 vecs +
    #              from 2 segs +
    #              from 2 lines -
    #              from vec / seg / line and vec / seg / line seem to be +
    plane = Plane(pt1, pt2, pt3)
    plane1 = Plane(1, 1.0, 1, 1)
    plane2 = Plane(pt1, vec)
    vec1 = Vector(2, 2, 0)
    plane3 = Plane(vec, vec1)
    plane4 = Plane(segment, segment4)
    plane5 = Plane(line1, line3)
    plane6 = Plane(vec1, line1)
    plane7 = Plane(vec1, segment3)
    # PolygonRegular inits: from vertices +
    polygon = PolygonRegular([pt1, pt2, pt3, pt4])
    polygon1 = PolygonRegular([pt5, pt6, pt7, pt8])
    # PrismRegular intis
    prism = PrismRegular(polygon, polygon1)


test_inits()
