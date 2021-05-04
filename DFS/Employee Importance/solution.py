'''
DFS
Let's use a hashmap emap = {employee.id -> employee} to query employees quickly.

Now to find the total importance of an employee, it will be the importance of that employee, 
plus the total importance of each of that employee's subordinates. This is a straightforward 
depth-first search.

Time Complexity: O(N) where N is the number of employees. We might query each employee in dfs.
Space Complexity: O(N), the size of the implicit call stack when evaluating dfs.
'''

'''
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
'''

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emap = {e.id: e for e in employees}
        print(emap.values())
        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
        return dfs(id)
