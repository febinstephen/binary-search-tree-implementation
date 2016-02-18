class TreeNode:

    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftchild(self):
        return self.parent and sel.parent.leftChild == self

    def isRightchild(self):
        return self.parent and sel.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def splitOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.rightChild
                self.leftChild.parent = self.parent
            else:
                 if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                 else:
                    self.parent.rightChild = self.rightChild
                 self.rightChildParent = self.parent
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem





class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        """
        Checks whether the tree is empty if not calls _put()

        else if not set root to an instance of Treenode class

        """
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        """

        """
        if key > currentNode.key:
            if currentNode.rightChild:
                _put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent = currentNode)
        elif key < currentNode.key:
            if currentNode.leftChild:
                _put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent = currentNode)

    def __setitem__(self, k, v):
        """
        """
        self.put(k, v)

    def get(self, key):
        """
        """
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        """
        """
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key > currentNode.key:
             return self._get(key, currentNode.rightChild)
        else:
            return self._get(key, current.leftChild)

    def __getitem__(self, key):
        """
        """
        return self.get(key)

    def __contains__(self, key):
        """
        """
        if self._get(key, self.root):
            return True
        else:
            return False
    def delete(self, key):
        """
        """
        if self.size > 1:
            nodeToRemove = _get(self, key)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -+ 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, key not in tree")

    def __delitem__(self, key):
        """
        """
        self.delete(key)


    def remove(currentNode):
        """
        """
        if currentNode.isLeaf(): #1st case node has no children 
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): #interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            current.payload = succ.payload
        else: #node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = cunrrentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                            currentNode.leftChild.payload,currentNode.leftChild.leftChild,
                            currentNode.leftChild.rightChild)
            else:
                 if currentNode.isLeftChild():
                    currentNode.righttChild.parent = currentNode.parent
                    currentNode.parent.leftChild = cunrrentNode.rightChild
                 elif currentNode.isRightChild():
                    currentNode.righttChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                 else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                            currentNode.righttChild.payload,currentNode.rightChild.leftChild,
                            currentNode.righttChild.rightChild)


mytree = BinarySearchTree()
mytree[3] = "red"
mytree[6] = "apple"
print(mytree[3])
print(mytree[6])
