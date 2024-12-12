import re


def parser(output):
    pattern = r"\[\s*\d+\]\s+([\d\.]+-[\d\.]+)\s+sec\s+([\d\.]+\s+[A-Za-z]+)\s+([\d\.]+\s+[A-Za-z]+/sec)"
    matches = re.findall(pattern, output)
    results = []
    for match in matches:
        interval = match[0]
        transfer_value, transfer_unit = match[1].split()
        bandwidth_value, bandwidth_unit = match[2].split()
        results.append({
            "Interval": interval,
            "Transfer": float(transfer_value),
            "TransferUnit": transfer_unit,
            "Bitrate": float(bandwidth_value),
            "BandwidthUnit": bandwidth_unit
        })
    return results