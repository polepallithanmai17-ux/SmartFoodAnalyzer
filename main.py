from crewai import Crew, Process

from agents import create_agents
from tasks import create_tasks


def main():

    print("=" * 60)
    print("        SMART FOOD SUGGESTION SYSTEM")
    print("              5-AGENT AI SYSTEM")
    print("=" * 60)

    print("\nStarting the 5 AI agents...\n")

    # -----------------------------------------
    # CREATE 5 AGENTS
    # -----------------------------------------

    (
        profile_agent,
        nutrition_agent,
        fitness_agent,
        food_agent,
        review_agent
    ) = create_agents()


    # -----------------------------------------
    # CREATE 5 TASKS
    # -----------------------------------------

    (
        profile_task,
        nutrition_task,
        fitness_task,
        food_task,
        review_task
    ) = create_tasks(
        profile_agent,
        nutrition_agent,
        fitness_agent,
        food_agent,
        review_agent
    )


    # -----------------------------------------
    # CREATE CREW
    # -----------------------------------------

    crew = Crew(
        agents=[
            profile_agent,
            nutrition_agent,
            fitness_agent,
            food_agent,
            review_agent
        ],

        tasks=[
            profile_task,
            nutrition_task,
            fitness_task,
            food_task,
            review_task
        ],

        process=Process.sequential,

        verbose=True
    )


    # -----------------------------------------
    # USER INPUT
    # -----------------------------------------

    print("\n" + "=" * 60)
    print("             USER INFORMATION")
    print("=" * 60)

    name = input("\nEnter your name: ")

    age = input("Enter your age: ")

    weight = input("Enter your weight in kg: ")

    height = input("Enter your height in cm: ")


    print("\nSelect your goal:")

    print("1. Muscle Gain")
    print("2. Weight Loss")
    print("3. Weight Maintenance")
    print("4. Healthy Eating")

    goal_choice = input("Enter your choice (1-4): ")


    goals = {
        "1": "Muscle Gain",
        "2": "Weight Loss",
        "3": "Weight Maintenance",
        "4": "Healthy Eating"
    }

    goal = goals.get(
        goal_choice,
        "Healthy Eating"
    )


    print("\nSelect your activity:")

    print("1. Gym")
    print("2. Light Activity")
    print("3. Mostly Sedentary")

    activity_choice = input(
        "Enter your choice (1-3): "
    )


    activities = {
        "1": "Gym",
        "2": "Light Activity",
        "3": "Mostly Sedentary"
    }

    activity = activities.get(
        activity_choice,
        "Light Activity"
    )


    print("\nSelect your diet:")

    print("1. Vegetarian")
    print("2. Non-Vegetarian")

    diet_choice = input(
        "Enter your choice (1-2): "
    )


    diets = {
        "1": "Vegetarian",
        "2": "Non-Vegetarian"
    }

    diet = diets.get(
        diet_choice,
        "Vegetarian"
    )


    # -----------------------------------------
    # CREATE USER INPUT FOR CREW
    # -----------------------------------------

    user_information = f"""
    User Information:

    Name: {name}
    Age: {age}
    Weight: {weight} kg
    Height: {height} cm

    Goal: {goal}
    Activity Level: {activity}
    Diet: {diet}

    Create a personalized food recommendation
    based on this information.
    """


    # -----------------------------------------
    # RUN THE 5 AGENTS
    # -----------------------------------------

    print("\n" + "=" * 60)
    print("          RUNNING 5 AI AGENTS")
    print("=" * 60)

    result = crew.kickoff(
        inputs={
            "user_information": user_information
        }
    )


    # -----------------------------------------
    # DISPLAY FINAL RESULT
    # -----------------------------------------

    print("\n" + "=" * 60)
    print("          FINAL SMART FOOD PLAN")
    print("=" * 60)

    print(result)

    print("\n" + "=" * 60)
    print("              PROCESS COMPLETE")
    print("=" * 60)

    print("\nPowered by:")
    print("CrewAI + Ollama + Llama 3.2")

    print(
        "\nNote: This is an educational food "
        "recommendation system and not medical advice."
    )


if __name__ == "__main__":
    main()