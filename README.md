# Advent-of-Code-2020
### Also my first repo.

Welcome to first my repository on Github. I am Anthei0774 and eager to show you my solutions for the international coding challenge, [Advent of Code](https://adventofcode.com/). I started this challenge in 2020 autumn when one my lecturers at the university recommended the group to participate. Since then, I had a great time, felt myself challenged while I was creating various algorithms to solve the daily problems. Without further ado, let us look into solutions.

### --- Day 1: Report Repair ---

**Part 1-2:**
It is an easy to read and solve problem just to warm up. With two nested loops on the indices *i, j* of the input, I found the two indices whose entries adds up to *2020*. With always starting *j = i + 1*, I never check the same pair as well. Part 2 uses three nested loops with *i, j, k* indices, and always starting with *j = i + 1, k = j + 1*, no triplets will repeat.

### --- Day 2: Password Philosophy ---

**Part 1-2:**
Still an easy problem to solve. After some minor formatting on the input, the Part 1 is done by using the built-in .count() method for string variables, checking if the occurences lie in the validity range. In Part 2, I had to subract 1 from the validity range, so the indexing will be proper, starting from 0, and with logic XOR = OR - AND, the solution is obtained.
