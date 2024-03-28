# Network Information Retrieval

This Python script retrieves information about the currently active/connected WiFi network on Windows, including the IPv4 address, subnet mask, and WiFi network name (SSID).

## Requirements

- Python 3.x
- Windows operating system (tested on Windows)

## Usage

1. Clone the repository or download the `network_info.py` file.
2. Run the script using Python:

```bash
python network_info.py
```

3. The script will print the following information:

   - WiFi Network Name (SSID)
   - IPv4 Address
   - Subnet Mask
   - Network Range (CIDR notation)

## Functionality

### `get_network_info()`

This function retrieves the IPv4 address, subnet mask, and WiFi network name (SSID) of the currently active/connected WiFi network on Windows.

Returns:
- IPv4 address (str)
- Subnet mask (str)
- WiFi network name (SSID) (str)

If any of the information cannot be retrieved, it returns `None` for the corresponding value.

### `calculate_network_range(ip_address: str, subnet_mask: str) -> str`

This function calculates the network range in CIDR notation based on an IPv4 address and subnet mask.

Args:
- `ip_address` (str): IPv4 address (e.g., "192.168.1.100")
- `subnet_mask` (str): Subnet mask (e.g., "255.255.255.0")

Returns:
- Network range in CIDR notation (str) (e.g., "192.168.1.0/24")

## Note

- This script is specifically designed for Windows operating systems.
- Ensure that the script is executed with administrative privileges to retrieve accurate network information.
