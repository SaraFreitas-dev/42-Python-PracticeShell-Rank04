def count_islands(grid: list[str]) -> int:
    if not grid:
        return 0
    cols: int = len(grid[0])
    rows: int = len(grid)
    seen: set[tuple[int, int]] = set()
    islands: int = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "#" and (row, col) not in seen:
                islands += 1

                # Increase the island
                to_visit: list[tuple[int, int]] = [(row, col)]
                seen.add((row, col))

                while to_visit:
                    r, c = to_visit.pop()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr = r + dr
                        nc = c + dc
                        if ((0 <= nr < rows) and (0 <= nc < cols)
                                and (grid[nr][nc] == "#")
                                and ((nr, nc) not in seen)):
                            seen.add((nr, nc))
                            to_visit.append((nr, nc))
    return islands


if __name__ == "__main__":
    print(count_islands(['##..', '##..', '..##']))  # 2
    print(count_islands(['#.#', '.#.', '#.#']))     # 5
    print(count_islands(['###', '#.#', '###']))     # 1
    print(count_islands(['....', '....']))          # 0
    print(count_islands(['#']))                     # 1
    print(count_islands([]))                        # 0
    print(count_islands(['#.#.#']))                 # 3
    print(count_islands(['#', '.', '#', '#']))      # 2
