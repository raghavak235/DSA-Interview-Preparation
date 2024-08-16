
class BinarySearchTreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


def insertBST(root, value):
    if root is None:
        return BinarySearchTreeNode(value)
    else:
        if root.val == value:
            return root

        elif root.val < value:
            root.right =insertBST(root.right, value)
        else:
            root.left = insertBST(root.left, value)
        return root


def searchBST(root, target):
    if root is None:
        return False
    elif root.val < target:
        return searchBST(root.right, target)
    elif root.val > target:
        return searchBST(root.left, target)
    else:
        return True


def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=' ')
        inorderTraversal(root.right )

root = BinarySearchTreeNode(100)
root = insertBST(root,80)
root = insertBST(root, 120)


inorderTraversal(root)

print(searchBST(root,80))