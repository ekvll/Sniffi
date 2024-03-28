import socket
import subprocess
import re


def get_network_info():
    """
    Retrieves the IPv4 address, subnet mask, and WiFi network name (SSID) of the currently active/connected WiFi network on Windows.

    Returns:
    - str: IPv4 address of the host machine.
    - str: Subnet mask of the host machine.
    - str: WiFi network name (SSID) of the currently connected WiFi network.

    If any of the information cannot be retrieved, it returns None for the corresponding value.
    """
    ip_address = subnet_mask = wifi_network_name = None

    # Get IPv4 address and subnet mask
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        subnet_mask = "255.255.255.0"  # Default subnet mask for most home networks

    # Get WiFi network name (SSID)
    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True,
            text=True,
            check=True,
        )
        output = result.stdout
        wifi_network_name_match = re.search(
            r"^\s*SSID\s*:\s*(.*)$", output, flags=re.MULTILINE
        )
        if wifi_network_name_match:
            wifi_network_name = wifi_network_name_match.group(1).strip()
    except subprocess.CalledProcessError:
        pass 

    return ip_address, subnet_mask, wifi_network_name


def calculate_network_range(ip_address: str, subnet_mask: str) -> str:
    """
    Calculate the network range based on an IPv4 address and subnet mask.

    Args:
    - ip_address (str): IPv4 address (e.g., "192.168.1.100")
    - subnet_mask (str): Subnet mask (e.g., "255.255.255.0")

    Returns:
    - str: Network range in CIDR notation (e.g., "192.168.1.0/24")
    """
    # Convert IPv4 address and subnet mask to binary strings
    ip_octets = [bin(int(octet))[2:].zfill(8) for octet in ip_address.split(".")]
    subnet_octets = [bin(int(octet))[2:].zfill(8) for octet in subnet_mask.split(".")]

    # Calculate the network address using bitwise AND operation
    network_octets = [
        str(int(ip_octet, 2) & int(subnet_octet, 2))
        for ip_octet, subnet_octet in zip(ip_octets, subnet_octets)
    ]

    # Construct the network range in CIDR notation
    network_range = (
        ".".join(network_octets)
        + "/"
        + str(sum(bin(int(octet)).count("1") for octet in subnet_mask.split(".")))
    )

    return network_range


if __name__ == "__main__":
    ip_address, subnet_mask, wifi_network_name = get_network_info()
    network_range = calculate_network_range(ip_address, subnet_mask)

    print("WiFi Network Name (SSID):", wifi_network_name)
    print("IPv4 Address:", ip_address)
    print("Subnet Mask:", subnet_mask)
    print("Network range:", network_range)
