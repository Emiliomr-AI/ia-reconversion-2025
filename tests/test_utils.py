from src.common.utils import slugify


def test_slugify_basic():
    assert slugify("Hello World!") == "hello-world"
