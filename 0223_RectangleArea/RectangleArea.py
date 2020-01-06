class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        wid1 = abs(A-C)
        hei1 = abs(B-D)
        wid2 = abs(E-G)
        hei2 = abs(F-H)
        x_overlap = A < G and E < C
        y_overlap = B < H and F < D
        all_areas = wid1*hei1 + wid2*hei2
        overlap = 0
        if x_overlap and y_overlap:
            overlap = abs(max(A,E)-min(C,G)) * abs(max(B,F) - min(D,H))
        return all_areas - overlap

# --------------------------------------


class Rectangle:    
    def __init__(self, px, py):
        xlo, ylo = px
        xhi, yhi = py
        self.x = xlo, xhi
        self.y = ylo, yhi
        
    def __len__(self):
        return (self.x[1] - self.x[0]) * (self.y[1] - self.y[0])
    
    def intersection(self, other):
        has_intersection = all((
            Rectangle.is_overlap(self.x, other.x),
            Rectangle.is_overlap(self.y, other.y)
        ))
        
        if not has_intersection:
            return Rectangle.point()
        
        xlo = max(self.x[0], other.x[0])
        ylo = max(self.y[0], other.y[0])
        xhi = min(self.x[1], other.x[1])
        yhi = min(self.y[1], other.y[1])
        
        return Rectangle((xlo, ylo), (xhi, yhi))
    
    @staticmethod
    def is_overlap(bound_a, bound_b):
        a_lo, a_hi = bound_a
        b_lo, b_hi = bound_b
        return a_lo < b_hi and b_lo < a_hi
    
    @classmethod
    def point(cls):
        return cls((0, 0), (0, 0))
    
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        rect1 = Rectangle((A, B), (C, D))
        rect2 = Rectangle((E, F), (G, H))
        rect3 = rect1.intersection(rect2)
        
        return len(rect1) + len(rect2) - len(rect3)