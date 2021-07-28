import pytest
import os
import inspect
import re
import polygon, polygon_seq


def test_readme_exists():
    """Checks if README file exists"""
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_file_for_atleast_10_hashes():
    """Checks if README file has proper formatting (minimum of 10 hashes)"""
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_cap_letter():
    """test fails if Capital letter(s) used for function names"""
    functions = inspect.getmembers(polygon, inspect.isfunction)
    for function in functions:
        assert (
            len(re.findall("([A-Z])", function[0])) == 0
        ), "You have used Capital letter(s) in your function names"


def test_polygon_constructor():
    """
    This function tests the initializer function of polygon
    """
    with pytest.raises(
        ValueError,
        match=r".*Number of edges/vertices should be equal to or greater than 3*",
    ):
        p1 = polygon.Polygon(2, 10)


p2 = polygon.Polygon(6, 10)


def test_polygon_interior_angle():
    """This function tests the interior angle calculated by polygon class"""

    assert p2.interior_angle == 120.0, "Interior angle is incorrect."


def test_polygon_edge_length():
    """This function tests the edge length calculated by polygon class"""

    assert p2.edge_length == 9.999999999999998, "Egde length is incorrect."


def test_polygon_apothem():
    """This function tests the apothem calculated by polygon class"""

    assert p2.apothem == 8.660254037844387, "Apothem is incorrect."


def test_polygon_area():
    """This function tests the area calculated by polygon class"""

    assert p2.area == 259.80762113533154, "Area is incorrect."


def test_polygon_perimeter():
    """This function tests the perimeter calculated by polygon class"""

    assert p2.perimeter == 59.999999999999986, "perimeter is incorrect."


p3 = polygon.Polygon(6, 10)
p4 = polygon.Polygon(7, 10)


def test_equal_to():
    """This test checks the equal to operator"""

    assert p2 == p3, "Equal to is incorrect."


def test_greater_than():
    """
    This function tests the greater than operator
    """

    assert p4 > p2, "Greater than is incorrect."


def test_polygon_seq_constructor():
    """
    This function tests the initializer function of polygon sequence
    """
    with pytest.raises(
        ValueError,
        match=r".*Number of edges/vertices should be equal to or greater than 3*",
    ):
        p5 = polygon_seq.PolygonSeq(2, 10)


p6 = polygon_seq.PolygonSeq(6, 10)


def test_len_operator():
    """This function tests the len method"""
    assert len(p6) == 6, "length is incorrect."
