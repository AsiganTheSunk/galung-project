from Node import Node
from trunk.datastructure.Metadata import Metadata

# todo crear excepciones propias del treeroot

class TreeRoot(object):
    def __init__(self):
        self.dictionary = None
        self.nodes = []
        self.node_count = -1

    def get_nodes(self):
        return self.nodes

    def get_node_count(self):
        return self.node_count

    def add_node_count(self):
        self.node_count += 1

    def add_node(self, basename, metadata=None, parent_basename=None, debug=None):
        self.add_node_count()
        if metadata is None: metadata = Metadata()
        node = Node(basename, self.node_count, metadata)
        node.parent_basename = parent_basename
        if debug:
            print ('[ADDED]: - basename:'+str(node.basename), ' --- parent_basename: '+str(node.parent_basename))
        if parent_basename is not None:
            pnode = self.search(parent_basename)
            pnode[len(pnode)-1].add_child(node)
            if debug:
                print ('[PARENT]: - ID(' + str(pnode[len(pnode)-1].identifier)+') '+str(pnode[len(pnode)-1].basename))
                print ('[_CHILD]: COUNT('+str(len(pnode[len(pnode)-1].children))+') - ID(' + str(node.identifier)+') '+str(node.basename))
        self.nodes.append(node)
        return node

    def search(self, basename, parent_basename=None):
        node = None
        nodelist = []
        if parent_basename is None:
            for item in self.nodes:
                if item.basename == basename:
                    nodelist.append(item)
            return nodelist
        else:
            for item in self.nodes:
                if item.basename == basename and item.parent_basename == parent_basename:
                    node = item
            return [node]

    def tree(self, basename):
        subtrees = self.search(basename)[0].children
        for i, val in enumerate(subtrees):
             self.subtree(subtrees[i].basename, deep=1)

    def subtree(self, basename, parent_basename=None, deep=int):
        if parent_basename is None:
            nodelist = self.search(basename)
            print('--' + str(basename))
            for i, val in enumerate(nodelist):
                self.subtree(nodelist[i].basename, nodelist[i].parent_basename, deep=deep)
        else:
            node = self.search(basename, parent_basename)[0]
            string = '--'*int(deep)
            print (str(string) + ': index: ('+str(node.identifier) + ') - [basename]: '+str(node.basename) + ' [parent]: ' + str(node.parent_basename))
            if node.children is not []:
                for child in node.children:
                    self.subtree(child.basename, child.parent_basename, deep=deep + 1)

    def display(self):
        for item in self.nodes:
            print ('[ID]: ' + str(item.identifier)+' [PATH]: '+str(item.parent_basename)+' ./'+str(item.basename))


    # todo caso de node list, como discriminar, apano para reconstruir el path devuelto
    def get_full_path (self, path , source=None, aux=None):
        if source is None: source = path
        if aux is None: aux = ''
        node = self.search(path)
        node = node[len(node)-1]

        if node.parent_basename is not None:
            aux += '/' + str(node.basename)
            return self.get_full_path(node.parent_basename, source, aux)

        aux += '/' + str(node.basename)
        list = aux.split('/')
        temp = ''
        for i in range (len(list)-1, 0, -1):
            temp += '/' + list[i]
        return temp

    def update_parent_node_byindex(self, index, parent):
        '''
        :param index: node identifier
        :param parent: new parent basename
        :type index: int
        :type parent: str
        '''

        tnode = pnode = Node
        for node in self.get_nodes():
            if node.identifier == index:
                pnode = self.search(basename=node.parent_basename)[0]
                for child in pnode.children:
                    if child.basename == node.basename:
                        tnode = child
                        pnode.remove_child(child_basename=child.basename)
                tnode.set_parent_basename(parent)
                node.set_parent_basename(parent)
                new_parent = self.search(basename=parent)[0]
                new_parent.add_child(child=tnode)


    def build_full_path_tree(self):
        nodes = self.get_nodes()
        list = []
        for node in nodes:
            list.append(self.get_full_path(node.basename))

        return list

    def tree_path(self):
        subtrees = self.nodes[0].children
        for i, val in enumerate(subtrees):
             self.subtree_path(subtrees[i].basename, deep=1)

    def subtree_path(self, basename, parent_basename=None, deep=int):
        if parent_basename is None:
            nodelist = self.search(basename)
            for i, val in enumerate(nodelist):
                self.subtree_path(nodelist[i].basename, nodelist[i].parent_basename, deep=deep)
        else:
            node = self.search(basename, parent_basename)[0]
            print 'index('+ str(node.identifier) +') - deep: ' + str(deep) + ' - ' + self.get_full_path(node.basename)
            if node.children is not []:
                for child in node.children:
                    self.subtree_path(child.basename, child.parent_basename, deep=deep + 1)




    #
    # def update_parent_node (self, basename, parent):
    #     node = self.search(basename=basename)[0]                        # recupero el nodo
    #     current_parent = node.parent_basename                           # guardo el nombre del padre actual
    #     node.parent_basename = parent                                   # asigno new_parent_basename al parent_basename del nodo buscado
    #
    #     parent_node = self.search(basename=current_parent)[0]           # busco el nodo padre
    #     self.remove_child_node (node=parent_node, basename=basename)    # elimino la aparicion del nodo hijo en su lista
    #
    #     new_parent = self.search(basename=parent)[0]                    # busco el nuevo nodo padre
    #     new_parent.add_child_node(node=node)                            # inserto el nodo en su lista de hijos
