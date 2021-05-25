'''
Intuition here is that the robot will either return to (0,0) position or will change the direction (not North) if it has to be bound
in a circle. We determine the distacne travelled and the direction vector.

    north = 0, east = 1, south = 2, west = 3

Now everything is ready to iterate over the instructions.

    If the current instruction is R, i.e. to turn on the right, the next direction is idx = (idx + 1) % 4. 
    Modulo here is needed to deal with the situation - facing west, idx = 3, turn to the right to face north, idx = 0.

    If the current instruction is L, i.e. to turn on the left, the next direction could written in a symmetric way 
    idx = (idx - 1) % 4. That means we have to deal with negative indices. A more simple way is to notice that 1 turn 
    to the left = 3 turns to the right: idx = (idx + 3) % 4.

    If the current instruction is to move, we simply update the coordinates: x += directions[idx][0], y += directions[idx][1].

    After one cycle we have everything to decide. It's a limit cycle trajectory if the robot is back to 
    the center: x = y = 0 or if the robot doesn't face north: idx != 0.

'''

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        idx = 0
        x = y = 0
        for i in instructions:
            if i == 'L':
                idx = (idx+3) % 4
            elif i == 'R':
                idx = (idx+1) % 4
            else:
                x += direction[idx][0]
                y += direction[idx][1]
        return (x==0 and y==0) or idx != 0
        