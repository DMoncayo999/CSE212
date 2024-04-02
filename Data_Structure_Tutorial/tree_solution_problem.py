class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert_node(root, key):
    if root is None:
        return TreeNode(key)
    
    if key < root.key:
        root.left = insert_node(root.left, key)
    elif key > root.key:
        root.right = insert_node(root.right, key)
    
    return root

def find_min_value(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.key

# Example usage
root = None
keys = [50, 30, 70, 20, 40, 60, 80]

for key in keys:
    root = insert_node(root, key)

min_value = find_min_value(root)
print(f"The minimum value in the BST is {min_value}")  # Output: 20


