# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:41:59 2024

@author: student
"""

def main():
    # 讓用戶輸入姓名、年齡、身高和喜愛的顏色
    name = input("請輸入您的姓名：")
    age = int(input("請輸入您的年齡："))
    height = float(input("請輸入您的身高（米）："))
    favorite_color = input("請輸入您喜愛的顏色：")

    # 將資料存儲在字典中
    user_info = {
        "姓名": name,
        "年齡": age,
        "身高": height,
        "喜愛的顏色": favorite_color
    }

    # 格式化輸出摘要信息
    summary = "{}, {}歲, 身高{}米, 喜愛的顏色是{}。".format(
        user_info["姓名"], user_info["年齡"], user_info["身高"], user_info["喜愛的顏色"])

    print(summary)

if __name__ == "__main__":
    main()
