from openapy.utils import remove_nulls


def test_remove_nulls():
    source_dict = {
        "key1": [
            {
                "subkey1": None,
                "subkey2": {"subkey4": None},
                "subkey3": [None],
            }
        ],
        "key2": None,
    }

    target_dict = {
        "key1": [
            {
                "subkey2": {},
                "subkey3": [None],
            }
        ],
    }
    remove_nulls(source_dict)
    assert source_dict == target_dict
