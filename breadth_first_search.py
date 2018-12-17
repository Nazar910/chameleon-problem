from state import State
from collections import deque

def bfs(state):
    visited = set([str(state)])
    stack = deque([state])
    full_path = []
    while len(stack) and not state.has_only_one_color():
        state = stack.popleft()
        full_path.append(state)
        if state.has_red_ones() and state.has_green_ones() and str(state.red_met_green()) not in visited:
            stack.append(state.red_met_green())
        if state.has_blue_ones() and state.has_red_ones() and str(state.blue_met_red()) not in visited:
            stack.append(state.blue_met_red())
        if state.has_blue_ones() and state.has_green_ones() and str(state.green_met_blue()) not in visited:
            stack.append(state.green_met_blue())
        visited.add(str(state))
    return {
        'final_state': state,
        'visited': visited,
        'full_path': full_path,
        'path': state.get_path()
    }
