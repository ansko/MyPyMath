#!/usr/bin/env python3

import pprint
pprint=pprint.PrettyPrinter(indent=4).pprint


import mypymath
from mypymath.linalg import Vector
from mypymath.geometry.figures import (Point, Line, Segment, Plane, PolygonRegular,
                                       PrismRegular)
from mypymath.geometry.functions import AffinityChecker
from mypymath.geometry.functions import DistanceCalculator


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


def test_strs(debug_flag=True):
    pt = Point(1.5, 1.5, 1)
    pt8 = Point(1.5, 1.5, 1.5)
    pt0 = Point(1, 1, 1)
    pt1 = Point(1, 2, 1)
    pt2 = Point(2, 2, 1)
    pt3 = Point(2, 1, 1)
    pt4 = Point(1, 1, 2)
    pt5 = Point(1, 2, 2)
    pt6 = Point(2, 2, 2)
    pt7 = Point(2, 1, 2)
    line = Line(pt0, pt2)
    segment = Segment(pt0, pt2)
    segment1 = Segment(Point(0, 0, 1), Point(3, 3, 1))
    plane = Plane(pt0, pt1, pt2)
    polygon = PolygonRegular([pt0, pt1, pt2, pt3])
    polygon1 = PolygonRegular([Point(0, 0, 1), Point(0, 3, 1),
                               Point(3, 3, 1), Point(3, 0, 1)])
    polygon2 = PolygonRegular([Point(1.5, 1.5, 1.5), Point(1.5, 1.6, 1.5),
                               Point(1.6, 1.6, 1.5), Point(1.6, 1.5, 1.5)])
    top_facet = PolygonRegular([pt4, pt5, pt6, pt7])
    prism = PrismRegular(top_facet, polygon)
    if debug_flag:
        print(pt)
        print(line)
        print(segment)
        print(plane)
        print(polygon)
        print(prism)
    return 0

def test_affinity(debug_flag=True):
    pt = Point(1.5, 1.5, 1)
    pt8 = Point(1.5, 1.5, 1.5)
    pt0 = Point(1, 1, 1)
    pt1 = Point(1, 2, 1)
    pt2 = Point(2, 2, 1)
    pt3 = Point(2, 1, 1)
    pt4 = Point(1, 1, 2)
    pt5 = Point(1, 2, 2)
    pt6 = Point(2, 2, 2)
    pt7 = Point(2, 1, 2)
    line = Line(pt0, pt2)
    segment = Segment(pt0, pt2)
    segment1 = Segment(Point(0, 0, 1), Point(3, 3, 1))
    plane = Plane(pt0, pt1, pt2)
    polygon = PolygonRegular([pt0, pt1, pt2, pt3])
    polygon1 = PolygonRegular([Point(0, 0, 1), Point(0, 3, 1),
                               Point(3, 3, 1), Point(3, 0, 1)])
    polygon2 = PolygonRegular([Point(1.5, 1.5, 1.5), Point(1.5, 1.6, 1.5),
                               Point(1.6, 1.6, 1.5), Point(1.6, 1.5, 1.5)])
    top_facet = PolygonRegular([pt4, pt5, pt6, pt7])
    prism = PrismRegular(top_facet, polygon)
    prism1 = PrismRegular(PolygonRegular([Point(0, 0, 2),
                                          Point(0, 3, 2),
                                          Point(3, 3, 2),
                                          Point(3, 0, 2)]),
                          PolygonRegular([Point(0, 0, 1),
                                          Point(0, 3, 1),
                                          Point(3, 3, 1),
                                          Point(3, 0, 1)]))
    ac = AffinityChecker()
    if debug_flag:
        print()
        # point affinity
        print('\t', 'pt to line', ac.check(pt, line))                   # True
        print('\t', 'pt to segment', ac.check(pt, segment))             # True
        print('\t', 'pt to plane', ac.check(pt, plane))                 # True
        print('\t', 'pt to polygon', ac.check(pt, polygon))             # True
        print('\t', 'pt to prism', ac.check(pt8, prism))                # True
        # line affinity
        print('\t', 'line to plane', ac.check(line, plane))             # True
        # segment affinity
        print('\t', 'segment to line', ac.check(segment, line))         # True
        print('\t', 'segment to segment', ac.check(segment, segment1))  # True
        print('\t', 'segment to plane', ac.check(segment, plane))       # True
        print('\t', 'segment to polygon', ac.check(segment, polygon))   # True
        print('\t', 'segment to prism', ac.check(segment, prism))       # True
        # polygon affinity
        print('\t', 'polygon to plane', ac.check(polygon, plane))       # True
        print('\t', 'polygon to polygon', ac.check(polygon, polygon1))  # True
        print('\t', 'polygon to prism', ac.check(polygon2, prism))      # True
        # prism affinity
        print('\t', 'prism to prism', ac.check(prism, prism1))          # True

def test_distances(debug_flag=True):
    dc = DistanceCalculator()
    pt = Point(0, 0, 0)
    pt1 = Point(1, 1, 1)
    pt2 = Point(1, 2, 1)
    pt3 = Point(2, 2, 1)
    pt4 = Point(2, 1, 1)
    pt5 = Point(1, 1, 2)
    pt6 = Point(1, 2, 2)
    pt7 = Point(2, 2, 2)
    pt8 = Point(2, 1, 2)
    segment = Segment(pt1, pt2)
    line = Line(pt1, pt2)
    line1 = Line(pt5, pt6)
    line2 = Line(Point(0, 0, -1), Point(1, 1, -1))
    plane = Plane(pt1, pt2, pt3)
    plane1 = Plane(pt5, pt6, pt7)
    plane2 = Plane(Point(0, 0, -1), Point(0, 1, -1), Point(1, 0, -1))
    polygon = PolygonRegular([pt1, pt2, pt3, pt4])
    polygon1 = PolygonRegular([Point(1, 1, -1), Point(1, 2, -1),
                               Point(2, 2, -1), Point(2, 1, -1)])
    bottom_facet = PolygonRegular([pt5, pt6, pt7, pt8])
    prism = PrismRegular(polygon, bottom_facet)
    prism1 = PrismRegular(polygon.translated(Vector(0, 0, 10)),
                          polygon.translated(Vector(0, 0, 11)))
    segment1 = Segment(pt1, pt3)
    segment2 = Segment(pt2, pt4)
    segment3 = Segment(pt5, pt7)
    segment4 = Segment(Point(1, 1, -1), Point(1, 2, -1))
    if debug_flag:
        print()
        # pt-ANY
        print('pt-pt: ', dc.distance(pt, pt1))                    # 1.0
        print('pt-line: ', dc.distance(pt, line))                 # sqrt(2)
        print('pt-seg: ', dc.distance(pt, segment))               # sqrt(3)
        print('pt-plane: ', dc.distance(pt, plane))               # 1.0
        print('pt-poly: ', dc.distance(pt, polygon))              # sqrt(3)
        print('pt-prism: ', dc.distance(pt, prism))               # sqrt(3)
        # line-ANY
        print('line-pt: ', dc.distance(line, pt))                 # 1.0
        print('line-line, 0: ', dc.distance(line, line))          # 0.0
        print('line-line, 1: ', dc.distance(line, line1))         # 1.0
        print('line-seg: ', dc.distance(line1, segment))          # 1.0
        print('line-plane: ', dc.distance(line1, plane))          # 1.0
        print('line-poly: ', dc.distance(line1, polygon))         # 1.0
        print('line-prism, 0: ', dc.distance(line, prism))        # 0.0
        print('line-prism, 0: ', dc.distance(line2, prism))       # 2.0
        # segment-ANY
        print('segment-pt: ', dc.distance(segment, pt))           # sqrt(3)
        print('segment-line: ', dc.distance(segment, line))       # 0.0
        print('segment-line: ', dc.distance(segment, line1))      # 1.0
        print('segment-seg: ', dc.distance(segment1, segment2))   # 0.0
        print('segment-seg: ', dc.distance(segment, segment3))    # 1.0
        print('segment-plane: ', dc.distance(segment3, plane))    # 1.0
        print('segment-poly: ', dc.distance(segment3, polygon))   # 1.0
        print('segment-prism: ', dc.distance(segment4, prism))    # 2.0
        # plane-ANY
        print('plane-pt: ', dc.distance(plane, pt))               # 1.0
        print('plane-line ', dc.distance(plane, line1))           # 1.0
        print('plane-seg ', dc.distance(plane, segment4))         # 2.0
        print('plane-plane ', dc.distance(plane, plane))          # 0.0
        print('plane-plane ', dc.distance(plane, plane1))         # 1.0
        print('plane-poly ', dc.distance(plane1, polygon))        # 1.0
        print('plane-prism ', dc.distance(plane2, prism))         # 2.0
        # polygon-ANY
        print('polygon-pt: ', dc.distance(polygon, pt))                # sqrt(3)
        print('polygon-line: ', dc.distance(polygon, line1))           # 1.0
        print('polygon-seg: ', dc.distance(polygon, segment4))         # 2.0
        print('polygon-plane: ', dc.distance(polygon, plane2))         # 2.0
        print('polygon-polygon: ', dc.distance(polygon, polygon))      # 0.0
        print('polygon-polygon: ', dc.distance(polygon, bottom_facet)) # 1.0
        print('polygon-prism: ', dc.distance(polygon1, prism))         # 2.0
        # prism-ANY
        print('prism-pt ', dc.distance(prism, pt))                # sqrt(3)
        print('prism-line ', dc.distance(prism, line2))           # 2.0
        print('prism-seg ', dc.distance(prism, segment4))         # 2.0
        print('prism-plane ', dc.distance(prism, plane2))         # 2.0
        print('prism-polygon ', dc.distance(prism, polygon1))     # 2.0
        print('prism-prism, 0: ', dc.distance(prism, prism))      # 0.0
        print('prism-prism, 1: ', dc.distance(prism, prism1))     # 9.0


def test_everything_possible():
    debug_flag = True
    print('Testing inits:', end=' ')
    test_inits()
    print('ok')
    print('Testing __str__s:', end=' ')
    test_strs(debug_flag)
    print('ok')
    print('Testing AffinityChecker:', end=' ')
    test_affinity(debug_flag)
    print('ok')
    print('Testing DistanceCalculator:', end=' ')
    test_distances(debug_flag)
    print('ok')


test_everything_possible()
