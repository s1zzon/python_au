+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Symmetric Tree](#symmetric-tree)
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
+ [Binary Search Tree Iterator](#binary-search-tree-iterator)
<!-----solution----->

## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

```python

def __init__(self, root: TreeNode):
    self.index = 0
    self.values = self.insert(root)
    self.num_values = len(self.values)
    
def insert(self, root: TreeNode) -> List[int]:
    if root == None:
        return []
    if root.left == None and root.right == None:
        return [root.val]
    if root.left == None:
        return [root.val] + self.insert(root.right)
    if root.right == None:
        return self.insert(root.left) + [root.val]
    return self.insert(root.left) + [root.val] + self.insert(root.right)
    

def next(self) -> int:
    output = self.values[self.index]
    self.index += 1
    return output

def hasNext(self) -> bool:
    return self.index < self.num_values
```

## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

```python
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if root is None:
        return root
    queue = []
    return_list = []
    queue.append(root)
    while len(queue) > 0:
        ans = []
        l = len(queue)
        for l in range(l):
            node = queue.pop(0)
            ans.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return_list.append(ans)
    return return_list
```

## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

```python
def kthSmallest(self, root: TreeNode, k: int) -> int:
    self.k = k
    self.result = 0
    def dfs(node: TreeNode):
        if not node or self.result:
            return
        dfs(node.left)
        self.k -= 1
        if not self.k:
            self.result = node.val
        dfs(node.right)

    dfs(root)
    return self.result
```

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

```python
        if node:
            if node.val <= left or node.val >= right: return False
            return rec(node.left, left, node.val) and rec(node.right, node.val, right)
        return True
s Solution:
def isValidBST(self, root: TreeNode) -> bool:
    return rec(root, -float('inf'), float('inf') )        
```

## Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

```python
if node1==None and node2==None:
    return True
elif node1==None or node2==None:
    return False
else:
    return node1.val==node2.val and isSymmetricBst(node1.left,node2.right) and isSymmetricBst(node1.right, node2.left)

s Solution:
def isSymmetric(self, root: TreeNode) -> bool:
    if root == None:
        return True
    return isSymmetricBst(root.left, root.right)
```

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.traverse(root, res)
        return res

def traverse(self, node, order):
    if node is None:
        return
    self.traverse(node.left, order)
    order.append(node.val)
    self.traverse(node.right, order)
    return order
```

## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

```python
def invertTree(self, root: TreeNode) -> TreeNode:
    if node is None:
        return
    node.left, node.right = node.right, node.left
    self.invert(node.left)
    self.invert(node.right)
    return node
```

## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
def maxDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    leftN = self.maxDepth(root.left)
    rightN = self.maxDepth(root.right)
    return max(leftN, rightN) + 1
```
