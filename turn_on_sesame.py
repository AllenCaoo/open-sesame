import asyncio
from kasa import Discover


def main():
    sesame_dev = None

    def sesame_connected():
        nonlocal sesame_dev
        devices = asyncio.run(Discover.discover())
        for addr, dev in devices.items():
            asyncio.run(dev.update())
            print(f"{addr} >> {dev}")
            if dev.hw_info['dev_name'] == "Wi-Fi Smart Plug With Energy Monitoring":
                sesame_dev = dev

    sesame_connected()
    print("sesame device: ", sesame_dev)
    if sesame_dev:
        while True:
            print('0 to turn off, 1 to turn on')
            response = input('What do you want to do? ')
            if response == '1':
                if sesame_dev.is_on:
                    print('already on')
                else:
                    asyncio.run(sesame_dev.turn_on())
                    asyncio.run(sesame_dev.update())
                    print('sesame successfully turned on')
                    break
            elif response == '0':
                if sesame_dev.is_off:
                    print('already off')
                else:
                    asyncio.run(sesame_dev.turn_off())
                    asyncio.run(sesame_dev.update())
                    print('sesame successfully turned off')
                    break
            else:
                print('Please give proper response')
                print()
    else:
        print('sesame not connected to WIFI')


main()
