# 1791. Find Center of Star Graph

There is an undirected star graph consisting of n nodes labeled from 1 to n. </br>
A star graph is a graph where there is one center node and exactly n - 1 </br>
edges that connect the center node with every other node. </br>

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates </br>
that there is an edge between the nodes ui and vi. Return the center of the given star graph. </br>

## Example 1:

Input: edges = [[1,2],[2,3],[4,2]] </br>
Output: 2 </br>
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center. </br>

## Example 2:

Input: edges = [[1,2],[5,1],[1,3],[1,4]] </br>
Output: 1 </br>

## Constraints:

3 <= n <= 105 </br>
edges.length == n - 1 </br>
edges[i].length == 2 </br>
1 <= ui, vi <= n </br>
ui != vi </br>
The given edges represent a valid star graph. </br>
