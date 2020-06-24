

def test_rst_loader_instantiation(rst_loader):
    assert rst_loader is not None


def test_rst_loader_load(rst_loader):
    rst_loader.load()

    assert len(rst_loader.nodes) > 0
    assert isinstance(rst_loader.nodes, list)


def test_rst_loader_load_if_not_initialized(rst_loader):
    assert len(rst_loader.nodes) > 0
    assert isinstance(rst_loader.nodes, list)


def test_rst_loader_load_custom_id(rst_loader):
    for node in rst_loader.nodes:
        if node.get('name') == '4.1 Close Project':
            assert node['id'] == 'custom_4.1'
            break
    else:
        assert False
