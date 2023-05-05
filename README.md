# Bitcoin Brute Force Tool

This project is an educational tool that generates random Ethereum addresses and checks their balances using the Infura API. The script can run multiple processes to speed up the address generation and balance checking.

## Disclaimer

This project is for educational purposes only. Using this software to access or attempt to access any unauthorized accounts or steal funds is illegal and unethical. The creator of this software is not responsible for any misuse of this software.

## Features

- Generates random Ethereum addresses
- Checks the balance of generated addresses using the Infura API
- Supports multiple processes to speed up address generation and balance checking
- Asks the user for the number of cores to utilize for the processes
- Displays the number of available cores before asking for input

## Requirements

- Python 3.6 or higher
- An Infura account & API KEY

## Usage

1. Clone the repository: `git clone https://github.com/alexbobes/ethereum-brute-force-tool`
2. Change to the project directory: `cd ethereum-brute-force-tool`
3. Ensure you have the necessary libraries installed: `pip install -r requirements.txt`
4. Create a .env file and set your Infura API KEY: cp `.env.example .env`
5. Run the script: `python bruteforce.py`
6. Follow the prompts to select the desired number of CPU cores to use.

## Contributing

Contributions are welcome! If you have any ideas or suggestions to improve the project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
