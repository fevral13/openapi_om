from openapi_om.openapi import OpenAPI, Info, License, Contact


def test_openapi():
    openapi = OpenAPI(info=Info(title="title", version="0.1"), paths={})
    expected = {
        "info": {"title": "title", "version": "0.1"},
        "openapi": "3.0.1",
        "paths": {},
        "servers": [{"description": "Default server", "url": "/"}],
    }
    assert expected == openapi.dict(exclude_none=True, by_alias=True)


def test_license():
    _license = License(name="MIT", url="http://license.local/mit")
    expected = {"name": "MIT", "url": "http://license.local/mit"}
    assert expected == _license.dict(exclude_none=True, by_alias=True)


def test_contact():
    contact = Contact(name="Name SecondName", url="http://page.personal/name")
    expected = {"name": "Name SecondName", "url": "http://page.personal/name"}
    assert expected == contact.dict(exclude_none=True, by_alias=True)
