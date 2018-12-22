class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        self.elements.append((priority, item))
        self.elements.sort(key=lambda elem: elem[0], reverse=True)

    def get(self):
        return self.elements.pop(0)[1]

from state import State
goal = State(red=0, green=46, blue=0)
def heuristic_to_goal(node):
    return abs(goal.red_count - node.red_count) \
     + abs(goal.blue_count - node.blue_count) \
     + abs(goal.green_count - node.green_count)

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start and current != None:
        path.append(current)
        current = came_from[str(current)]
    path.reverse()  # optional
    return path

from collections import deque

def a_star(state):
    queue = PriorityQueue()
    queue.put(state, 0)
    came_from = {}
    cost_so_far = {}
    came_from[str(state)] = None
    cost_so_far[str(state)] = 0

    full_path = []

    while not queue.empty():
        current = queue.get()
        full_path.append(str(current))

        if current.has_only_one_color():
            break

        neighbors = deque()
        if current.has_red_ones() and current.has_green_ones():
            neighbors.append(current.red_met_green())
        if current.has_blue_ones() and current.has_red_ones():
            neighbors.append(current.blue_met_red())
        if current.has_blue_ones() and current.has_green_ones():
            neighbors.append(current.green_met_blue())

        for next in neighbors:
            new_cost = cost_so_far[str(current)] + 1
            if str(next) not in cost_so_far or new_cost < cost_so_far[str(next)]:
                cost_so_far[str(next)] = new_cost
                priority = new_cost + heuristic_to_goal(next)
                queue.put(next, priority)
                came_from[str(next)] = str(current)
    return {
        'final_state': current,
        'full_path': full_path,
        'path': reconstruct_path(came_from, state, goal)
    }
