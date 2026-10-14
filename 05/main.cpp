#include <iostream>
#include <cmath>

int main() {
    double ax, ay, bx, by, cx, cy;

    std::cin >> ax >> ay >> bx >> by >> cx >> cy;

    double abx = bx - ax;
    double aby = by - ay;
    double acx = cx - ax;
    double acy = cy - ay;

    double cross = abx * acy - aby * acx;
    const double eps = 1e-14;

    if (cross > eps) std::cout << "слева";
    else if (cross < -eps) std::cout << "справа";
    else std::cout << "на прямой";

    return 0;
}
