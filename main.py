class TreeStore:
    def __init__(self, items):
        self.items = items

    def __repr__(self):
        return str(self.items)

    def getAll(self):
        return self.items

    def getItem(self, id):
        item = list(filter(lambda item: item['id'] == id, self.items))
        if item:
            return item[0]
        else:
            return f'Объекта с id {id} не существует'

    def getChildren(self, id):
        items = list(filter(lambda item: item['parent'] == id, self.items))

        return items

    def getParents(self, id):
        tree = []
        current_item = ts.getItem(id)
        if current_item != f'Объекта с id {id} не существует':
            while current_item['parent'] != 'root':
                next_item = ts.getItem(current_item['parent'])
                tree.append(next_item)
                current_item = next_item

            return tree
        else:
            return current_item


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)
print(ts.getAll())
print(ts.getItem(3))
print(ts.getItem(18))
print(ts.getChildren(4))
print(ts.getChildren(5))
print(ts.getParents(7))
print(ts.getParents(18))
