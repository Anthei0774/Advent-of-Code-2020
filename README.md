# Advent-of-Code-2020
### Also my first repo.

Welcome to first my repository on Github. I am Anthei0774 and eager to show you my solutions for the international coding challenge, [Advent of Code](https://adventofcode.com/). I started this challenge in 2020 autumn when one my lecturers at the university recommended the group to participate. Since then, I had a great time, felt myself challenged while I was creating various algorithms to solve the daily problems. Without further ado, let us look into solutions.

### --- Day 1: Report Repair ---

**Part 1:**
It is an easy to read and solve problem just to warm up. With two nested loops on the indices *i, j* of the input, I found the two indices whose entries adds up to *2020*. With always starting *j = i + 1*, we never check the same pair as well.

**Part 2:**
Straightforward as before, using three nested loops with *i, j, k* indices, and always starting with *j = i + 1, k = j + 1*, so no triplets will repeat.
