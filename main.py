from planner_agent import generate_health_plan

def main():
    print("🧘‍♀️ Welcome to your faj AI Health & Wellness Planner!")
    user_goal = input("💬 Enter your health goal (e.g., 'I want to lose 5kg in 2 months'): ")

    plan = generate_health_plan(user_goal)

    print("\n📋 Your Personalized Health Plan:\n")
    print(plan)

if __name__ == "__main__":
    main()
