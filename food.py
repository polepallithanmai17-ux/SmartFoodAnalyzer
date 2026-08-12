def get_goal(goal_choice):
    goals = {
        "1": "Muscle Gain",
        "2": "Weight Loss",
        "3": "Weight Maintenance",
        "4": "Healthy Eating"
    }

    return goals.get(goal_choice, "Healthy Eating")


def get_activity(activity_choice):
    activities = {
        "1": "Gym",
        "2": "Light Activity",
        "3": "Mostly Sedentary"
    }

    return activities.get(activity_choice, "Light Activity")


def get_diet(diet_choice):
    diets = {
        "1": "Vegetarian",
        "2": "Non-Vegetarian"
    }

    return diets.get(diet_choice, "Vegetarian")


def calculate_calories(weight, goal, activity):
    # General estimate for this educational project
    calories = weight * 30

    if activity == "Gym":
        calories += 300
    elif activity == "Light Activity":
        calories += 150

    if goal == "Muscle Gain":
        calories += 250
    elif goal == "Weight Loss":
        calories -= 300

    return round(calories)


def calculate_protein(weight, goal):
    if goal == "Muscle Gain":
        return round(weight * 1.6)

    elif goal == "Weight Loss":
        return round(weight * 1.2)

    else:
        return round(weight * 1.0)


def get_food_plan(goal, diet, activity):

    if diet == "Vegetarian":

        breakfast = [
            "Oats with milk",
            "Banana",
            "Peanut butter"
        ]

        lunch = [
            "Rice",
            "Dal",
            "Paneer",
            "Vegetables"
        ]

        snack = [
            "Fruit",
            "Greek yogurt",
            "A handful of nuts"
        ]

        dinner = [
            "Chapati",
            "Dal",
            "Paneer",
            "Vegetables"
        ]

    else:

        breakfast = [
            "Oats with milk",
            "Boiled eggs",
            "Banana"
        ]

        lunch = [
            "Rice",
            "Chicken",
            "Vegetables",
            "Curd"
        ]

        snack = [
            "Fruit",
            "Boiled eggs",
            "A handful of nuts"
        ]

        dinner = [
            "Chapati",
            "Chicken or fish",
            "Vegetables",
            "Curd"
        ]

    # Extra suggestions for gym users
    if activity == "Gym":

        pre_workout = [
            "Banana",
            "Oats",
            "Water"
        ]

        post_workout = [
            "Milk or curd",
            "Fruit",
            "Protein-rich food"
        ]

    else:

        pre_workout = []
        post_workout = []

    return {
        "breakfast": breakfast,
        "lunch": lunch,
        "snack": snack,
        "dinner": dinner,
        "pre_workout": pre_workout,
        "post_workout": post_workout
    }