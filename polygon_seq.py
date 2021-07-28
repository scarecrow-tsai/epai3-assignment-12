from polygon import Polygon


class PolygonSeq:
    def __init__(self, vertices, radius):
        self.vertices = vertices
        if self.vertices < 3:
            raise ValueError(
                "Number of edges/vertices should be equal to or greater than 3"
            )
        self.radius = radius
        self.polygon = [
            Polygon(num_vertices=i, circum_radius=self.radius)
            for i in range(3, self.vertices + 1)
        ]

    def __len__(self):
        return self.vertices

    def __iter__(self):
        return self.PolygonsIterator(self)

    def __getitem__(self, s):
        return self.polygon[s]

    def __repr__(self):
        """
        repr method for PolygonSeq class.
        """
        return f"PolygonSeq(1 - {self.vertices}, {self.radius})"

    def __str__(self):
        """
        str method for PolygonSeq class.
        """
        return f"PolygonSeq(vertices: {1, self.vertices},radius={self.radius})"

    def get_maxeff_poly(self):
        """
        Get polygon with max efficiency.
        Efficiency = area:perimeter
        """
        eff_list = []
        for p in self:
            if p.num_vertices >= 3:
                eff_list.append(p.area / p.perimeter)

        return max(eff_list), self[eff_list.index(max(eff_list))]

    class PolygonsIterator:
        def __init__(self, polygon_obj):
            self.polygon_obj = polygon_obj
            self._index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self._index >= len(self.polygon_obj.polygon):
                raise StopIteration
            else:
                item = self.polygon_obj.polygon[self._index]
                self._index += 1
                return item


if __name__ == "__main__":
    ps = PolygonSeq(vertices=5, radius=5)
    print(ps)
    print(list(ps))
    print(ps[1])
    print(ps[2])
    print(ps.get_maxeff_poly())
    print([i for i in iter(ps)])
