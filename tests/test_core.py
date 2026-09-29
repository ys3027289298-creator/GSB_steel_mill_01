import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_charge(self):
        state = core.new_game()
        self.assertTrue(core.charge(state, 1, 10))
        self.assertFalse(core.charge(state, 1, 10))

    def test_02_furnace_capacity(self):
        state = core.new_game()
        state["furnace_load"] = 2
        result = core.smelt(state, 1)
        self.assertFalse(result)

    def test_03_temp_boundary(self):
        state = core.new_game()
        self.assertEqual(core.check_temp(state, 35), "over")

    def test_04_cancel_releases_furnace(self):
        state = core.new_game()
        core.smelt(state, 1)
        core.cancel(state, 1)
        self.assertEqual(state["furnace_load"], 0)

    def test_05_no_desulfur_on_fault(self):
        state = core.new_game()
        state["fault"] = True
        result = core.desulfur(state, 5)
        self.assertFalse(result)

    def test_06_leak_once(self):
        state = core.new_game()
        core.leak(state)
        self.assertEqual(state["safety"], 90)

    def test_07_no_cast_without_continuous(self):
        state = core.new_game()
        state["continuous"] = 0
        result = core.cast(state, 5)
        self.assertFalse(result)

    def test_08_load_preserves_batch(self):
        state = core.new_game()
        state["batch_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["batch_id"], 4)


if __name__ == "__main__":
    unittest.main()
