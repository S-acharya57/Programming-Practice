import bst 

root = bst.randomize_BST(10)


def kth_smallest(root:bst.TreeNode, k:int)->int:
    """To find the k-th smallest element of the BST

    Arguments:
        root -- root of the BST
        k -- the numerical value of the smallest element at position 'k' 

    Returns:
        an integer that is the k-th smallest element in the BST
    """
    if(root==None):
        return None 
    print(f'At root: {root.data}')    
    # print(f'Going left to {root.left.data}\n\n')
    left = kth_smallest(root.left, k)

    if (left!=None):
        return left 
    
    k = k-1 
    if(k==0):
        return root.data 
    
    # print(f'Going right to {root.right.data}\n\n')
    return kth_smallest(root.right, k)

k = 3
bst.inOrderTraversal(root)
print(f'\n{k}-th smallest data is: \n')
print(kth_smallest(root, k)) 