import unittest
from beziers.cubicbezier import CubicBezier
from beziers.line import Line
from beziers.point import Point
from beziers.path import BezierPath
from beziers.path.representations.Segment import SegmentRepresentation

class IntersectionMethods(unittest.TestCase):
  def test_cubic_line(self):
    q = CubicBezier(
      Point(100,240), Point(30,60), Point(210,230), Point(160,30))
    l = Line(Point(25,260), Point(230,20))
    path = BezierPath()
    path.closed = False
    path.activeRepresentation = SegmentRepresentation(path,[q])
    i = q.intersections(l)
    self.assertEqual(len(i),3)
    self.assertEqual(i[0],q.pointAtTime(0.117517031451))
    self.assertEqual(i[1],q.pointAtTime(0.518591792307))
    self.assertEqual(i[2],q.pointAtTime(0.867886610031))
    # print q.intersections(l)
    # import matplotlib.pyplot as plt
    # fig, ax = plt.subplots()
    # path.plot(ax)

    # path = BezierPath()
    # path.closed = False
    # path.activeRepresentation = SegmentRepresentation(path,[l])
    # path.plot(ax)

    # for n in q.intersections(l):
    #   circle = plt.Circle((n.x, n.y), 1, fill=False)
    #   ax.add_artist(circle)

    # plt.show()

  def test_cubic_cubic(self):
    # q1 = Bezier(10,100, 90,30, 40,140, 220,220)
    # q2 = Bezier(5,150, 180,20, 80,250, 210,190)
    # console.log(q1.intersects(q2))
    q1 = CubicBezier(
        Point(10,100), Point(90,30), Point(40,140), Point(220,220)
    )
    q2 = CubicBezier(
        Point(5,150), Point(180,20), Point(80,250), Point(210,190)
    )
    i = q1.intersections(q2)
    self.assertEqual(len(i),3)
    self.assertAlmostEqual(i[0].x,81.7904225873)
    self.assertAlmostEqual(i[0].y,109.899396337)
    self.assertAlmostEqual(i[1].x,133.186831292)
    self.assertAlmostEqual(i[1].y,167.148173322)
    self.assertAlmostEqual(i[2].x,179.869157678)
    self.assertAlmostEqual(i[2].y,199.661989162)