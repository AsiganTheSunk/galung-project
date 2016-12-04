#!/usr/bin/python

import re

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
        self.node_count+=1

    def add_node(self, basename, parent_basename=None):
        self.add_node_count()
        node = Node(basename,self.node_count)
        node.parent_basename = parent_basename
        #print '[ADDED]: - basename:'+str(node.basename), ' --- parent_basename: '+str(node.parent_basename)
        if parent_basename is not None:
            nodo = self.search(parent_basename)
            nodo[len(nodo)-1].add_child(node)
            #if (nodo[len(nodo)-1].identifier < node.identifier):
            #    nodo[len(nodo)-1].add_child(node)
                #print '[PARENT]: - ID('+ str(nodo[len(nodo)-1].identifier)+') '+str(nodo[len(nodo)-1].basename)
                #print '[_CHILD]: COUNT('+str(len(nodo[len(nodo)-1].children))+') - ID('+ str(node.identifier)+') '+str(node.basename)
        self.nodes.append(node)
        return node


    def season_show_index (self, key, seasons):
        index = Index(keyword=key)
        found = []
        for item in self.nodes:
            try:
                for i in range(1,seasons):
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






    def search(self, basename, parent_basename=None):
        node = None
        nodeList = []
        if parent_basename is None:
            for item in self.nodes:
                if item.basename in basename:
                    nodeList.append(item)
            return nodeList
        else:
            for item in self.nodes:
                if item.basename in basename and item.parent_basename in parent_basename:
                    node = item
            return [node]


    def update_node_basename (self, basename=None, new_basename=None, parent_basename=None):
        nodeList = self.search(basename=basename)[0]
        #parentNode =  self.search(nodeList.parent_basename)
        nodeList.basename= new_basename
        for child in nodeList.children:
            child.parent_basename = new_basename


    def tree(self, basename):
        subtrees = self.search(basename)[0].children
        for i, val in enumerate(subtrees):
            self.subtree(subtrees[i].basename)


    def subtree(self, basename, parent_basename=None):
        if parent_basename  is None:
            nodeList = self.search(basename)
            for i, val in enumerate(nodeList):
                self.subtree(nodeList[i].basename, nodeList[i].parent_basename)
        else:
            nodeList = self.search(basename, parent_basename)[0]
            print ('identifier: '+str(nodeList.identifier), 'basename: '+str(nodeList.basename))
            if nodeList.children is not []:
                for child in nodeList.children:
                    self.subtree(child.basename, child.parent_basename)

    def display(self):
        for item in self.nodes:
            print ('[ID]: '+ str(item.identifier)+' [PATH]: '+str(item.parent_basename)+' ./'+str(item.basename))
