spiral = {}
spiral[(0,0)] = 1
# positions to check around the number
NEIGHBORS = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
DIRECTION = [(1,0), (0,1), (-1,0), (0,-1)] # Right Up Left Down

n = int(input("Type number: "))

def spiral_until_at_least(n):
    spiral = {}               # Spiral dictionary
    spiral[(0,0)] = 1
    x,y = 0,0
    steps_in_row = 1          # times spiral extends in same direction
    second_direction = False  # spiral extends in same direction twice: False if first leg, True if second
    nstep = 0                 # number of steps in current direction
    step_direction = 0        # index of direction in DIRECTION
    
    while True:
        dx, dy = DIRECTION[step_direction]  # coords of next step 
        x, y = x + dx, y + dy   # coords of the next number
        total = 0
        for neighbor in NEIGHBORS:      # loop for checking the surrounding of number
            nx, ny = neighbor
            if (x+nx, y+ny) in spiral:
                total += spiral[(x+nx, y+ny)]
                
        print("X: {}, Y:{}, Total:{}".format(x,y,total))
        
        if total > n:
            return total
        spiral[(x,y)] = total   # adding step to dictionary
        nstep += 1 # adding step 
        if nstep == steps_in_row:   # condition if there is another step in given row
                                    # it is working for 2 walls, as scheme is
                                    # RULLDDRRRUUULLLL... etc.
            nstep = 0
            step_direction = (step_direction + 1)% 4
            if second_direction:
                second_direction = False
                steps_in_row += 1
            else:
                second_direction = True

spiral_until_at_least(n)