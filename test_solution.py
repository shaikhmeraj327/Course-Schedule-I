import unittest

from solution import Solution, can_finish


class CourseScheduleTests(unittest.TestCase):
    def test_can_complete_when_acyclic(self):
        self.assertTrue(can_finish(4, [[1, 0], [2, 1], [3, 2]]))

    def test_cannot_complete_when_cycle_exists(self):
        self.assertFalse(can_finish(2, [[1, 0], [0, 1]]))

    def test_solution_compatibility_methods(self):
        solver = Solution()
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        self.assertTrue(solver.canFinish(4, prerequisites))
        self.assertTrue(solver.isPossible(4, prerequisites))

    def test_solution_compatibility_methods_with_cycle(self):
        solver = Solution()
        prerequisites = [[1, 0], [0, 1]]
        self.assertFalse(solver.canFinish(2, prerequisites))
        self.assertFalse(solver.isPossible(2, prerequisites))


if __name__ == "__main__":
    unittest.main()
