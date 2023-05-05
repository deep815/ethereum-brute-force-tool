from concurrent.futures import ProcessPoolExecutor
import os
from dotenv import load_dotenv
from web3 import Web3
import random
import multiprocessing

load_dotenv()

INFURA_API_KEY = os.getenv("INFURA_API_KEY")

if not INFURA_API_KEY:
    raise ValueError("Infura API KEY is not set in the .env file")

w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_API_KEY}'))

def generate_and_check_eth_address():
    while True:
        private_key = ''.join([f'{random.randint(0, 15):x}' for _ in range(64)])
        account = w3.eth.account.privateKeyToAccount(private_key)
        address = account.address
        balance = w3.eth.getBalance(address)
        print(f'Instance: 1 - Generated: {address} balance: {balance}')
        if balance > 0:
            with open('found.txt', 'a') as result:
                result.write(f'{private_key}\n')
            print(f'Address: {address} has balance: {balance} wei')

def main():
    num_cores = multiprocessing.cpu_count()
    print(f"You have {num_cores} cores available.")
    print("How many cores do you want to use?")
    cpu_cores = int(input('> '))

    with ProcessPoolExecutor(max_workers=cpu_cores) as executor:
        for _ in range(cpu_cores):
            executor.submit(generate_and_check_eth_address)

if __name__ == '__main__':
    main()