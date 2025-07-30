class User:


    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear


    def get_name(self):
        name = self.name.upper()
        return name


    def age(self, current_year):
        user_age = int(current_year) - int(self.birthyear)
        return user_age


if __name__ == "__main__":
    user_name = "John"
    user_birthyear = 1999
    user = User(name=user_name, birthyear=user_birthyear)
    current_year = 2023
    print(user.get_name())
    print(user.age(current_year))
