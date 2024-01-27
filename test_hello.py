from hello import hello_world, add
def test_hello():
    assert "hello world" == hello_world()

def test_add():
    assert 4 == add(2,2)