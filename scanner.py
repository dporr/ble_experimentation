import asyncio
from bleak import BleakScanner


devices = {}
MAX_DEVICES = 50

async def main():
    stop_event = asyncio.Event()
    def callback(device, advertisement_data):
        print("New device... ", len(devices), " ---", device.name)
        devices[device.address] = {"name": device.name, "advertisement_data": advertisement_data}
        #This smells wrong... Need to learn async progra=mming properly
        if(len(devices) >= MAX_DEVICES): stop_event.set()

    async with BleakScanner(callback) as scanner: 
        print("Scanning...")
        await stop_event.wait()
    resolve_mac()


#Potentially method, must run in a separate thread
def resolve_mac():
     with open("mac-vendors.csv") as file:
        for line in file.readlines():
            for device in devices.keys():
                device_s = device[:8]
                prefix, vendor = line.split(",")[:2]
                if(device_s==prefix): print(device_s, device, prefix, vendor)





if __name__ == '__main__':
    asyncio.run(main())

