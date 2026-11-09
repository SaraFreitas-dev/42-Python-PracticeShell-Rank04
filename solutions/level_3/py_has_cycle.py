def has_cycle(graph: dict[str, list[str]]) -> bool:
    if not graph:
        return False
    path: set[str] = set()
    finished_path: set[str] = set()

    def explore(node: str) -> bool:
        path.add(node)
        for neighbor in graph.get(node, []):
            if neighbor in path:
                return True
            if neighbor not in finished_path:
                if explore(neighbor):
                    return True
        path.remove(node)
        finished_path.add(node)
        return False
    
    for node in graph:
        if explore(node):
            return True
    return False
    

if __name__ == "__main__":
    print(has_cycle({"a": ["b"], "b": ["c"], "c": []}))  # False
    print(has_cycle({"a": ["b"], "b": ["a"]}))  # True
    print(has_cycle({"a": ["a"]}))  # True
    print(has_cycle({"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": []}))  # False
    print(has_cycle({"a": ["b"], "b": [], "c": ["d"], "d": ["e"], "e": ["c"]}))  # True
    print(has_cycle({}))  # False
