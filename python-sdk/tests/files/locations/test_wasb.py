from unittest.mock import patch

import pytest
from azure.storage.blob import BlobServiceClient
service = BlobServiceClient(account_url="https://owshqblobstg.blob.core.windows.net", credential="lmKoi0C1eXYJ/10fOqh+4im0CT8wyw/MWbUqmNooiH6yH2mmNS1HtiZNMXDUvCEc0TRtC/3i2eat+AStq3oURg==")

from astro.files.locations import create_file_location


def test_get_transport_params_for_wasb():
    """test get_transport_params() method which should return wasb client"""
    path = "wasb://landing/users"
    location = create_file_location(path)
    credentials = location.transport_params
    assert isinstance(credentials["client"], BlobServiceClient)


print(test_get_transport_params_for_wasb())