#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 23 10:40:22 2025

@author: rivka
"""

import cv2
import time
import numpy as np



print(cv2.__version__)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Can't open camera")
    cap.release()
    exit(255)

while True:
    ret, img = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break    
    
    
    result = img.copy()
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0,81,0])
    upper = np.array([6,255,255])
    mask = cv2.inRange(img, lower, upper)
    result = cv2.bitwise_and(result, result, mask=mask)
    
    
    cv2.imshow("Original", img)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.waitKey()    
    cv2.destroyAllWindows()
    cap.release()
