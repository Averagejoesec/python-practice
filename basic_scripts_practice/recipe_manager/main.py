
# Uses a Python class to represent a recipe
class Recipe:
    # Stores recipe name, ingredients list, and cooking time as attributes
    def __init__ (self, name, ingredients, cookingTime):
        self.name = name
        self.ingredients = ingredients
        self.cookingTime = cookingTime
    # Includes a method to display the full recipe details
    def displayRecipe(self):
        print(f"Recipe: {self.name}")
        print(f"Ingredients: {', '.join(self.ingredients)}")
        print(f"Cooking Time: {self.cookingTime} minutes")
    # Includes a method to add new ingredients to the recipe
    def addIngredient(self, ingredient):
        self.ingredients.append(ingredient)
        print(f"Added {ingredient} to {self.name}\n")
    # Creates multiple recipe instances to build a cookbook

if __name__ == "__main__":
    recipe1 = Recipe("Pasta", ["Noodles", "Tomato Sauce", "Cheese"], 20)
    recipe2 = Recipe("Salad", ["Lettuce", "Tomatoes", "Cucumbers", "Dressing"], 10)
    recipe3 = Recipe("Omelette", ["Eggs", "Salt", "Pepper", "Cheese"], 15)

    print("Recipe Manager")
    print("===============\n")
    print("Creating Recipes...\n")

    Recipe.displayRecipe(recipe1)
    Recipe.displayRecipe(recipe2)
    Recipe.displayRecipe(recipe3)

    print("\nAdding extra ingredients...\n")

    Recipe.addIngredient(recipe1, "Basil")
    Recipe.displayRecipe(recipe1)

    print("\nCookbook Complete!")

# Adding a new ingredient to the pasta recipe
# Demonstrates how lists can be stored as class attributes

# Shows how methods can modify object data dynamically