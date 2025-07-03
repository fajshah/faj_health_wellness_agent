# faj_health_wellness_agent# 🧘‍♀️ Health & Wellness Planner Agent

A fully functional AI-powered Health & Wellness Planner built using the OpenAI Agents SDK and Google Gemini API.
This agent can analyze user health goals, generate structured plans, and guide users through a personalized fitness and nutrition journey.

---

## ✅ SDK Features Overview

| Feature                    | Status | Description |
|---------------------------|--------|-------------|
| Agent + Tool Creation     | ✅ Yes | Created a main agent using Assistant(...) and integrated 5 domain-specific tools. |
| State Management          | ✅ Yes | Implemented UserSessionContext to maintain per-user state across conversations. |
| Guardrails (Input/Output) | ✅ Yes | Applied via custom run_hooks using MyRunHooks, allowing validation and sanitization. |
| Real-Time Streaming       | ✅ Yes | Implemented via utils/streaming.py for live user feedback during longer responses. |
| Handoff to Another Agent  | ✅ Yes | Delegates tasks to nutrition_expert_agent, injury_support_agent, and escalation_agent. |
| Lifecycle Hooks           | ✅ Yes | Fully implemented using hooks/MyRunHooks.py for pre/post-processing and context adaptation. |

---

## 🧩 Modular Architecture

```
health_wellness_agent/
├── main.py                          # Entry point
├── context/
│   └── UserSessionContext.py        # Session-specific state management
├── tools/                           # Planner tools
│   ├── goal_analyzer.py             # Analyzes user goals
│   ├── meal_planner.py              # Personalized diet planning
│   ├── workout_recommender.py       # Suggests suitable workouts
│   ├── scheduler.py                 # Weekly check-in planner
│   └── tracker.py                   # Progress tracker tool
├── agents/                          # Specialized agents for handoff
│   ├── nutrition_expert_agent.py
│   ├── injury_support_agent.py
│   └── escalation_agent.py
├── hooks/
│   └── MyRunHooks.py                # Custom lifecycle logic
├── utils/
│   └── streaming.py                 # Real-time streaming for responses
├── planner_agent.py                 # The main `Assistant` agent config
├── .env                             # API key securely loaded here
```

---

## 🔧 Tools Overview

| Tool Name              | Purpose                                                                 |
|------------------------|-------------------------------------------------------------------------|
| `GoalAnalyzerTool`     | Converts user goals into structured format using input/output guardrails |
| `MealPlannerTool`      | Async tool to suggest 7-day meal plan honoring dietary preferences       |
| `WorkoutRecommenderTool` | Suggests workout plan based on parsed goals and experience              |
| `CheckinSchedulerTool` | Schedules recurring weekly progress checks                               |
| `ProgressTrackerTool`  | Accepts updates, tracks user progress, modifies session context          |

---

## 🤝 Handoffs (Specialized Agents)

Specialized agents receive control through `handoff()` based on user input.

| Agent Name            | Trigger Condition                                        |
|----------------------|-----------------------------------------------------------|
| `EscalationAgent`     | User wants to speak to a human coach                      |
| `NutritionExpertAgent`| Complex dietary needs like diabetes or allergies          |
| `InjurySupportAgent`  | Physical limitations or injury-specific workouts          |

Each agent should:
- Be declared and passed in the `handoffs` parameter of the main agent
- Optionally implement `on_handoff()` for logging or initialization

---

## 📦 Context Management

A shared context class is used across all tools and agents to persist user-specific state.

```python
class UserSessionContext(BaseModel):
    name: str
    uid: int
    goal: Optional[dict] = None
    diet_preferences: Optional[str] = None
    workout_plan: Optional[dict] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: List[str] = []
    progress_logs: List[Dict[str, str]] = []
```

Used by all tools, hooks, and agents as `RunContextWrapper[UserSessionContext]`.

---

## 🔒 Guardrails

### ✅ Input Guardrails:
- Validate goal input format: quantity, metric, duration (e.g. "lose 5kg in 2 months")
- Ensure valid dietary or injury-related inputs
- Block unsupported or incomplete entries

### ✅ Output Guardrails:
- Ensure tools return structured JSON or Pydantic models
- Useful for validating and parsing agent responses

---

## 🔄 Streaming

Real-time responses are streamed using the `Runner.stream(...)` method:

```python
async for step in Runner.stream(starting_agent=agent, input="Help me lose weight", context=user_context):
    print(step.pretty_output)
```

---

## 💡 Bonus Ideas

To further enhance your Health & Wellness Planner Agent:

- 📊 **Streamlit Dashboard**  
  Build a clean and interactive UI using Streamlit to allow users to set goals, track progress, and visualize plans.

- 📝 **User Progress PDF Report**  
  Generate downloadable PDF reports of weekly or monthly user progress using libraries like `reportlab` or `fpdf`.

- 🗃️ **Integration with a Database or File Storage**  
  Store user sessions, plans, and progress history in a database like SQLite, PostgreSQL, or even JSON/CSV files for persistent tracking and analytics.

---

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/health-wellness-agent.git
cd health-wellness-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your `.env` file:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

4. Run the planner agent:
```bash
python main.py
```

5. (Optional) Run Streamlit dashboard:
```bash
streamlit run streamlit_dashboard.py
```

---

## 📄 License
This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

---

## ✨ Credits
Built with ❤️ by Faj
