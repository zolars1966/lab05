#include <iostream>
#include <cmath>

int main() {
    double a, b, c, d;
    std::cin >> a >> b >> c >> d;

    const double eps = 1e-12;
    double x = a + b;
    double y = c + d;

    if (x - y > eps) std::cout << 1;
    else if (y - x > eps) std::cout << -1;
    else std::cout << 0;

    return 0;
}