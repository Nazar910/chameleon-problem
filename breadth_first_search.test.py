import unittest
from breadth_first_search import bfs
from state import State
from collections import deque

class TestBfs(unittest.TestCase):
    def test_result(self):
        result = bfs(State(red=13, blue=16, green=17))
        final_state = result['final_state']
        self.assertEqual(final_state.red_count, 0)
        self.assertEqual(final_state.green_count, 46)
        self.assertEqual(final_state.blue_count, 0)
        print('Visited elems: {}'.format(len(result['visited'])))

if __name__ == "__main__":
    unittest.main()
