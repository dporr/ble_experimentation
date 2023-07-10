import argparse
import asyncio
import os
from bleak import BleakClient

TARGET = os.getenv("BLE_CTF_MAC")
srvs = ""
gatt_service_collection = ""

async def main(args):
    global gatt_service_collection
    async with BleakClient(TARGET) as device:
        gatt_service_collection = device.services
        for srvs in gatt_service_collection:
            print("{name}",srvs.description)
            print("{handle}",hex(srvs.handle))
            print("{uuid}",srvs.uuid)
            print("{path}",srvs.path)
            print("{obj}",srvs.obj)
    uuid = resolve_hanlde(args.handle)
    # if args.write:
    #     
    # if args.read:
    #     pas

def resolve_hanlde(handle):
    uuid = ""
    for srvs in gatt_service_collection:
        print(handle,"----",srvs.handle,handle == srvs.handle )
        if(handle == srvs.handle):
            print(handle,"----",srvs.handle, srvs.uuid)
            uuid = srvs.uuid
    return uuid

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--handle",
        help="Get a numeric handle and map to corresponding UUID",
    )
    args = parser.parse_args()
    asyncio.run(main(args))