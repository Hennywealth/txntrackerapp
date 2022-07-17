from celery import shared_task
from time import sleep
from web3.auto import Web3
from .models import Address
bsc = "wss://bsc-dataseed3.defibit.io/ws"
w3 = Web3(Web3.WebsocketProvider(bsc))

@shared_task(bind=True)
def log_loop(self,  event_filter, poll_interval):
    global w3
    
    if event_filter == "block_filter":
        print(event_filter)
        event_filter = w3.eth.filter('pending')
    elif event_filter == 'tx_filter':
        print(event_filter)
        event_filter = w3.eth.filter('pending')
    else :
        pass
    
    while True:
        for event in event_filter.get_new_entries():
            txn = event.hex()
            data = w3.eth.getTransaction(txn)

            res = Address.objects.filter(address = data["from"])
            if len(list(res)) > 0:

                print(data)
            else:
                print('no address found')
            print(data)
           


        


    
    




