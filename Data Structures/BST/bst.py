import numpy as np 
import matplotlib.pyplot as plt 


class TreeNode:
    """Class representing a node in a binary search tree.

    Attributes:
        data: The data stored in the node.
        left: The left child node.
        right: The right child node.
    """

    def __init__(self, data):
        """Initializes a TreeNode with the given data.

        Arguments:
            data: The data to store in the node.
        """
        self.data = data 
        self.left = None 
        self.right = None 


def inOrderTraversal(node):
    """Performs an in-order traversal of the binary search tree.

    Arguments:
        node: The root node of the binary search tree.
    """
    if node is None:
        return 
    inOrderTraversal(node.left)
    print(node.data, end=', ')
    inOrderTraversal(node.right)


def search(node, target):
    """Searches for a node with the given target data in the binary search tree.

    Arguments:
        node: The root node of the binary search tree.
        target: The data to search for.

    Returns:
        The node with the target data if found, otherwise None.
    """
    if node is None:
        return None 
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)
    

def insert(node, data):
    """Inserts a node with the given data into the binary search tree.

    Arguments:
        node: The root node of the binary search tree.
        data: The data to insert.

    Returns:
        The root node of the binary search tree after insertion.
    """
    if node is None:
        return TreeNode(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node


def minValueNode(node):
    """Finds the node with the minimum value in the binary search tree.

    Arguments:
        node: The root node of the binary search tree.

    Returns:
        The node with the minimum value.
    """
    current = node
    while current.left is not None:
        current = current.left
    return current


def maxValueNode(node):
    """Finds the node with the maximum value in the binary search tree.

    Arguments:
        node: The root node of the binary search tree.

    Returns:
        The node with the maximum value.
    """
    current = node 
    while current.right is not None:
        current = current.right 
    return current 


def delete(node, data):
    """Deletes a node with the given data from the binary search tree.

    Arguments:
        node: The root node of the binary search tree.
        data: The data of the node to delete.

    Returns:
        The root node of the binary search tree after deletion.
    """
    if not node:
        return None

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        
        # Node with only one child or no child
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp

        # Node with two children, get the in-order successor
        node.data = minValueNode(node.right).data
        node.right = delete(node.right, node.data)

    return node


def randomize_BST(num:int)->TreeNode:
    """Creates a binary search tree with random numbers.

    Arguments:
        num -- The total number of elements in the BST.

    Returns:
        The root node of the binary search tree.
    """
    nums = np.random.randint(0, 100, (1, num))
    nums = nums.flatten()
    print(nums) 
    root = TreeNode(nums[0])
    print(f'root-> {root.data}')
    for i in range(1, len(nums)):
        print(f'Inserting {nums[i]}')
        insert(root, nums[i])
    return root 


def LCA(root:TreeNode, num1:int, num2:int)->int:
    """Function to get the lowest common ancestor of two nodes of a BST

    Arguments:
        num1 -- a number 
        num2 -- another number to get LCA

    Returns:
        Lowest Common Ancestor of num1 and num2 
    """
    if(root.data > num1) and (root.data>num2) and root.left:
        print(f'Calling LCA for {root.left.data, num1, num2}')
        return LCA(root.left, num1, num2)
    
    if(root.data < num1) and (root.data<num2) and root.right: 
        print(f'Calling LCA for {root.right.data, num1, num2}')
        return LCA(root.right, num1, num2)
    
    return root.data 


def plot_tree(root:TreeNode):
    """Function to plot the BST

    Arguments:
        root -- TreeNode of the BSt

    Returns:
        a plot of the tree with nodes and edges visible
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')

    def calculate_positions(node, x=0, y=0, level=1, positions=None, parent=None):
        if positions is None:
            positions = {}

        if node is not None:
            positions[node] = (x, y)
            color = 'red' if parent is None else ('green' if node == parent.left else 'blue')  # Assign color based on node type
            if parent:
                ax.plot([positions[parent][0], x], [positions[parent][1], y], color=color, linewidth=2)  # Draw lines between nodes
            # Recursively calculate positions for left and right subtrees
            horizontal_gap = 2.5 / (2 ** level)  # Adjust horizontal gap based on level
            calculate_positions(node.left, x - horizontal_gap, y - 1.5, level + 1, positions, node)
            calculate_positions(node.right, x + horizontal_gap, y - 1.5, level + 1, positions, node)
        
        return positions

    positions = calculate_positions(root)

    for node, (x, y) in positions.items():
        ax.text(x, y, str(node.data), size=14, ha='center', va='center', bbox=dict(facecolor='white', boxstyle='circle'))

    plt.tight_layout()
    plt.show()


def get_height(root:TreeNode)->int:
    """Function to get the height of the binary tree 

    Arguments:
        root -- root node of the tree
    """
    # print(f'Root is {root.data}')
    if root is None:
        # print(f'Returned 0')
        return 0 
    # print(f'Root is {root.data}')

    # print(f'Calling left of {root.data}\n')
    left_height = get_height(root.left)
    # print(f'Calling right of {root.data}\n')
    
    right_height = get_height(root.right)
    # print(f'Left height of {root.data} is {left_height}')
    # print(f'right height of {root.data} is {right_height}')

    # print(f'{max(left_height, right_height) + 1}')
    return max(left_height, right_height) + 1