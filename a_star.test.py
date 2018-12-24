import unittest
from a_star import a_star
from state import State
from collections import deque

class TestBfs(unittest.TestCase):
    def test_result(self):
        print('=======================')
        print('A* algorithm')
        print('=======================')
        result = a_star(State(red=13, blue=16, green=17))
        final_state = result['final_state']
        self.assertEqual(final_state.red_count, 0)
        self.assertEqual(final_state.green_count, 46)
        self.assertEqual(final_state.blue_count, 0)
        full_path = result['full_path']
        print('Full path length: {}'.format(len(full_path)))
        self.assertEqual(len(full_path), 3295)
        path = result['path']
        print('Path length is {}'.format(len(path)))
        self.assertEqual(len(path), 17)
        i = 1
        for node in path:
            print('{}:{}'.format(i, node))
            i += 1

if __name__ == "__main__":
    unittest.main()
