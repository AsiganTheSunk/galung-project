import re
from trunk.filemapper import retrieve_module as rmod
from trunk.datastructure.Metadata import Metadata
from Index import Index
from Node import Node

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
                if item.basename in basename:
                    nodelist.append(item)
            return nodelist
        else:
            for item in self.nodes:
                if item.basename in basename and item.parent_basename in parent_basename:
                    node = item
            return [node]

    # todo Falta por hacer la actualizacion
    def update_node_basename(self, basename=None, new_basename=None, parent_basename=None):
        nodelist = self.search(basename=basename)[0]
        #parentNode =  self.search(nodeList.parent_basename)
        nodelist.basename= new_basename
        for child in nodelist.children:
            child.parent_basename = new_basename

    def tree(self, basename):
        subtrees = self.search(basename)[0].children
        for i, val in enumerate(subtrees):
            self.subtree(subtrees[i].basename)

    def subtree(self, basename, parent_basename=None):
        if parent_basename is None:
            nodelist = self.search(basename)
            for i, val in enumerate(nodelist):
                self.subtree(nodelist[i].basename, nodelist[i].parent_basename)
        else:
            nodelist = self.search(basename, parent_basename)[0]
            print ('identifier: '+str(nodelist.identifier), 'basename: '+str(nodelist.basename))
            if nodelist.children is not []:
                for child in nodelist.children:
                    self.subtree(child.basename, child.parent_basename)

    def display(self):
        for item in self.nodes:
            print ('[ID]: ' + str(item.identifier)+' [PATH]: '+str(item.parent_basename)+' ./'+str(item.basename))

    def find_show_seasons(self, key, seasons):
        if key == '':
            return
        index = Index(keyword=key)
        found = []
        for item in self.nodes:
            try:
                for i in range(1, seasons):
                    try:
                        expression = key+' S0'+str(i)
                        aux = re.search(re.escape(expression), item.basename).group(0)
                        if aux:
                            found.append(aux)
                    except:
                        continue
                index.nodes.append(item)
            except:
                continue

        total = (str(len(set(found))))
        print ('[SHOW]: '+key+' [SEASONS]:('+total+'/'+str(seasons)+')')


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


    def create_season_index (self):
        index = Index()
        temp_index = []

        #for item in self.nodes:
            #temp_index.append(item.get_metadata.get_name())
        # todo Aqui tenemos aquellas series que son de nombre unico
        temp = set(temp_index)
        # todo Recuperar el numero de seasons
        # de las seasons recuperadas, generar los directorios que tienen capitulos presentes
        for show in temp:
            self.find_show_seasons(key=show, seasons=rmod.retrieve_number_of_seasons(key=show))

