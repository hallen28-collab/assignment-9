class DoctorNode:
 
    def __init__(self, name):
        self.name = name
        self.left = None   # left report
        self.right = None  # right report
 
 
class DoctorTree:

    def __init__(self):
        self.root = None
 
    def _find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        found = self._find(node.left, name)
        if found is not None:
            return found
        return self._find(node.right, name)
 
    def insert(self, parent_name, employee_name, side):
        if side not in ("left", "right"):
            print(f"Invalid side '{side}'. Use 'left' or 'right'.")
            return False
 
        parent = self._find(self.root, parent_name)
        if parent is None:
            print(f"Parent '{parent_name}' not found in the tree.")
            return False
 
        if getattr(parent, side) is not None:
            print(f"{parent_name} already has a {side} report.")
            return False
 
        setattr(parent, side, DoctorNode(employee_name))
        return True
 
    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)
 
    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)
 
    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]
 
 
# Test
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
 
    
    print(tree.insert("Dr. Croft", "Dr. Goldsmith", "right"))  
    print(tree.insert("Dr. Croft", "Dr. Phan", "left"))        
    print(tree.insert("Dr. Phan", "Dr. Carson", "right"))      
    print(tree.insert("Dr. Phan", "Dr. Morgan", "left"))       
 
    
    print(tree.preorder(tree.root))   
    print(tree.inorder(tree.root))    
    print(tree.postorder(tree.root))  
 
    print("\n--- Edge cases ---")
    print(tree.insert("Dr. Nobody", "Dr. Lee", "left"))     
    print(tree.insert("Dr. Croft", "Dr. Lee", "middle"))    
    print(tree.insert("Dr. Croft", "Dr. Lee", "left"))      
    print(tree.insert("Dr. Morgan", "Dr. Lee", "left"))     
    print(tree.preorder(tree.root))
 
    empty = DoctorTree()
    print(empty.insert("Dr. Croft", "Dr. Lee", "left"))     
    print(empty.preorder(empty.root))                      
    print(empty.inorder(empty.root))                        
    print(empty.postorder(empty.root))                      
 
    phan = tree._find(tree.root, "Dr. Phan")
    print(tree.preorder(phan))