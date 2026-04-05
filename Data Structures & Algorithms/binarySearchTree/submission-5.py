class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None 


    def insert(self, key: int, val: int) -> None:
        # Maybe using a dummy root would be better? It skips the edge case of empty tree
        if not self.root:
            self.root = TreeNode(key, val)
            return

        def insert_rec(key, val, root):
            if root == None:
                return TreeNode(key, val)
            if key > root.key:
                root.right = insert_rec(key, val, root.right)
            elif key < root.key:
                root.left = insert_rec(key, val, root.left)
            else:
                root.val = val
            
            return root 
        
        self.root = insert_rec(key, val, self.root)

    def get(self, key: int) -> int:

        def get_helper(key, root):
            if root == None:
                return -1 
            if key > root.key:
                return get_helper(key, root.right)
            elif key < root.key:
                return get_helper(key, root.left)
            else: 
                return root.val
        get = get_helper(key, self.root)
        return get


    def getMin(self) -> int:
        def min_helper(root):
            if root == None:
                return -1 
            if root.left == None:
                return root.val
            else: 
                min_helper(root.left)
        least = min_helper(self.root)
        return least


    def getMax(self) -> int:

        def max_helper(root):
            if root == None:
                return -1 
            if root.right == None:
                print(root.val)
                return root.val
            else: 
                return max_helper(root.right)

        most = max_helper(self.root)
        return most


    def remove(self, key: int) -> None:

        def get_min(root):
            if root == None:
                return None
            if not root.left:
                return root
            else:
                return get_min(root.left)

        def rem_helper(key, root):
            if root == None:
                return 

            if key > root.key:
                root.right = rem_helper(key, root.right)
            elif key < root.key:
                root.left = rem_helper(key, root.right)
            else:
                if root.left == None:
                    return root.right
                elif root.right == None:
                    return root.left 
                else:
                    min_node = get_min(root.right)
                    print(min_node.key)
                    root.key = min_node.key
                    root.val = min_node.val
                    root.right = rem_helper(min_node.key, root.right)
            return root
        
        self.root = rem_helper(key, self.root)


    def getInorderKeys(self) -> List[int]:
        out = []
        curr = self.root

        def dfs(node):
            if node == None:
                return
            dfs(node.left)
            out.append(node.key)
            dfs(node.right)
        dfs(curr)
        return out


