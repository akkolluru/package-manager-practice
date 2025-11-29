from app import get_status
def test_get_status():
    status = get_status()
    assert status == 200