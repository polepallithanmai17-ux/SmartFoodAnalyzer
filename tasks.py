from crewai import Task


def create_tasks(
    profile_agent,
    nutrition_agent,
    fitness_agent,
    food_agent,
    review_agent
):

    # -------------------------------------------------
    # TASK 1 - USER PROFILE
    # -------------------------------------------------

    profile_task = Task(
        description="""
        Analyze the user's information.

        Identify:
        - Age
        - Weight
        - Height
        - Goal
        - Activity level
        - Diet preference

        Create a clear summary of the user's profile
        that can be used by the other agents.
        """,

        expected_output="""
        A clear user profile containing:
        age, weight, height, goal, activity level,
        and diet preference.
        """,

        agent=profile_agent
    )


    # -------------------------------------------------
    # TASK 2 - NUTRITION
    # -------------------------------------------------

    nutrition_task = Task(
        description="""
        Using the user's profile, provide general
        nutritional guidance.

        Estimate:
        - Daily calorie requirement
        - Daily protein target

        Consider the user's:
        - Weight
        - Goal
        - Activity level

        Explain that the values are general estimates
        for an educational food suggestion system.
        """,

        expected_output="""
        A nutrition summary containing an estimated
        daily calorie target and protein target,
        with a short explanation.
        """,

        agent=nutrition_agent,
        context=[profile_task]
    )


    # -------------------------------------------------
    # TASK 3 - FITNESS
    # -------------------------------------------------

    fitness_task = Task(
        description="""
        Analyze the user's activity level and goal.

        Provide food-related fitness recommendations.

        If the user goes to the gym, include:
        - Pre-workout food suggestions
        - Post-workout food suggestions
        - Hydration suggestions

        If the user does not go to the gym,
        provide suitable general activity-related
        food recommendations.
        """,

        expected_output="""
        Fitness-related food recommendations
        appropriate for the user's activity level
        and goal.
        """,

        agent=fitness_agent,
        context=[profile_task, nutrition_task]
    )


    # -------------------------------------------------
    # TASK 4 - FOOD PLAN
    # -------------------------------------------------

    food_task = Task(
        description="""
        Create a practical one-day food plan based
        on the user's profile, nutrition information,
        and fitness recommendations.

        Include:

        - Breakfast
        - Lunch
        - Snack
        - Dinner

        If the user is a gym-going person, also include:

        - Pre-workout meal
        - Post-workout meal

        Respect the user's diet preference:

        Vegetarian:
        Do not recommend meat, chicken, fish, or eggs.

        Non-Vegetarian:
        Meat, chicken, fish, and eggs may be included.

        Make the suggestions practical and easy to understand.
        """,

        expected_output="""
        A complete one-day personalized food plan
        containing breakfast, lunch, snack, dinner,
        and gym-related meals when appropriate.
        """,

        agent=food_agent,
        context=[
            profile_task,
            nutrition_task,
            fitness_task
        ]
    )


    # -------------------------------------------------
    # TASK 5 - REVIEW
    # -------------------------------------------------

    review_task = Task(
        description="""
        Review the complete food plan.

        Check whether:

        1. The food plan matches the user's goal.
        2. The food plan matches the user's diet preference.
        3. The food plan matches the activity level.
        4. Breakfast, lunch, snack, and dinner are present.
        5. Gym users have suitable pre-workout and
           post-workout suggestions.
        6. The recommendations are generally balanced.
        7. There are no obvious contradictions.

        If something needs improvement, suggest a correction.

        Do not provide medical diagnosis or treatment.
        """,

        expected_output="""
        A final reviewed food plan with:
        - Review status
        - Problems found, if any
        - Recommended corrections
        - Final recommendations
        """,

        agent=review_agent,
        context=[
            profile_task,
            nutrition_task,
            fitness_task,
            food_task
        ]
    )


    return (
        profile_task,
        nutrition_task,
        fitness_task,
        food_task,
        review_task
    )