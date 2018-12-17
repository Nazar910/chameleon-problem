import unittest
from depth_first_search import dfs
from state import State
from collections import deque

class TestDfs(unittest.TestCase):
    def test_result(self):
        result = dfs(State(red=13, blue=16, green=17))
        final_state = result['final_state']
        self.assertEqual(final_state.red_count, 0)
        self.assertEqual(final_state.green_count, 46)
        self.assertEqual(final_state.blue_count, 0)
        path = result['path']
        print('Path length: {}'.format(len(path)))
        print('Path')
        for p in result['path']:
            print(p)
        print('Full path length: {}'.format(len(result['full_path'])))

if __name__ == "__main__":
    unittest.main()
