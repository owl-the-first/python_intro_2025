from collections import deque


class Maze:
    def __init__(self, size):
        self.size = size
        self.horizontal_barriers = [[True] * size for i in range(size - 1)]
        self.vertical_barriers = [[True] * (size - 1) for i in range(size)]

    def _parse_coordinates(self, key_item):
        x_start = key_item[0]
        y_slice = key_item[1].start
        x_end = key_item[1].stop
        y_end = key_item[2]
        return x_start, y_slice, x_end, y_end, (x_start == x_end) or (y_slice == y_end)

    def __setitem__(self, key_item, state):
        x1, y1, x2, y2, is_straight = self._parse_coordinates(key_item)
        if not is_straight:
            return
        f = (state == "█")
        if x1 == x2:
            row = x1
            for col in range(min(y1, y2), max(y1, y2)):
                if 0 <= col < self.size - 1 and 0 <= row < self.size:
                    self.horizontal_barriers[col][row] = f
        elif y1 == y2:
            col = y1
            for i in range(min(x1, x2), max(x1, x2)):
                if 0 <= col < self.size and 0 <= i < self.size - 1:
                    self.vertical_barriers[col][i] = f

    def _check_connectivity(self, start_x, start_y, end_x, end_y):
        if start_x == end_x and start_y == end_y:
            return True
        to_visit = deque([(start_x, start_y)])
        explored = {(start_x, start_y)}
        while to_visit:
            current_x, current_y = to_visit.popleft()
            directions = [(1, 0, 'down'), (-1, 0, 'up'),
                          (0, 1, 'right'), (0, -1, 'left')]
            for dx, dy, direction in directions:
                next_x, next_y = current_x + dx, current_y + dy
                if not (0 <= next_x < self.size and 0 <= next_y < self.size):
                    continue
                wall_blocked = True
                if direction == 'right':
                    wall_blocked = self.horizontal_barriers[current_y][current_x]
                elif direction == 'left':
                    wall_blocked = self.horizontal_barriers[next_y][current_x]
                elif direction == 'down':
                    wall_blocked = self.vertical_barriers[current_y][current_x]
                elif direction == 'up':
                    wall_blocked = self.vertical_barriers[current_y][next_x]
                if wall_blocked:
                    continue
                if (next_x, next_y) == (end_x, end_y):
                    return True
                if (next_x, next_y) not in explored:
                    explored.add((next_x, next_y))
                    to_visit.append((next_x, next_y))
        return False

    def __getitem__(self, key_item):
        x1, y1, x2, y2, _ = self._parse_coordinates(key_item)
        return self._check_connectivity(x1, y1, x2, y2)

    def __str__(self):
        total_width = 2 * self.size + 1
        result_lines = ["█" * total_width]
        for i in range(self.size):
            room_line = ["█"]
            for col in range(self.size):
                room_line.append("·")
                if col < self.size - 1:
                    room_line.append("█" if self.vertical_barriers[i][col] else "·")
            result_lines.append("".join(room_line) + "█")
            if i < self.size - 1:
                wall_line = ["█"]
                for col in range(self.size):
                    wall_line.append("█" if self.horizontal_barriers[i][col] else "·")
                    if col < self.size - 1:
                        wall_line.append("█")
                result_lines.append("".join(wall_line) + "█")
        result_lines.append("█" * total_width)
        return "\n".join(result_lines)


import sys
exec(sys.stdin.read())
