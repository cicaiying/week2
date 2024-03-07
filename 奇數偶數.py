# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:47:54 2024

@author: student
"""

def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def main():
    number = int(input("請輸入一個整數："))
    if check_even(number):
        print(number, "是一個偶數。")
    else:
        print(number, "不是一個偶數。")

if __name__ == "__main__":
    main()