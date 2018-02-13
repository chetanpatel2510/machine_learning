from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'c:/Program Files (x86)/Graphviz2.38/bin/'
dot = Digraph(comment='The Round Table')
globalNodes = [];
count = 0;
def display(mytree) :
    firstKey = next(iter(mytree));
    dot.node(firstKey, firstKey)
    globalNodes.append(firstKey);
    if isinstance(mytree[firstKey], dict):
        traverseTree(mytree[firstKey], firstKey, firstKey)


def traverseTree(mytree, parentkey, grandParentKey):
    global count;
    for key in mytree:
        
        if isinstance(mytree[key],dict) :
            if (parentkey != grandParentKey):
               dot.edge(str(grandParentKey), str(key), str(parentkey),constraint='false');
            traverseTree(mytree[key], key, parentkey)
        else:
            nodeName = mytree[key];
            if mytree[key] in globalNodes:
                nodeName = str(nodeName) + str(count);
            globalNodes.append(nodeName);
            #dot.edge(str(grandParentKey), str(parentkey), str(key) ,constraint='false')
            #dot.node(nodeName, nodeName)E
            dot.edge(str(parentkey), nodeName, str(key) ,constraint='false')
            
     
mytree =    {'Wings': {0: {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}, 2: 'maybe'}}    
display(mytree);
print(dot.source) 
dot.render('test-output/round-table.gv', view=True)  
#{'Wings': {0: {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}, 2: 'maybe'}}  
#{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}, 2: 'maybe'}}
#{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}};  