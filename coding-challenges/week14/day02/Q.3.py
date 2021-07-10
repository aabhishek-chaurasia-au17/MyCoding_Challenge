
"""
Q-3)All Paths From Source to Target (5
marks)
https://leetcode.com/problems/all-paths-from-source-to-target/
(Easy)
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all
possible paths from node 0 to node n - 1, and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from
node i (i.e., there is a directed edge from node i to node graph[i][j]).
Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
"""


class Solution:
    def allPathsSourceTarget(self, graph):
        
        mem=[ [] for i in range(len(graph))]
        self.util(0,graph,mem)
        return mem[0]
    
    def util(self,node,graph,mem):

        if len(mem[node])>0:
            return mem[node]

        if(node == len(graph)-1):
            return [[len(graph)-1]]

        for i in range(len(graph[node])):

            temp=self.util(graph[node][i],graph,mem)


            for pth in temp:
                mem[node].append([node]+pth)

        return mem[node]

