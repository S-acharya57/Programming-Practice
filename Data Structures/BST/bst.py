import numpy as np 


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