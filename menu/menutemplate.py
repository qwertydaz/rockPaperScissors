class MenuTemplate:
    def __init__(self, title, divider, options, exit_option):
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not isinstance(divider, str):
            raise TypeError("divider must be a string")
        if not all(isinstance(option, str) for option in options):
            raise TypeError("options must be a list of strings")
        if not isinstance(exit_option, str):
            raise TypeError("exit_option must be a string")

        self.title = title
        self.divider = divider
        self.options = options
        self.exit_option = exit_option

    def show(self):
        print(self.title)

        index = 1
        for option in self.options:
            print("(" + str(index) + ") " + option)
            index += 1

        print("(0) " + self.exit_option)
        print(self.divider)

    def get_choice(self):
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice")
            return self.get_choice()

        if choice < 0 or choice > len(self.options):
            print("Invalid choice")
            return self.get_choice()

        return choice

    def num_of_options(self):
        return len(self.options)
