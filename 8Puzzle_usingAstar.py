import heapq

class EightPuzzle:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # Goal state of the puzzle

    def is_goal(self, state):
        return state == self.goal_state


    def right_move(self, state):
        state = list(state)
        i = state.index(0)
        temp = state[i]
        if i % 3 != 2:  # Check if blank space is not already at the rightmost position
            state[i] = state[i + 1]
            state[i + 1] = temp
        return tuple(state)

    def left_move(self, state):
        state = list(state)
        i = state.index(0)
        temp = state[i - 1]
        state[i - 1] = state[i]
        state[i] = temp
        return tuple(state)

    def up_move(self, state):
        state = list(state)
        i = state.index(0)
        temp = state[i - 3]
        state[i - 3] = state[i]
        state[i] = temp
        return tuple(state)

    def down_move(self, state):
        state = list(state)
        i = state.index(0)
        temp = state[i + 3]
        state[i + 3] = state[i]
        state[i] = temp
        return tuple(state)


    def get_neighbors(self, state):

        successors = []

        if state[0] == 0:
            successors.append(self.right_move(state))
            successors.append(self.down_move(state))

        elif state[1] == 0:
            successors.append(self.right_move(state))
            successors.append(self.down_move(state))
            successors.append(self.left_move(state))

        elif state[2] == 0:
            successors.append(self.left_move(state))
            successors.append(self.down_move(state))

        elif state[3] == 0:
           successors.append(self.up_move(state))
           successors.append(self.left_move(state))
           successors.append(self.down_move(state))

        elif state[4] == 0:
           successors.append(self.up_move(state))
           successors.append(self.left_move(state))
           successors.append(self.down_move(state))
           successors.append(self.right_move(state))

        elif state[5] == 0:
           successors.append(self.up_move(state))
           successors.append(self.right_move(state))
           successors.append(self.down_move(state))

        elif state[6] == 0:
          successors.append(self.up_move(state))
          successors.append(self.left_move(state))

        elif state[7] == 0:
          successors.append(self.up_move(state))
          successors.append(self.left_move(state))
          successors.append(self.right_move(state))

        elif state[8] == 0:
            successors.append(self.up_move(state))
            successors.append(self.right_move(state))

        return successors

    def manhattan_distance(self, state):
        distance = 0
        for i in range(9):
            if state[i] == 0:
                continue
            x, y = i % 3, i // 3
            gx, gy = (state[i] - 1) % 3, (state[i] - 1) // 3
            distance += abs(x - gx) + abs(y - gy)
        return distance

    def reconstruct_path(self, state, parent):
        path = [state]
        while parent[state] is not None:
            state = parent[state]
            path.append(state)
        path.reverse()
        return path

    def a_star(self):
        queue = [(self.manhattan_distance(self.initial_state), self.initial_state)]
        visited = set()
        parent = {self.initial_state: None}

        while queue:
            h_n, current_state = heapq.heappop(queue)

            if self.is_goal(current_state):
                return self.reconstruct_path(current_state, parent)

            visited.add(current_state)

            successors = self.get_neighbors(current_state)

            for successor in successors:
                if successor not in visited and successor not in parent:
                    g_n = len(self.reconstruct_path(current_state, parent))  # actual cost
                    h_n = self.manhattan_distance(successor)  #Heuristics
                    f_n = g_n + h_n  # Realistic estimated cost
                    heapq.heappush(queue, (f_n, successor))
                    parent[successor] = current_state

        return False

# Example usage:
# initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)  # Example of a scrambled puzzle (unsolvable state)
initial_state = (1, 2, 3, 4, 5, 0, 6, 7, 8) # solvable state
puzzle = EightPuzzle(initial_state)
solution = puzzle.a_star()

if solution:
    print("Solution found:")
    for state in solution:
        print(state)
else:
    print("No solution found.")
