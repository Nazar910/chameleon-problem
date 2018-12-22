from collections import deque

def dfs(state):
    prev_states = deque()
    visited = set()
    full_path = []
    i = 0
    while state is not None and not state.has_only_one_color():
        full_path.append(str(state))
        if state.has_red_ones() and state.has_green_ones() and str(state.red_met_green()) not in visited:
            new_state = state.red_met_green()
        elif state.has_blue_ones() and state.has_red_ones() and str(state.blue_met_red()) not in visited:
            new_state = state.blue_met_red()
        elif state.has_blue_ones() and state.has_green_ones() and str(state.green_met_blue()) not in visited:
            new_state = state.green_met_blue()
        else:
            state = prev_states.pop()
            print('Going one step back')
            continue
        prev_states.append(state)
        print('{}:{}'.format(i, state))
        i += 1
        state = new_state
        visited.add(str(new_state))
    print('Final state is {}:{}'.format(i, state))
    return {
        'final_state': state,
        'visited': visited,
        'path': state.get_path(),
        'full_path': full_path
    }
