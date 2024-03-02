import sys
import requests
import csv
import json
from datetime import datetime

def get_node_info(node_address):
    # API endpoint for node leaderboard
    api_url = "https://shdw-rewards-oracle.shdwdrive.com/node-leaderboard"
    
    # Fetch JSON data from the API
    response = requests.get(api_url)
    data = response.json()

    # Find the node in the data
    node_info = next((node for node in data["nodes"] if node["node_id"] == node_address), None)

    if node_info:
        # Get rank, rewards, and status for the specified node
        rank = data["nodes"].index(node_info) + 1
        rewards = int(node_info["total_rewards"]) / 1_000_000_000  # Divide by 1 billion
        status = node_info["status"]
        return rank, rewards, status
    else:
        return None


def record_node_data(data_filename, node_address, rank, rewards, status):
    try:
        with open(data_filename, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Node Address", "Rank", "Rewards", "Status"])
    except FileExistsError:
        pass  # file already exists, no need to create again
    
    with open(data_filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), node_address, rank, rewards, status])

if __name__ == "__main__":
    # pre-defined file
    filename = "nodes.txt"  # or "nodes.json"
    data_filename = "node_rankings.csv"
    nodes = []
    current_time = datetime.now()

    # read node address from file
    if filename.endswith('.json'):
        with open(filename, 'r') as file:
            nodes = json.load(file)
    elif filename.endswith('.txt'):
        with open(filename, 'r') as file:
            nodes = file.read().splitlines()
    else:
        print("Unsupported file format. Please use a .json or .txt file.")
        sys.exit(1)

    # print column name and define width
    print("====================================")
    print(f"Current Timestamp: {current_time}")
    print("------")
    print(f"{'Node Address':<50}{'Rank':<8}{'Rewards':<20}{'Status'}")

    # check and print nodes stats
    total_rewards = 0  # initial total rewards
    for node_address in nodes:
        result = get_node_info(node_address)
        if result:
            rank, rewards, status = result
            total_rewards += rewards  # accumulate rewards
            # print nodes info that found
            print(f"{node_address:<50}{rank:<8}{rewards:<20}{status}")
            # record stat to CSV file
            record_node_data(data_filename, node_address, rank, rewards, status)
        else:
            # print nodes that not found
            print(f"{node_address:<50}{'Not found':<8}{'Not found':<20}{'Not found'}")
    print("------")
    print(f"{'Total Rewards: ':<58}{total_rewards:<20}")
    print("====================================")
