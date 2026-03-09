class DetectSquares:

    def __init__(self):
        self.points_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        total_squares = 0

        for (x, y), count in self.points_count.items():
            if abs(px - x) == abs(py - y) and px != x:
                if (px, y) in self.points_count and (x, py) in self.points_count:
                    total_squares += count * self.points_count[(px, y)] * self.points_count[(x, py)]
                    
        return total_squares
