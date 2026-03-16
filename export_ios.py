# export_ios.py
import pandas as pd
from jamf_api import get_jamf_token, get_all_ios_devices, get_ios_device_details


def main():
    print("Authenticating with Jamf Pro...")
    token = get_jamf_token()

    print("Retrieving list of iOS devices...")
    devices = get_all_ios_devices(token)

    results = []

    print(f"Found {len(devices)} devices. Fetching details...")
    for device in devices:
        device_id = device.get("id")
        details = get_ios_device_details(token, device_id)
        results.append(details)

    df = pd.DataFrame(results)
    df.to_excel("jamf_ios_devices.xlsx", index=False)

    print("Export complete! File saved as jamf_ios_devices.xlsx")


if __name__ == "__main__":
    main()