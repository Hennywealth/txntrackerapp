from web3.auto import Web3
import asyncio
bsc = ""
w3 = Web3(Web3.WebsocketProvider(bsc))
print(w3.isConnected())


def handle_event(event):
    print(event)
async def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            txn = event.hex()
            my_addresses = ['0x49c696f008e58a2a9cbc31c3cbe59639a4d3bb20', '0x12f56bddbfe5dbd9b30a4e3d9c9e4ea2091b73f5', '0x861ef7bdcfca685001ef1be823f8e87ddca8d38a', '0x27e6ddf2d70eeb50ff70db7ca69cb8daf8840991',
                             '0x9cef5d9aa7b687d7e36b9c4ca38e91df2b7d9846', '0x3b9bA781797b57872687Ce5d5219A1A4Bc0e85ea', '0xad8959ca7b5a1e76a99965e40838dbebe255ca23', '0xC7B702ee7C5b63BD5fF534FaAA82320CaB2B2c0']

            data = w3.eth.getTransaction(txn)
            
           
            if data["from"] in my_addresses:

                print(data)
            else:
                print('no address found')
            
            print(data)
          
        await asyncio.sleep(poll_interval)
    

def main():
    block_filter = w3.eth.filter('pending')
    tx_filter = w3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(block_filter, 2),
                log_loop(tx_filter, 2)))
    finally:
        loop.close()

if __name__ == '__main__':
    main()