class Inventory:

    def __init__(self, __capacity):
        self.__capacity = __capacity
        self.items = []

    def get_capacity(self):
        return self.__capacity

    def add_item(self, item):
        if self.__capacity > 0:
            self.items.append(item)
            self.__capacity -= 1
        else:
            return f"not enough room in the inventory"

    def __repr__(self):
        result = f"Items:"
        result += ", ".join(self.items)
        result += f"Capacity left: {self.__capacity}"
        return result


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
