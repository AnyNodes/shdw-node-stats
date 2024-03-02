# shdw-node-stats

This Python script, `NodeStats.py`, is designed to fetch and record information about blockchain nodes. It retrieves data such as the node's rank, total rewards, and status from a specified API endpoint, then records this information in a CSV file.

## Installation

To use this script, ensure you have Python installed on your system (version 3.8 or later is recommended). You will also need to install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Prepare a file named `nodes.txt` or `nodes.json` containing the addresses of the nodes you wish to query. For a `.json` file, the addresses should be in an array format. For a `.txt` file, list each address on a new line.

2. Run the script using Python from the terminal or command prompt:

```bash
python NodeStats.py
```

The script will output the information for each node to the console and record the data in a CSV file named `node_rankings.csv`.

## File Formats Supported

- **JSON (.json):** Should contain an array of node addresses.
- **Text (.txt):** Should contain node addresses, one per line.

## Output

`NodeStats.py` generates a CSV file named `node_rankings.csv`, which includes the following columns: Timestamp, Node Address, Rank, Rewards, and Status. The console output will display the node information and the total rewards accumulated by the nodes listed in the input file.

## Community Contribution

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](./LICENSE) for more information.

## Note

This script is intended for educational and demonstration purposes. It showcases how to interact with web APIs, process data in Python, and write output to a CSV file. Ensure you have the necessary permissions to use the API and data.
