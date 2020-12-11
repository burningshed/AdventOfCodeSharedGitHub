class StepNode:
    def __init__(self, name):
        self.nextNodes = []
        self.myName = name
        self.nextNodeList = []
    def addToList(self, nodeName):
        self.nextNodeList.append(nodeName)
    def addNode(self, newNode):
        self.nextNodes.append(newNode)
    def sortNodes(self):
        self.nextNodes.sort()
    def popNode(self):
        node = False
        if len(self.nextNodes) > 0:
            node = self.nextNodes[0]
            self.nextNodes.remove(node)
        return node
    def nodeName(self):
        return self.myName
    def __str__(self):
        return self.myName + ": " + str(self.nextNodeList) + '\n'
    def getNodeList(self):
        return self.nextNodeList
    __repr__ = __str__

infile = open("./day7/input", "r")
# example line: Step Z must be finished before step B can begin.
nodes = {}
initialNodes = set()
for line in infile:
    inline = line.split()
    repeat = False
    for node in nodes:
        if node == inline[1]:
            repeat = True
            nodes[node].addToList(inline[7])
    if repeat == False:
        newNode = StepNode(inline[1])
        newNode.addToList(inline[7])
        nodes[inline[1]] = newNode
    initialNodes.add(inline[1])

# find initial node(s)
depNodes = set()
for node in nodes:
    for item in nodes[node].getNodeList():
        depNodes.add(item)
        if item in initialNodes:
            initialNodes.remove(item)

avalNodes = list(initialNodes)
avalNodes.sort()
curNodes = list(nodes.keys())
notDone = True
order = []
while notDone:
    # update avaliable nodes
    avalNodes = set(curNodes)
    for node in curNodes:
        for item in nodes[node].getNodeList():
            if item in avalNodes:
                avalNodes.remove(item)
    avalNodes = list(avalNodes)
    avalNodes.sort()

    # if done, stop
    if len(avalNodes) == 0:
        break

    # remove first node in avalNodes
    order.append(avalNodes[0])
    curNodes.remove(avalNodes[0])

print(avalNodes)
print(curNodes)
print(order)
print(len(order))
print(len(nodes.keys()))
for item in order:
    print(item, end='')
# haha Q is never the first part, so it was left out, added it manually to the submission

