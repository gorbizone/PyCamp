# -*- coding: utf-8 -*-
"""
Testing module for Lotek (PyCamp - Module 0)
"""

from lotek import drawing_machine


def test_drawing_machine():
    drawn_numbers = sorted(list(drawing_machine()))
    for _ in range(300):
        assert len(drawn_numbers) == 6
        assert drawn_numbers[1] >= 1
        assert drawn_numbers[-1] <= 49
