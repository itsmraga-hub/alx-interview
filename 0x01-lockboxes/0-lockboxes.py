def canUnlockAll(boxes):
    # Initialize a set to keep track of visited boxes
    visited = set()
    visited.add(0)

    # Initialize a stack for DFS
    stack = [0]

    while stack:
        current_box = stack.pop()
        keys = boxes[current_box]
        for key in keys:
            if key not in visited:
                stack.append(key)
                visited.add(key)

    return len(visited) == len(boxes)
