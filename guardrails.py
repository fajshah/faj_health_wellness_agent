def validate_goal_input(text: str) -> bool:
    return any(metric in text.lower() for metric in ["kg", "pounds", "weeks", "months"])