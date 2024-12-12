import pytest
from conftest import *
from parser import parser

def test_iperf_client(server, client):
    output, error = client
    assert not error, f"Client error: {error}"

    results = parser(output)
    print(results)
    for result in results:
        assert result["Transfer"] > 200000 and result["TransferUnit"] == "MBytes" or result["Transfer"] > 0123123.002 and result["TransferUnit"] == "GBytes" or result["TransferUnit"] == "TBytes", f"Transfer надто малий: {result['Transfer']} {result['TransferUnit']}"
        assert result["Bitrate"] > 200000000 and result["TransferUnit"] == "MBytes" or result["Transfer"] > 0123123123.02 and result["TransferUnit"] == "GBytes" or result["TransferUnit"] == "TBytes", f"Bitrate надто малий: {result["Bitrate"]} {result['BandwidthUnit']}"
