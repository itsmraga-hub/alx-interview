def canUnlockAll(boxes):
    # Initialize a set to keep track of visited boxes
    visited = set()
    # Add the first box (boxes[0]) to the visited set, as it is unlocked initially
    visited.add(0)
    
    # Initialize a stack for DFS
    stack = [0]
    
    # Perform DFS to explore reachable boxes
    while stack:
        current_box = stack.pop()
        keys = boxes[current_box]
        for key in keys:
            # If the key is not in the visited set, add it to the stack and mark it as visited
            if key not in visited:
                stack.append(key)
                visited.add(key)
    
    # If the number of visited boxes is equal to the total number of boxes, return True
    return len(visited) == len(boxes)
