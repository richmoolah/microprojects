'''
from linkedlist import *
from queue import *
from stack import *
from binarytree import *
from heap import *
from graphnode import *
from graphsearch import *
'''
from ds-a import *
from borrowedtree import *


#init data
testList = LinkedList()
node6 = Node(6)
node5 = Node(5)
node4 = Node(4)
node3 = Node(3)
node2 = Node(2)
node1 = Node(1)
testList.head = node5
node5.next = node3
node3.next = node4
node4.next = node1
node1.next = node2
node2.next = node6

#test 
print("Linked List result...")
#testList.deleteNode(9)
testList.insertNode(7, "end")
testList.insertNodeBtwn(8,3,4)
print(testList.printLList())

#print(node1.data)
print("Queue result...")
testQueue = Queue()
testQueue.queueNode(node1)
print(testQueue.peek())
testQueue.queueNode(node2)
testQueue.dequeueNode()
testQueue.queueNode(node3)
print(testQueue.peek())
testQueue.queueNode(node4)
testQueue.queueNode(node5)
testQueue.dequeueNode()
print(testQueue.peek())

print("Stack result...")
testStack = Stack()
testStack.pushNode(node1)
testStack.pushNode(node2)
testStack.pushNode(node3)
print(testStack.peek())
testStack.pushNode(node4)
testStack.pushNode(node5)
print(testStack.peek())
testStack.popNode()
print(testStack.peek())


print("BST result...")
testBST = BinaryTree()
#testBST.updateRoot(1)
testBST.insertNode(testBST.root, 1)
#testBST.visitTree(testBST.root)
testBST.insertNode(testBST.root, 2)
testBST.insertNode(testBST.root, 3)
testBST.insertNode(testBST.root, 4)
testBST.insertNode(testBST.root, 5)
testBST.insertNode(testBST.root, 9)
testBST.insertNode(testBST.root, 7)
testBST.insertNode(testBST.root, 6)
testBST.insertNode(testBST.root, 8)
#testBST.visitTree(testBST.root)
print_tree(testBST.root)
#print(testBST.peek())
print("BST2 result...")
secondBST = BinaryTree()
secondBST.insertNode(secondBST.root, 5)
secondBST.insertNode(secondBST.root, 2)
secondBST.insertNode(secondBST.root, 4)
secondBST.insertNode(secondBST.root, 1)
secondBST.insertNode(secondBST.root, 3)
secondBST.insertNode(secondBST.root, 9)
secondBST.insertNode(secondBST.root, 7)
secondBST.insertNode(secondBST.root, 6)
secondBST.insertNode(secondBST.root, 8)
#secondBST.visitTree(secondBST.root)
print_tree(secondBST.root)
#secondBST.updateRoot()


print("Heap result...")
testHeap = MinHeap()
testHeap.insert_node(5)
testHeap.insert_node(2)
testHeap.insert_node(3)
testHeap.insert_node(4)
testHeap.insert_node(1)
testHeap.swap(2,3)
testHeap.print_heap()



print("Graph result...")
gnode1 = GraphNode(1)
gnode2 = GraphNode(2)
gnode3 = GraphNode(3)
gnode4 = GraphNode(4)
gnode5 = GraphNode(5)
gnode6 = GraphNode(6)
gnode7 = GraphNode(7)
gnode8 = GraphNode(8)
gnode9 = GraphNode(9)
gnode10 = GraphNode(10)
gnode11 = GraphNode(11)
gnode12 = GraphNode(12)
gnode13 = GraphNode(13)
gnode14 = GraphNode(14)
gnode15 = GraphNode(15)
gnode16 = GraphNode(16)
gnode17 = GraphNode(17)
gnode18 = GraphNode(18)
gnode19 = GraphNode(19)
gnode20 = GraphNode(20)
gnode1.update_adj([gnode2, gnode3])
gnode2.update_adj([gnode5])
gnode3.update_adj([gnode4, gnode6, gnode11])
gnode4.update_adj([gnode1])
gnode5.update_adj([gnode6, gnode8])
gnode6.update_adj([gnode7, gnode11])
gnode7.update_adj([gnode8, gnode9])
gnode8.update_adj([gnode6])
gnode9.update_adj([])
gnode10.update_adj([gnode1])
gnode11.update_adj([gnode4, gnode10, gnode12, gnode14, gnode16, gnode17])
gnode12.update_adj([gnode13])
gnode13.update_adj([])
gnode14.update_adj([gnode15])
gnode15.update_adj([gnode13])
gnode16.update_adj([gnode14, gnode20])
gnode17.update_adj([gnode18])
gnode18.update_adj([gnode19])
gnode19.update_adj([gnode17])
gnode20.update_adj([])
#print("DFS result...")
#dfs(gnode1)
print("BFS result...")
bfs(gnode1)

plt.plot([1,2,3,4])

plt.show()
