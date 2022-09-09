from openapi_om import Tag


def test_tag():
    tag = Tag(name="Orders")
    expected = {"description": "", "name": "Orders"}
    assert expected == tag.dict(exclude_none=True, by_alias=True)
