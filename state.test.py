import unittest
from state import State

class TestState(unittest.TestCase):
    def test_constructor(self):
        state = State(red=13, green=16, blue=17)
        self.assertEqual(state.red_count, 13)
        self.assertEqual(state.green_count, 16)
        self.assertEqual(state.blue_count, 17)

    def test_has_red_ones(self):
        state = State(red=13, green=16, blue=17)
        self.assertTrue(state.has_red_ones())
    def test_has_red_ones_count_equals_0(self):
        state = State(red=0, green=16, blue=17)
        self.assertFalse(state.has_red_ones())
    def test_has_only_red_ones(self):
        state = State(red=16, green=0, blue=0)
        self.assertTrue(state.has_only_red_ones())
    def test_has_only_red_ones_false(self):
        state = State(red=13, green=16, blue=17)
        self.assertFalse(state.has_only_red_ones())
    def test_has_only_one_color_red(self):
        state = State(red=16, green=0, blue=0)
        self.assertTrue(state.has_only_one_color())

    def test_has_green_ones(self):
        state = State(red=13, green=16, blue=17)
        self.assertTrue(state.has_green_ones())
    def test_has_green_ones_count_equals_0(self):
        state = State(red=13, green=0, blue=17)
        self.assertFalse(state.has_green_ones())
    def test_has_only_green_ones(self):
        state = State(red=0, green=16, blue=0)
        self.assertTrue(state.has_only_green_ones())
    def test_has_only_green_ones_false(self):
        state = State(red=13, green=16, blue=17)
        self.assertFalse(state.has_only_green_ones())
    def test_has_only_one_color_green(self):
        state = State(red=0, green=16, blue=0)
        self.assertTrue(state.has_only_one_color())

    def test_has_blue_ones(self):
        state = State(red=13, green=16, blue=17)
        self.assertTrue(state.has_blue_ones())
    def test_has_blue_ones_count_equals_0(self):
        state = State(red=13, green=16, blue=0)
        self.assertFalse(state.has_blue_ones())
    def test_has_only_blue_ones(self):
        state = State(red=0, green=0, blue=16)
        self.assertTrue(state.has_only_blue_ones())
    def test_has_only_blue_ones_false(self):
        state = State(red=13, green=16, blue=17 )
        self.assertFalse(state.has_only_blue_ones())
    def test_has_only_one_color_blue(self):
        state = State(red=0, green=0, blue=16)
        self.assertTrue(state.has_only_one_color())

    def test_red_met_green(self):
        state = State(red=10, green=10, blue=10)
        new_state = state.red_met_green()
        self.assertEqual(new_state.red_count, 9)
        self.assertEqual(new_state.green_count, 9)
        self.assertEqual(new_state.blue_count, 12)
        self.assertEqual(new_state.parent, state)
    def test_red_met_green_exception_red_less_than_1(self):
        state = State(red=0, green=10, blue=10)
        self.assertRaises(Exception, state.red_met_green)
    def test_red_met_green_exception_green_less_than_1(self):
        state = State(red=10, green=0, blue=10)
        self.assertRaises(Exception, state.red_met_green)

    def test_green_met_blue(self):
        state = State(red=10, green=10, blue=10)
        new_state = state.green_met_blue()
        self.assertEqual(new_state.red_count, 12)
        self.assertEqual(new_state.green_count, 9)
        self.assertEqual(new_state.blue_count, 9)
        self.assertEqual(new_state.parent, state)
    def test_green_met_blue_exception_green_less_than_1(self):
        state = State(red=10, green=0, blue=10)
        self.assertRaises(Exception, state.green_met_blue)
    def test_green_met_blue_exception_blue_less_than_1(self):
        state = State(red=10, green=10, blue=0)
        self.assertRaises(Exception, state.green_met_blue)

    def test_blue_met_red(self):
        state = State(red=10, green=10, blue=10)
        new_state = state.blue_met_red()
        self.assertEqual(new_state.red_count, 9)
        self.assertEqual(new_state.green_count, 12)
        self.assertEqual(new_state.blue_count, 9)
        self.assertEqual(new_state.parent, state)

    def test_blue_met_red_exception_red_less_than_1(self):
        state = State(red=0, green=10, blue=10)
        self.assertRaises(Exception, state.blue_met_red)
    def test_blue_met_red_exception_blue_less_than_1(self):
        state = State(red=10, green=10, blue=0)
        self.assertRaises(Exception, state.blue_met_red)

if __name__ == "__main__":
    unittest.main()
