# Python-Number-Guessing-Game
Python implementation of the Bisection Algorithm applied to a Number Guessing Game. 
# Number Guessing Game (Bisection Algorithm) 

A Python command-line application that demonstrates the **Bisection Algorithm** (Interval Halving method). The computer attempts to guess a user's number by systematically dividing the search interval.

##  About The Project
This project is part of the practical coursework for the **Mahara Tech (مهارة تك)** platform. 
It serves as a practical implementation of the **Bisection Algorithm**, commonly used in numerical analysis to find roots or target values within a given range.

## The Logic (Bisection Method)
The script applies the mathematical concept of interval halving:
1.  Define an interval `[Low, High]`.
2.  Calculate the midpoint: `Medium = (Low + High) // 2`.
3.  Based on user feedback, eliminate half of the interval:
    * If the target is **Higher**, the new interval becomes `[Medium, High]`.
    * If the target is **Lower**, the new interval becomes `[Low, Medium]`.
4.  Repeat until the target is found.

## Technologies
- **Python 3.14.2**
- **Control Flow:** Loops & Conditionals

 # Follow me [linkedIn](https://www.linkedin.com/in/khaled-elbadawy).
   
