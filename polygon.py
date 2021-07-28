import math


class Polygon:
    """
    Polygon class.
    Input: vertices and radius
    """

    def __init__(self, num_vertices, circum_radius):
        self.num_vertices = num_vertices
        if self.num_vertices < 3:
            raise ValueError(
                "Number of edges/vertices should be equal to or greater than 3"
            )
        self.circum_radius = circum_radius

    @property
    def num_vertices(self):
        """
        Getter for num_verticess.
        """
        return self._num_vertices

    @num_vertices.setter
    def num_vertices(self, val):
        """
        Setter for num_verticess.
        """
        self._num_vertices = val

    @property
    def circum_radius(self):
        """
        Getter for circum_radius.
        """
        return self._circum_radius

    @circum_radius.setter
    def circum_radius(self, val):
        """
        Setter for circum_radius.
        """
        self._circum_radius = val

    @property
    def interior_angle(self):
        """
        Getter for interior_angle.
        """
        return (self.num_vertices - 2) * 180 / self.num_vertices

    @property
    def edge_length(self):
        """
        Getter for edge_length.
        """
        return 2 * self.circum_radius * math.sin(math.pi / self.num_vertices)

    @property
    def apothem(self):
        """
        Getter for apothem.
        """
        return self.circum_radius * math.cos(math.pi / self.num_vertices)

    @property
    def area(self):
        """
        Getter for area.
        """
        if self.num_vertices >= 3:
            return 0.5 * self.num_vertices * self.edge_length * self.apothem
        else:
            raise ValueError("Atleast 3 sides required to calculate area")

    @property
    def perimeter(self):
        """
        Getter for perimeter.
        """
        if self.num_vertices >= 3:
            return self.num_vertices * self.edge_length
        else:
            raise ValueError("Atleast 3 sides required to calculate perimeter")

    def __eq__(self, other):
        """
        Equal to method for Polygon class.
        """
        if isinstance(other, Polygon):
            return (
                self.num_vertices == other.num_vertices
                and self.circum_radius == other.circum_radius
            )
        else:
            raise NotImplementedError

    def __gt__(self, other):
        """
        Greater than method for Polygon class.
        """
        if isinstance(other, Polygon):
            return self.num_vertices > other.num_vertices
        else:
            raise NotImplementedError

    def __repr__(self):
        """
        repr method for Polygon class.
        """
        return f"Polygon({self.num_vertices}, {self.circum_radius})"

    def __str__(self):
        """
        str method for Polygon class.
        """
        return f"Polygon(vertices={self.num_vertices}, radius={self.circum_radius})"


if __name__ == "__main__":
    p = Polygon(3, 5)
    p1 = Polygon(4, 5)
    print(p, p1)
    print(p1 == p)
    print(p1 > p)
    print(p.num_vertices)
    print(p.circum_radius)
    print(p.interior_angle)
    print(p.edge_length)
    print(p.apothem)
    print(p.area)
    print(p.perimeter)
