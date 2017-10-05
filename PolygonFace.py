class Face:

    def __init__(self, vertices=[], vertices_id=[], color='#00ffff'):
        self._vertices = vertices
        self._vertices_ids = vertices_id
        self._color = color
    
    def __str__(self):
        return str(self._vertices_ids)

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, vertices):
        self._vertices = vertices

    def get_xs(self):
        return [v[0][0] for v in self._vertices]

    def get_ys(self):
        return [v[0][1] for v in self._vertices]

    def get_zs(self):
        return [v[0][2] for v in self._vertices]

    def get_color(self):
        return self._color