class ConnectGame:
    def __init__(self, board_str):
        self.board = [row.split() for row in board_str.strip().split('\n')]
        self.rows = len(self.board)
        self.cols = len(self.board[0]) if self.rows > 0 else 0

    def get_winner(self):
        if self._check_path("O"):
            return "O"
        if self._check_path("X"):
            return "X"
        return ""

    def _check_path(self, player):
        target = player
        visited = set()
        queue = []

        if target == "O":
            queue = [(0, c) for c in range(self.cols) if self.board[0][c] == "O"]
        else:
            queue = [(r, 0) for r in range(self.rows) if self.board[r][0] == "X"]

        for start in queue:
            visited.add(start)

        idx = 0
        while idx < len(queue):
            r, c = queue[idx]
            idx += 1

            if target == "O" and r == self.rows - 1:
                return True
            if target == "X" and c == self.cols - 1:
                return True

            for nr, nc in self._get_neighbors(r, c):
                if (nr, nc) not in visited and self.board[nr][nc] == target:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        
        return False

    def _get_neighbors(self, r, c):
        potential = [
            (r - 1, c), (r - 1, c + 1),
            (r, c - 1), (r, c + 1), 
            (r + 1, c - 1), (r + 1, c)
        ]
        return [(nr, nc) for nr, nc in potential 
                if 0 <= nr < self.rows and 0 <= nc < self.cols]