# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

def calculate_circle(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return circumference, area

def main():
    radius = float(input("請輸入圓的半徑："))
    circumference, area = calculate_circle(radius)
    print("圓周長為:", round(circumference, 2))
    print("圓面積為:", round(area, 2))

if __name__ == "__main__":
    main()