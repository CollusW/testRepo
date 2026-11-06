"""demo_tool 的单元测试。"""

import unittest

from demo_tool import divide


class TestDivide(unittest.TestCase):
    """覆盖 divide 的正常路径与除零异常。"""

    def test_positive(self):
        self.assertEqual(divide(10, 2), 5)

    def test_negative(self):
        self.assertEqual(divide(-10, 2), -5)

    def test_float_result(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
