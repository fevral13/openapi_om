from openapy import Tag


def test_tag():
    tag = Tag(name="Orders")
    expected = {"description": "", "name": "Orders"}
    assert expected == tag.as_dict()
