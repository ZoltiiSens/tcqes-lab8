import paramiko
import pytest
import subprocess
import os
import time


server_ip = "127.0.0.1"
username = "zoltiisen"
password = os.getenv('PASSWORD')


@pytest.fixture(scope="function")
def server():
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=server_ip, username=username, password=password)
        print("SSH connected.")
        
        stdin, stdout, stderr = client.exec_command("iperf -s")
        print("iperf server started.")
        
        time.sleep(1)
        yield client

        client.exec_command("killall iperf")
        stdin.close()
        stdout.close()
        stderr.close()
        client.close()
        print("SSH client connection closed.")
    except Exception as e:
        pytest.fail(f"Failed to setup server: {e}")


@pytest.fixture(scope="function")
def client(server):
    try:
        process = subprocess.Popen(
            ["iperf", "-c", server_ip, "-t", "3"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, error = process.communicate()
        yield output, error
    except Exception as e:
        pytest.fail(f"Failed to setup client: {e}")
