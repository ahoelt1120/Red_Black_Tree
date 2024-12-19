"""
Name: Amanda Hoelting
Title: Red Black Tree
"""
class Node(object):
    """Node object for binary search tree

                Represents a node in a red black tree. Has all attributes that a node in
                a red black tree would need (parent, left child, right child,and node data).

                Attributes
                ----------
                data: Node
                    Data of the node
                parent: Node
                    Parent of the node
                left: Node
                    Left of the node
                right: Node
                    Right of the node
                color: str
                    Signifies if node is red or black
                """
    def __init__(self, data, left = None, right = None, parent = None, color = 'red'):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color


class rb_tree(object):
    """Red black tree

            Supports most standard red black tree operations (insert, traverse, delete). The underlying implementation uses
            node objects to represent data in the tree. When initialized, Tree creates a new variable
            root that is set to None.

            Attributes
            ----------
            root: Node
                Root node of the tree
            sentinel: Node
                Node with a value of None and a color black
            sentinel.parent: Node
                Node with a value of None and a color black
            sentinel.left: Node
                Node with a value of None and a color black
             sentinel.right: Node
                Node with a value of None and a color black

            Methods
            -------
            print_tree(self):
                Print the data of all nodes in order
            __print_tree(self, curr_node):
                Recursively print a subtree (in order), rooted at curr_node
            __print_with_colors(self, curr_node):
                Recursively print the color and data of a node in a subtree
                (in order), rooted at curr_node
                Printed in PREORDER
            contains(self, data):
                Return True of node containing data is present in the tree
            __iter__(self):
                Iterate over the nodes with inorder traversal using a for loop
            inorder(self):
                Traverse through the tree in order
            preorder(self):
                Traverse through the tree preorder
            postorder(self):
                Traverse through the tree postorder
            __traverse(self, curr_node, traversal_type)):
                Yield data of the correct nodes
            find_min(self):
                Returns the minimum value held in the tree and returns None if the tree is empty
            find_node(self, data):
                Returns the node with that particular data value else returns None
            __get(self, data, current_node):
                Helper function receives data and a node. Returns the node with
                the given data
            find_successor(self, data):
                Receives data and finds a sucessor node for a node with that data
            insert(self, data):
                Inserts a node into the red black tree
            bst_insert(self, data):
                Inserts a node into a binary search tree
            __put(self, data, current_node):
                Helper function that finds the appropriate place to add a node in the tree
            delete(self, data):
                Deletes a node from the red black tree
            left_rotate(self, current_node):
                Rotates nodes left around current_node
            right_rotate(self, current_node):
                Rotates nodes right around current_node
            __rb_insert_fixup(self, z):
                This function maintains the balancing and coloring
                property after bst insertion
            __rb_delete_fixup(self, z):
                This function maintains the balancing and coloring
                property after bst deletion
            """

    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    # initialize root and size
    def __init__(self):
        self.root = None
        self.sentinel = Node(None, color = 'black')
        self.sentinel.parent = self.sentinel
        self.sentinel.left = self.sentinel
        self.sentinel.right = self.sentinel
    
    def print_tree(self):
        '''Print the data of all nodes in order'''
        self.__print_tree(self.root)
    
    def __print_tree(self, curr_node):
        '''Recursively print a subtree (in order), rooted at curr_node
         Printed in preorder'''
        if curr_node is not self.sentinel:
            print(str(curr_node.data), end=' ')  # save space
            self.__print_tree(curr_node.left)
            self.__print_tree(curr_node.right)

    def __print_with_colors(self, curr_node):
        '''Recursively print a subtree (in order), rooted at curr_node
            Printed in PREORDER
            Extracts the color of the node and print it in the format -dataC- where C is B for black and R for red '''
        if curr_node is not self.sentinel:

            if curr_node.color is "red":
                node_color = "R"
            else:
                node_color = "B"

            print(str(curr_node.data)+node_color, end=' ')  # save space
            self.__print_with_colors(curr_node.left)
            self.__print_with_colors(curr_node.right)

    def print_with_colors(self):
        '''Also prints the data of all node but with color indicators'''
        self.__print_with_colors(self.root)
            
            
    def __iter__(self):
        '''Iterates through the tree in order'''
        return self.inorder()

    def inorder(self):
        '''Does inorder traversal of tree'''
        return self.__traverse(self.root, rb_tree.INORDER)

    def preorder(self):
        '''Does preorder traversal of tree'''
        return self.__traverse(self.root, rb_tree.PREORDER)

    def postorder(self):
        '''Does postorder traversal of tree'''
        return self.__traverse(self.root, rb_tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        '''Traverses through through the tree based on
        the traversal type (inorder, preorder, or postorder)'''
        if curr_node is not self.sentinel:
            if traversal_type == self.PREORDER:
                yield curr_node
            yield from self.__traverse(curr_node.left, traversal_type)
            if traversal_type == self.INORDER:
                yield curr_node
            yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type == self.POSTORDER:
                yield curr_node

    def find_min(self):
        '''Travels across the leftChild of every node, and returns the
        node who has no leftChild. This is the min value of a subtree'''
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node

    def find_node(self, data):
        '''Expects a data and returns the Node object for the given data'''
        if self.root:
            res = self.__get(data, self.root)
            if res:
                return res
            else:
                raise KeyError('Error, data not found')
        else:
            raise KeyError('Error, tree has no root')


    def __get(self, data, current_node):
        '''Helper function receives data and a node. Returns the node with
        the given data'''
        if current_node is self.sentinel: # if current_node does not exist return None
            print("couldnt find data: {}".format(data))
            return None
        elif current_node.data == data:
            return current_node
        elif data < current_node.data:
            # recursively call __get with data and current_node's left
            return self.__get( data, current_node.left )
        else: # data is greater than current_node.data
            # recursively call __get with data and current_node's right
            return self.__get( data, current_node.right )
    

    def find_successor(self, data):
        '''Receives data and finds a sucessor node for a node with that data'''
        current_node = self.find_node(data)

        if current_node is self.sentinel:
            raise KeyError

        # Travel left down the rightmost subtree
        if current_node.right:
            current_node = current_node.right
            while current_node.left is not self.sentinel:
                current_node = current_node.left
            successor = current_node

        # Travel up until the node is a left child
        else:
            parent = current_node.parent
            while parent is not self.sentinel and current_node is not parent.left:
                current_node = parent
                parent = parent.parent
            successor = parent

        if successor:
            return successor
        else:
            return None


    def insert(self, data):
        '''Inserts a node into the red black tree and calls
        rb_insert_fixup to fix any red black tree rule violations'''
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            new_node = self.__put(data, self.root)
            self.__rb_insert_fixup(new_node)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
            new_node = self.root
            self.__rb_insert_fixup(new_node)

    def bst_insert(self, data):
        '''Inserts a node into a binary search tree'''
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            self.__put(data, self.root)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
        

    def __put(self, data, current_node):
        '''Helper function that finds the appropriate place to add a node in the tree'''
        if data < current_node.data:
            if current_node.left != self.sentinel:
                new_node = self.__put(data, current_node.left)
            else: # current_node has no child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.left = new_node
        else: # data is greater than or equal to current_node's data
            if current_node.right != self.sentinel:
                new_node = self.__put(data, current_node.right)
            else: # current_node has no right child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.right = new_node
        return new_node

    
    def delete(self, data):
        '''Deletes a node from the red black tree and calls
        rb_delete_fixup to fix any red black tree rule violations'''
        # Same as binary tree delete, except we call rb_delete fixup at the end.
        z = self.find_node(data)
        y = z
        y_org_color = y.color
        if z.left == self.sentinel:
            x = z.right
            # replace z by its right child
            if z.parent == self.sentinel:
                self.root = z.right
            elif z == z.parent.left:
                z.parent.left = z.right
            else:
                z.parent.right = z.right
            z.right.parent = z.parent
        elif z.right == self.sentinel:
            x = z.left
            if z.parent == self.sentinel:
                self.root = z.left
            elif z == z.parent.left:
                z.parent.left = z.right
            else:
                z.parent.right = z.left
            z.left.parent = z.parent
        else:
            y = self.find_successor(z.data)
            y_org_color = y.color
            x = y.right
            if y != z.right:
                if y.parent == self.sentinel:
                    self.root = y.right
                elif y == y.parent.left:
                    y.parent.left = y.right
                else:
                    y.parent.right = y.right
                y.right.parent = y.parent
                y.right = z.right
                y.right.parent = y
            else:
                x.parent = y
            if z.parent == self.sentinel:
                self.root = y
            elif z == z.parent.left:
                z.parent.left = y
            else:
                z.parent.right = y
            y.parent = z.parent
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_org_color == "black":
            self.__rb_delete_fixup(x)










    def left_rotate(self, current_node):
        ''' If there is nothing to rotate with, then raise a KeyError
            if x is the root of the tree to rotate with left child subtree T1 and right child y,
            where T2 and T3 are the left and right children of y then:
            x becomes left child of y and T3 as its right child of y
            T1 becomes left child of x and T2 becomes right child of x
            '''
        if self.root == None or current_node.right.data is None:
            raise KeyError("Cannot perform left rotation on a node with no right child")

        y = current_node.right
        current_node.right = y.left

        if y.left.data != None:
           y.left.parent = current_node

        y.parent = current_node.parent

        if current_node.parent.data == None:
            self.root = y
        elif current_node == current_node.parent.left:
            current_node.parent.left = y
        else:
            current_node.parent.right = y

        y.left = current_node
        current_node.parent = y
    def right_rotate(self, current_node):
        '''If there is nothing to rotate with, then raise a KeyError
            If y is the root of the tree to rotate with right child subtree T3 and left child x,
            where T1 and T2 are the left and right children of x then:
            y becomes right child of x and T1 as its left child of x
            T2 becomes left child of y and T3 becomes right child of y
        '''
        x = current_node
        if self.root == None or current_node.left.data == None:
            raise KeyError("Cannot perform right rotation on a node with no left child")

        y = x.left
        x.left = y.right
        if y.right.data != None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent.data == None:  # x is root
            self.root = y
        elif x == x.parent.right:  # x is right child
            x.parent.right = y
        else:  # x is left child
            x.parent.left = y
        y.right = x
        x.parent = y


    
    def __rb_insert_fixup(self, z):
        '''This function maintains the balancing and coloring property after bst insertion into
        the tree. Please red the code for insert() method to get a better understanding
       '''

        while z.parent.color == "red":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    print(z.parent.parent.data)
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.left_rotate(z.parent.parent)
        self.root.color = "black"






    def __rb_delete_fixup(self, x):
        '''This function maintains the balancing and coloring property after bst deletion
            from the tree. Please read the code for delete() method to get a better understanding.
            refer page 338 of CLRS book and lecture slides for rb_delete_fixup'''
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                if w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.right.color == "black":
                        w.left.color = "black"
                        w.color = "red"
                        self.right_rotate(w)
                        w = x.p.right
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "black" and w.left.color == "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.left.color == "black":
                        w.right.color = "black"
                        w.color = "red"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"




    


    
    