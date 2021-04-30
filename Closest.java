import java.awt.geom.Point2D;
import java.util.*;

class Point extends Point2D.Double {
  public Point(double x, double y) { super(x, y); }
}

class Closest {
  static double dist(List<Point> points) {
    double inf = Double.POSITIVE_INFINITY;
    double h = inf;
    int tail = 0;
    Point[] Lx = points.toArray(new Point[0]);
    Arrays.sort(Lx, (a, b) -> Double.valueOf(a.x).compareTo(b.x));
    SortedSet<Point> Ly = new TreeSet<Point>((a, b) -> a.y < b.y ? -1 : a.y > b.y ? 1 : Double.valueOf(a.x).compareTo(b.x));
    for (Point p: Lx) {
      while (Lx[tail].x < p.x - h) {
        Ly.remove(Lx[tail++]);
      }
      SortedSet<Point> range = Ly.subSet(
          new Point(-inf, p.y - h),
          new Point( inf, p.y + h));
      for (Point c: range) {
        h = Math.min(h, p.distance(c));
      }
      Ly.add(p);
    }
    return h;
  }

  public static void main(String[] args) {
    List<Point> L = new ArrayList<>();
    L.add(new Point(0, 0));
    L.add(new Point(0, 2));
    L.add(new Point(2, 2));
    L.add(new Point(0, 3.5));
    L.add(new Point(2, 0));
    System.out.println(dist(L));
  }

}
