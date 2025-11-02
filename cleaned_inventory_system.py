"""
Inventory management system for tracking stock items.

This module provides functions to add, remove, and query inventory items,
as well as load and save inventory data to/from JSON files.
"""

import json
from datetime import datetime


class InventoryManager:
    """Manages inventory stock data."""

    def __init__(self):
        """Initialize an empty inventory."""
        self.stock_data = {}

    def add_item(self, item="default", qty=0, logs=None):
        """
        Add a quantity of an item to the stock.

        Args:
            item: The name of the item to add (default: "default")
            qty: The quantity to add (default: 0)
            logs: Optional list to append log messages to (default: None)
        """
        if logs is None:
            logs = []
        if not item:
            return
        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        logs.append(f"{datetime.now()}: Added {qty} of {item}")

    def remove_item(self, item, qty):
        """
        Remove a quantity of an item from the stock.

        Args:
            item: The name of the item to remove
            qty: The quantity to remove
        """
        try:
            self.stock_data[item] -= qty
            if self.stock_data[item] <= 0:
                del self.stock_data[item]
        except KeyError:
            print(f"Error: {item} not found in inventory.")

    def get_qty(self, item):
        """
        Get the current quantity of an item.

        Args:
            item: The name of the item to query

        Returns:
            The quantity of the item in stock
        """
        return self.stock_data[item]

    def load_data(self, file="inventory.json"):
        """
        Load inventory data from a JSON file.

        Args:
            file: The path to the JSON file to load (default: "inventory.json")
        """
        with open(file, "r", encoding="utf-8") as f:
            self.stock_data = json.load(f)

    def save_data(self, file="inventory.json"):
        """
        Save the current inventory data to a JSON file.

        Args:
            file: The path to the JSON file to save (default: "inventory.json")
        """
        with open(file, "w", encoding="utf-8") as f:
            json.dump(self.stock_data, f)

    def print_data(self):
        """
        Print a report of all items in the inventory.
        """
        print("Items Report")
        for i in self.stock_data:
            print(i, "->", self.stock_data[i])

    def check_low_items(self, threshold=5):
        """
        Check for items with quantity below a threshold.

        Args:
            threshold: The minimum quantity threshold (default: 5)

        Returns:
            A list of item names that are below the threshold
        """
        result = []
        for i in self.stock_data:
            if self.stock_data[i] < threshold:
                result.append(i)
        return result


def main():
    """
    Main function to demonstrate the inventory system.
    """
    inventory = InventoryManager()
    inventory.add_item("apple", 10)
    inventory.add_item("banana", -2)
    inventory.add_item(123, "ten")  # invalid types, no check
    inventory.remove_item("apple", 3)
    inventory.remove_item("orange", 1)
    print("Apple stock:", inventory.get_qty("apple"))
    print("Low items:", inventory.check_low_items())
    inventory.save_data()
    inventory.load_data()
    inventory.print_data()


main()
