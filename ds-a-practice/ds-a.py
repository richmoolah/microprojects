#practice using data structures and several algorithms
#compiled all classes into one

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None    
    

class BinaryNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.val = data
    

class GraphNode:
    def __init__(self, data, adj=[], visited=0):
        self.data = data
        self.adj = adj
        self.next = None
        self.visited = visited
    
    def print_node(self):
        return self.data
    
    def print_adj(self):
        return self.adj

    def update_adj(self, arr):
        self.adj = arr

class LinkedList:
  def __init__(self):
    self.head = None

  def getNodeValue(self, node):
    return node.data

  def deleteNode(self, key):
    headnode = self.head
    if headnode.data == key:
      headnode.data = None
      self.head = headnode.next
    else:
      prevnode = headnode
      headnode = headnode.next
      while headnode != None:
        #print(prevnode.data, headnode.data)
        if headnode.data == key:
          prevnode.next = headnode.next
          headnode = None
        else:
          prevnode = headnode
          headnode = headnode.next
    
  def insertNode(self, key, placement):
    insertnode = Node(key)
    headnode = self.head
    if placement == "start":
      insertnode.next = self.head
      self.head = insertnode
    if placement == "end":
      while headnode != None:
        #print(headnode.data)
        if headnode.next == None:
          headnode.next = insertnode
          break
        else:
          headnode = headnode.next

  def insertNodeBtwn(self, key, front, back):
    frontnode = self.head
    backnode = self.head.next
    while backnode != None:
      if frontnode.data == front and backnode.data == back:
        insertnode = Node(key)
        frontnode.next = insertnode
        insertnode.next = backnode
        break
      else:
        backnode = backnode.next
        frontnode = frontnode.next
        
  def printLList(self):
    nodeList = []
    headnode = self.head
    while headnode != None:
      #print(headnode.data)
      nodeList.append(headnode.data)
      #print(headnode.data)
      headnode = headnode.next
    return nodeList

class BinaryTree:
  def __init__(self):
    self.root = None

  #def rebalance(self, currNode):
    #while 

  def visitTree(self, currNode):
    if currNode != None:
      self.visitTree(currNode.left)
      print(currNode.data)
      self.visitTree(currNode.right)

  def insertNode(self, nodeRoot, data):
    
    if self.root == None:
      self.root = BinaryNode(data)
    elif nodeRoot == None:
      #return nodeRoot(data)
      return BinaryNode(data)
    else:
      if nodeRoot.data == data:
        return nodeRoot
      elif nodeRoot.data < data:
        nodeRoot.right = self.insertNode(nodeRoot.right, data)
      else:
        nodeRoot.left = self.insertNode(nodeRoot.left, data)
      return nodeRoot

  def updateRoot(self, data):
    self.root = BinaryNode(data)

  def peek(self):
    return self.root.data
    
class MinHeap:
    def __init__(self):
        self.arr = []
        self.root = None

    def insert_node(self, val):
        self.arr.append(val)
        self.sift_up(val)
        
    def sift_up(self, curr_node):
        parent_pos = self.arr.index(curr_node)//2
        child_pos = self.arr.index(curr_node)
        while self.arr[child_pos] < self.arr[parent_pos]:
            self.swap(self.arr.index(curr_node),(self.arr.index(curr_node)//2))
            child_pos = parent_pos
            parent_pos = parent_pos//2

        
    def swap(self, first_pos, second_pos):
        self.arr[first_pos], self.arr[second_pos] = self.arr[second_pos], self.arr[first_pos]

    def print_heap(self):
        print(self.arr)

class Queue:
    def __init__(self):
        self.frontNode = None
        self.backNode = None

    def queueNode(self, newNode):
        #newNode = Node(key)
        if isinstance(newNode, GraphNode) or isinstance(newNode, Node):
            if self.backNode != None:
                self.backNode.next = newNode
            self.backNode = newNode
            if self.frontNode is None:
                self.frontNode = self.backNode
            else:
                return
        

    def dequeueNode(self):
        if self.frontNode is None:
            return
        data = self.frontNode
        self.frontNode = self.frontNode.next
        if self.frontNode is None:
            self.backNode = None
        return data

        
    def peek(self):
        return self.frontNode.data

    def isEmpty(self):
        if self.frontNode == None:
            return True
        else:
            return False

    def printQueue(self, currNode):
        arr = []
        while currNode != None:
            arr.append(currNode.data)
            currNode = currNode.next
        print(arr)

class Stack:
  def __init__(self):
     self.topNode = None
  
  def pushNode(self, newNode):
    if isinstance(newNode, Node):
      if self.topNode == None:
        self.topNode = newNode
      else:
        newNode.next = self.topNode
        self.topNode = newNode
    else:
      return

  def popNode(self):
    if self.topNode == None:
      return
    self.topNode = self.topNode.next

  def peek(self):
    return self.topNode.data
 

def dfs(curr_node):
    if curr_node == None:
        return
    print(curr_node.print_node())
    curr_node.visited = 1
    for n in curr_node.adj:
        if n.visited == 0:
            dfs(n)

def bfs(curr_node):
    order = Queue()
    #print(order.isEmpty())
    curr_node.visited = 1
    order.queueNode(curr_node)
    print(curr_node.data)
    #order.printQueue(curr_node)
    #print(order.isEmpty())
    #print(curr_node.data)
    #print(order.frontNode.data)
    
    while order.isEmpty() != True:
        #print(order.isEmpty())
        #print(curr_node.data)
        
        next_node = order.dequeueNode()
        next_node.visited = 1
        order.printQueue(next_node)
        print("Dequeued " + str(next_node.data))
        #print(order.isEmpty())
        #print(next_node.adj)
        for n in next_node.adj:
            #print(n.visited)
            if n.visited == 0:
                print("Adding " + str(n.data) + " to queue")
                n.visited = 1
                #print("Node " + str(n.data) + " visited " + str(n.visited))
                order.queueNode(n)
                #print(order.peek())
