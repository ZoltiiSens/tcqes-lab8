import subprocess
import re


def client(server_ip="test_data"):
    try:
        process = subprocess.Popen(
            ["iperf", "-c", server_ip, "-t", "3"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, error = process.communicate()
        return output, error
    except Exception as e:
        return None, str(e)


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


def main():
    server_ip = input("Enter ip address: ")
    if server_ip == "":
        output, error = client()
    else:
        output, error = client(server_ip)

    if error:
        print(f"Error: : {error}")
    else:
        print("Final data:")
        parsed_data = parser(output)
        for entry in parsed_data:
            if entry["Transfer"] > 2 and entry["Bitrate"] > 20:
                print(entry)


if __name__ == "__main__":
    main()
