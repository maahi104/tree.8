class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def count_subtrees_with_sum_x(root, x):
    if root is None:
        return 0

    count = 0
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            queue.append(node.left)
            queue.append(node.right)

            sum = node.data
            if sum == x:
                count += 1

            left = node.left
            right = node.right
            while left or right:
                if left:
                    sum += left.data
                    if sum == x:
                        count += 1
                    left = left.left or left.right

                if right:
                    sum += right.data
                    if sum == x:
                        count += 1
                    right = right.right or right.left

    return count

# Example usage
if __name__ == '__main__':
    root = None
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input())
        root = insert(root, data)

    x = int(input("Enter the value of x: "))
    print("Number of subtrees with sum x: ", count_subtrees_with_sum_x(root, x))