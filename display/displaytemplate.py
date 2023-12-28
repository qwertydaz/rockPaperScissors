class DisplayTemplate:
    def __init__(self, title, divider, items):
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not isinstance(divider, str):
            raise TypeError("divider must be a string")
        if not all(isinstance(item, str) for item in items):
            raise TypeError("items must be a list of strings")

        self.title = title
        self.divider = divider
        self.items = items

    def show(self):
        print(self.title)
        print(self.divider)

        for item in self.items:
            print(item)
