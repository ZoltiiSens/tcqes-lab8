import paramiko
import pytest

server_ip = "127.0.0.1"  # Localhost for server and client
username = "zoltiisen"
password = "Roma090703"

try:
    client = paramiko.SSHClient()
    print(client)  # Debug: Print client object
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=server_ip, username=username, password=password)
    print("Connected")  # Debug: Indicate successful connection
    
    # Start iperf server
    stdin, stdout, stderr = client.exec_command("iperf -s")
    print("client yielded")  # Debug: Indicate command execution
    
    # Ensure all streams are consumed and closed
    stdout.channel.recv_exit_status()  # Wait for command to complete
    stdin.close()
    stdout.close()
    stderr.close()
    
    client.exec_command("killall iperf")
    client.close()
    del stdin, stdout, stderr, client
    print("SSH client connection closed.")  # Debug: Indicate cleanup
except Exception as e:
    pytest.fail(f"Failed to setup server: {e}")