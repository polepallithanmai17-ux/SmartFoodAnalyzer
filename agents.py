from crewai import Agent, LLM


# Local LLM using Ollama
llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


def create_agents():

    # Agent 1
    profile_agent = Agent(
        role="User Profile Specialist",
        goal="Analyze the user's age, weight, height, activity level, diet, and food goal.",
        backstory=(
            "You are a user profile specialist. "
            "You carefully understand the user's lifestyle, "
            "diet preferences, and food goals."
        ),
        llm=llm,
        verbose=True
    )


    # Agent 2
    nutrition_agent = Agent(
        role="Nutrition Specialist",
        goal="Analyze the user's nutritional needs and provide general calorie and protein guidance.",
        backstory=(
            "You are a nutrition specialist who provides "
            "simple, educational, and balanced nutrition recommendations."
        ),
        llm=llm,
        verbose=True
    )


    # Agent 3
    fitness_agent = Agent(
        role="Fitness Nutrition Specialist",
        goal="Provide food recommendations based on whether the user goes to the gym, has light activity, or is mostly sedentary.",
        backstory=(
            "You are a fitness nutrition specialist. "
            "You understand the relationship between physical activity "
            "and food choices, including pre-workout and post-workout meals."
        ),
        llm=llm,
        verbose=True
    )


    # Agent 4
    food_agent = Agent(
        role="Food Recommendation Specialist",
        goal="Create practical breakfast, lunch, snack, and dinner recommendations based on the user's goal and diet.",
        backstory=(
            "You are a food planning specialist who creates "
            "practical meal recommendations for vegetarian "
            "and non-vegetarian users."
        ),
        llm=llm,
        verbose=True
    )


    # Agent 5
    review_agent = Agent(
        role="Food Plan Review Specialist",
        goal="Review the proposed food plan and check that it matches the user's goal, activity level, and diet preference.",
        backstory=(
            "You are a food plan reviewer. "
            "You check the final plan for consistency, "
            "balance, missing meals, and inappropriate recommendations."
        ),
        llm=llm,
        verbose=True
    )


    return (
        profile_agent,
        nutrition_agent,
        fitness_agent,
        food_agent,
        review_agent
    )