from main.filemapper.datastructure import TreeRoot as tr


# TreeRoot create Tests
def test0_create_tree_root():
    assert tr.TreeRoot() != None


# TreeRoot get_nodes Tests
def test0_get_nodes():
    assert tr.TreeRoot().get_nodes() == []


# TreeRoot add_node_count Tests
def test0_add_node_count():
    tree = tr.TreeRoot()
    tree.add_node_count()
    tree.get_node_count() != -1


# TreeRoot add_nodes Tests
def test0_add_nodes():
    tree = tr.TreeRoot()
    tree.add_node(basename='root')
    tree.get_node_count() != -1


# TreeRoot search Tests
def test0_search():
    return


# TreeRoot update_parent_by_index Tests
def test0_update_parent_by_index():
    tree = tr.TreeRoot()
    tree.add_node(basename='root')
    tree.add_node(basename='node0', parent_basename='root')
    tree.add_node(basename='node1',parent_basename='node0')
    tree.update_parent_node_by_index(index=2, parent='root')
    tree.search(basename='node1', parent_basename='root')


# TreeRoot get_full_path Tests
def test0_get_full_path():
    return


# TreeRoot build_full_path_tree Tests
def test0_buid_full_path_tree():
    return

