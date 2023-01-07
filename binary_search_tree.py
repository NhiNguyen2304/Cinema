import random
from customer import Customer


class BTree:
    def __init__(self, key) -> None:
        self.key = key
        self.left_child = None
        self.right_child = None

    def __str__(self) -> str:
        return f"{self.key}"

    def __repr__(self) -> str:
        return f"<BSTNode at {hex(id(self))}"

    def display(self):
        '''
        This function is inspired from: https://stackoverflow.com/a/54074933
        Description: Display binary search tree for testing purpose
        '''
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """
        This function is inspired from: https://stackoverflow.com/a/54074933
        Description: Returns list of strings, width, height, and horizontal coordinate of the root.
        """
        # No child.
        if self.right_child is None and self.left_child is None:
            line = '%s' % self.key.print_testing()
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right_child is None:
            lines, n, p, x = self.left_child._display_aux()
            s = '%s' % self.key.print_testing()
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left_child is None:
            lines, n, p, x = self.right_child._display_aux()
            s = '%s' % self.key.print_testing()
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left_child, n, p, x = self.left_child._display_aux()
        right_child, m, q, y = self.right_child._display_aux()
        s = '%s' % self.key.print_testing()
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left_child += [n * ' '] * (q - p)
        elif q < p:
            right_child += [m * ' '] * (p - q)
        zipped_lines = zip(left_child, right_child)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def isEmpty(self):
        ''' return true if the binary tree is empty; otherwise, return false'''
        if self.key == None:
            return True
        return False
    
    def insert(self, k):
        '''
		// pre: true
		// post: item is added to the binary search tree
        '''
        if self.key.isEmpty():
            self.key = k
        else:
            if self.key.compare_to(k) == 1:
                if self.left_child == None:
                    self.left_child = BTree(k)
                else:
                    self.left_child.insert(k)
            elif self.key.compare_to(k) == -1:
                if self.right_child == None:
                    self.right_child = BTree(k)
                else:
                    self.right_child.insert(k)

    def minValueNode(node):
        current = node
        while(current.left_child != None):
            current = current.left_child

        return current

    def delete(self, k):
        '''
        // pre: true
		// post: an occurrence of item is removed from the binary search tree 
		//		 if item is in the binary search tree
        '''
        ptr = self
        parent = None
        if self.key.compare_to(k) == 0:
            print("Cannot delete root")
        else:
            while ptr != None and ptr.key != k:
                parent = ptr
                if ptr.key.compare_to(k) == 1:
                    ptr = ptr.left_child
                else:
                    ptr = ptr.right_child

            if ptr != None:
                if ptr.left_child != None and ptr.right_child != None:
                    if ptr.left_child.right_child == None:
                        ptr.key = ptr.left_child
                        ptr.left_child = ptr.left_child.left_child
                    else:
                        p = ptr.left_child
                        pp = ptr
                        while p.right_child != None:
                            pp = p
                            p = p.right_child
                        ptr.key = p.key
                        pp.right_child = p.left_child

                else:
                    if ptr.left_child != None:
                        c = ptr.left_child
                    else:
                        c = ptr.right_child

                    if ptr == self.key: # need to change root
                        self.key = c
                    else:
                        if ptr == parent.left_child:
                            parent.left_child = c
                        else:
                            parent.right_child = c
                


    def search(self, k):
        '''
        // pre: true
		// post: return true if item is in the binary search customer;
		//	     otherwise, return None.
        '''
        if self.key != None:
            if self.key.compare_to(k) == 0:
                return self.key
            else:
                if self.key.compare_to(k) == -1:
                    if self.right_child != None:
                        return self.right_child.search(k)
                else:
                    if self.left_child != None:
                        return self.left_child.search(k)
        return None

    
    def pre_order_traverse(self):
        '''
        // pre: true
		// post: all the nodes in the binary tree are visited once and only once in pre-order
        '''
        # if self.key != None:
        #     item.append(self.key)
        print(self.key)
        if self.left_child != None:
            self.left_child.pre_order_traverse()
        if self.right_child != None:
            self.right_child.pre_order_traverse()
        # return item
    
    def in_order_traverse(self):
        '''
		// pre: true
		// post: all the nodes in the binary tree are visited once and only once in in-order
        '''
        if self.left_child != None:
            self.left_child.in_order_traverse()
        # if self.key != None:
        #     item.append(self.key)
        if self.right_child != None:
            self.right_child.in_order_traverse()
        # return item
    
    def post_order_traverse(self):
        '''
		// pre: true
		// post: all the nodes in the binary tree are visited once and only once in post-order
        '''
        if self.left_child != None:
            self.left_child.post_order_traverse()
        if self.right_child != None:
            self.right_child.post_order_traverse()
        # if self.key != None:
        #     item.append(self.key)
        # return item
    
    def clear(self):
        '''
		// pre: true
		// post: all the nodes in the binary tree are removed and the binary tree becomes empty
        '''
        self = BTree(None)

if __name__ == '__main__':
    # tree = BTree('A')
    # for x in 'BCDEFGH':
    #     tree.Insert(x)
    # print(tree.PreOrderTraverse())
    c0 = Customer('Nina', 'Nguyen','0450343022', 'Paypal', random.randint(1, 10))
    tree = BTree(c0)
    tree.delete(c0)
    c1 = Customer('Jim', 'Tomkinson', '0450343234', 'Paypal', random.randint(1, 10))
    c2 = Customer('Richy', 'AAAAA', '13434343', 'Cash', random.randint(1, 10))
    c3 = Customer('Nina', 'Hguyen','0450343022', 'Paypal', 9)

    tree.insert(c1)
    tree.insert(c2)
    tree.insert(c3)

    tree.display()

    # print(tree.key)
    # print(tree.left_child)
    # print(tree.right_child)
    # print(tree.left_child.right_child)
    # print(tree.right_child.right_child.right_child)

    # tree.delete(c3)
    # print('AFTER ####')
    # print(tree.key)
    # print(tree.left_child)
    # print(tree.right_child)
    # print(tree.left_child.right_child)

    print(tree.search(Customer('Nina','NNguyen','','','')))