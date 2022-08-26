from openapy.openapi import OpenAPI, Info, License, Contact


def test_openapi():
    openapi = OpenAPI(info=Info(title="title", version="0.1"), paths={})
    expected = {
        "info": {"title": "title", "version": "0.1"},
        "openapi": "3.0.1",
        "paths": {},
        "servers": [{"description": "Default server", "url": "/"}],
        "tags": (),
    }
    assert expected == openapi.as_dict()


def test_license():
    _license = License(name="MIT", url="http://license.local/mit")
    expected = {"name": "MIT", "url": "http://license.local/mit"}
    assert expected == _license.as_dict()


def test_contact():
    contact = Contact(name="Name SecondName", url="http://page.personal/name")
    expected = {"name": "Name SecondName", "url": "http://page.personal/name"}
    assert expected == contact.as_dict()
