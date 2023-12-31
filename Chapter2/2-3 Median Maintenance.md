### 1. Download the following text file:

2-3 Median Maintenance.txt

The goal of this problem is to implement the "Med ian Maintenance" algorithm (covered in the Week 3 lecture on heap applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Letting **x i** denote the i th number of the file, the **k th** median **m k** is defined as the **median of the numbers x1, ... , Xk**. (So, if k is odd, then mk is ( (k + 1) / 2) th smallest number among X1, ... , Xk ; if k is even, then mk is the (k / 2) th smallest number among X1, ... , Xk. )

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That is, you shou ld compute (m1 + m2 + m3 + · · · + m10000) mod 10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations
of the algorithm.