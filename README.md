# 🥗 Smart Food Suggestion System

An AI-powered **Smart Food Suggestion System** that generates personalized food recommendations based on a user's personal information, fitness goals, activity level, and dietary preferences.

The project uses a **5-agent multi-agent architecture** with **CrewAI**, powered by **Llama 3.2 through Ollama** for local AI inference.

---

## 📌 Project Overview

People have different nutritional requirements depending on their age, body measurements, fitness goals, activity levels, and dietary preferences.

The **Smart Food Suggestion System** addresses this problem by analyzing user information and generating a personalized daily food plan.

The system is designed for both:

- 🏋️ Gym-going users
- 🚶 Lightly active users
- 🪑 Mostly sedentary users
- 🥗 Vegetarian users
- 🍗 Non-vegetarian users

It supports multiple goals such as:

- Muscle Gain
- Weight Loss
- Weight Maintenance
- Healthy Eating

> **Note:** The recommendations are intended for educational purposes and should not be considered medical or professional dietary advice.

---

## 🎯 Objectives

The main objectives of this project are to:

- Collect and analyze user information.
- Identify the user's fitness and dietary goals.
- Provide general calorie and protein guidance.
- Generate personalized meal recommendations.
- Provide pre-workout and post-workout suggestions for gym users.
- Support vegetarian and non-vegetarian diets.
- Use multiple specialized AI agents for different responsibilities.
- Review the generated food plan before presenting it to the user.
- Run the LLM locally using Ollama.

---

## 🤖 Multi-Agent Architecture

The system uses **5 specialized AI agents**, with each agent performing a specific task.

### 1. 👤 Profile Agent

Analyzes the user's:

- Age
- Weight
- Height
- Goal
- Activity level
- Diet preference

### 2. 🥦 Nutrition Agent

Provides general nutritional guidance based on:

- Body weight
- Fitness goal
- Activity level

It provides estimated calorie and protein requirements.

### 3. 🏋️ Fitness Agent

Analyzes the user's activity level and fitness requirements.

For gym users, it provides:

- Pre-workout suggestions
- Post-workout suggestions
- Hydration guidance

### 4. 🍽️ Food Recommendation Agent

Creates a personalized daily food plan including:

- Breakfast
- Lunch
- Snacks
- Dinner
- Pre-workout meal
- Post-workout meal

where applicable.

### 5. ✅ Review Agent

Reviews the generated food plan and checks whether it:

- Matches the user's goal
- Matches the selected diet
- Matches the activity level
- Contains appropriate meals
- Provides suitable gym-related recommendations

---

## 🔄 System Workflow

```text
                    USER
                     │
                     ▼
              User Information
                     │
                     ▼
            ┌─────────────────┐
            │  Profile Agent  │
            └────────┬────────┘
                     │
                     ▼
           ┌──────────────────┐
           │ Nutrition Agent  │
           └────────┬─────────┘
                    │
                    ▼
           ┌──────────────────┐
           │  Fitness Agent   │
           └────────┬─────────┘
                    │
                    ▼
           ┌──────────────────┐
           │   Food Agent     │
           └────────┬─────────┘
                    │
                    ▼
           ┌──────────────────┐
           │   Review Agent   │
           └────────┬─────────┘
                    │
                    ▼
          Personalized Food Plan
