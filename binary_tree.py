from wsgiref import validate


class BinarySearchTree:
    def __init__(self, val=None):
        self.leftchild = None
        self.rightchild = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return
        
        if self.val == val:
            return
        
        if val < self.val:
            if self.leftchild:
                self.leftchild.insert(val)
                return
            self.leftchild = BinarySearchTree(val)
            return
        
        if self.rightchild:
            self.rightchild.insert(val)
            return
        self.rightchild = BinarySearchTree(val)
    
    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.leftchild is not None:
            self.leftchild.preorder(vals)
        if self.rightchild is not None:
            self.rightchild.preorder(vals)
        return vals

if __name__ == '__main__':
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    bst = BinarySearchTree()
    for num in nums:
        bst.insert(num)
    
    print("preorder:")
    print(bst.preorder([]))
    print("#")
    