class EightPuzzle:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # Goal state of the puzzle

    def is_goal(self, state):
        return state == self.goal_state

    def right_move(self, state):
        state = list(state)
        i = state.index(0)
        if i % 3 != 2:  # Check if blank space is not already at the rightmost position
            state[i], state[i + 1] = state[i + 1], state[i]
        return tuple(state)

    def left_move(self, state):
        state = list(state)
        i = state.index(0)
        if i % 3 != 0:  # Check if blank space is not already at the leftmost position
            state[i], state[i - 1] = state[i - 1], state[i]
        return tuple(state)

    def up_move(self, state):
        state = list(state)
        i = state.index(0)
        if i >= 3:  # Check if blank space is not already at the topmost position
            state[i], state[i - 3] = state[i - 3], state[i]
        return tuple(state)

    def down_move(self, state):
        state = list(state)
        i = state.index(0)
        if i <= 5:  # Check if blank space is not already at the bottommost position
            state[i], state[i + 3] = state[i + 3], state[i]
        return tuple(state)

    def get_neighbors(self, state):
        neighbors = []
        for move in [self.right_move, self.left_move, self.up_move, self.down_move]:
            new_state = move(state)
            if new_state != state:  # Ensure a valid move was made
                neighbors.append(new_state)
        return neighbors

    def manhattan_distance(self, state):
        distance = 0
        for i in range(9):
            if state[i] == 0:
                continue
            x, y = i % 3, i // 3
            gx, gy = (state[i] - 1) % 3, (state[i] - 1) // 3
            distance += abs(x - gx) + abs(y - gy)
        return distance

    def hill_climbing(self):
        current_state = self.initial_state
        while True:
            if self.is_goal(current_state):
                return current_state  # Found goal state
            neighbors = self.get_neighbors(current_state)
            if not neighbors:
                return False  # No valid moves left
            next_state = min(neighbors, key=self.manhattan_distance)
            if self.manhattan_distance(next_state) >= self.manhattan_distance(current_state):
                return False  # No improvement
            current_state = next_state

# Example usage:
#initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)  # Example of a scrambled puzzle (unsolvable state)
initial_state = (1, 2, 3, 4, 5, 6, 7, 0, 8) # Solvable state
puzzle = EightPuzzle(initial_state)
solution = puzzle.hill_climbing()

if solution:
    print("Solution found:")
    print(solution)
else:
    print("No solution found.")
