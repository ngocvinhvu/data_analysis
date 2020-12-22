#!/usr/bin/env python3


def solve(*args):
    """Return tổng (kiểu float) của các phân số trong args

    https://docs.python.org/3/library/fractions.html
    Thư viện fractions cung cấp class Fraction để tạo ra kiểu phân số trên
    Python.

    Tham khảo:
    http://www.familug.org/2017/03/python-fractions-tinh-toan-phan-so-tren.html
    """
    from fractions import Fraction as F

    result = 0
    for fraction in [*args]:
        result += F(fraction)

    return float(result)


def main():
    print(solve("1/10", "1/10", "1/10"))


# __name__ là một biến|name đặc biệt do Python tự tạo ra
# nó có giá trị là string "__main__" khi file được chạy bằng lệnh
# python filename.py
# và có giá trị là tên file (bỏ .py) khi được import.
if __name__ == "__main__":
    main()
