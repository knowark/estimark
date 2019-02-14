

def test_rst_loader_instantiation(rst_loader):
    assert rst_loader is not None


def test_rst_loader_load(rst_loader):
    rst_loader.load()

    assert len(rst_loader.nodes) > 0
    assert isinstance(rst_loader.nodes, dict)
