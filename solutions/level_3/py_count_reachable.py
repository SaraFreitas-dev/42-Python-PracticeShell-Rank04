def count_reachable(graph: dict[str, list[str]], start: str) -> int:
    if start not in graph:
        return 0
    if not graph[start]:
        return 1
    seen: set[str] = set()

    to_visit: list[str] = [start]
    seen.add(start)

    while to_visit:
        neighbors: list[str] = graph.get(to_visit.pop(), [])
        for n in neighbors:
            if n not in seen:
                seen.add(n)
                to_visit.append(n)
    return len(seen)


if __name__ == "__main__":
    print(count_reachable({"a": ["b", "c"], "b": ["d"], "c": [], "d": []}, "a"))  # 4
    print(count_reachable({"a": ["b", "c"], "b": ["d"], "c": [], "d": []}, "b"))  # 2
    print(count_reachable({"a": ["b"], "b": ["a"]}, "a"))  # 2
    print(count_reachable({"a": ["b"], "b": [], "c": ["a"]}, "a"))  # 2
    print(count_reachable({"x": []}, "x"))  # 1
    print(count_reachable({"a": []}, "z"))  # 0
