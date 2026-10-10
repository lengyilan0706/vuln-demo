from app import auth


def test_hash_is_stable():
    assert auth.hash_password("x") == auth.hash_password("x")
