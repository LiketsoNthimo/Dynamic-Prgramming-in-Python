# Dynamic-Programming-in-Python

## Background
Last year (2021), I encountered a problem that required me to learn dynamic programming, and I was lucky enough to come across a comprehensive tutorial on YouTube on the [freeCodeCamp.org](https://www.youtube.com/c/Freecodecamp) channel. The course is 5 hours and 10 minutes long, but it took me over 20 hours to complete because I had decided to code the functions myself after each tutorial, before viewing the instructor's code. The instructor uses JavaScript therefore, I opted to create python versions for future reference.

## Overview
The dynamic programming approaches covered are Memoization and Tabulation. 

## Layout
The repository contains a folder for each problem type. Each folder contains two python files, one for each approach. Some files may contain more than one function where I decided to keep my solution before appending the lecture solution.

### The problems covered are:
* Fibonacci
* GridTraveler
* CanSum
* HowSum
* BestSum
* CanConstruct
* CountConstruct
* AllConstruct

## Summary
### [Memoization recipe](https://www.youtube.com/watch?v=oBt53YbR9Kk&t=3892s)
1. Make it work
* Visualise the problem as a tree
* Implement the tree using recursion
* Test it

2. Make it efficient
* Add a memo object
* Add a base case to return memo values
* Store return values into the memo

### [Tabulation recipe](https://www.youtube.com/watch?v=oBt53YbR9Kk&t=12872s)
* Visualise the problem as a table
* Size the table based on the inputs
* Initialise the table with default values
* Seed the trivial answer into the table
* Iterate through the table
* Fill further positions based on the current position

## Acknowledgements
* [Dynamic Programming - Learn to Solve Algorithmic Problems & Coding Challenges](https://www.youtube.com/watch?v=oBt53YbR9Kk&t=1777s)
