AI Recipe Generator Jupyter to test -> Python -> Streamlit

AI-powered recipe generator i used to introduce myself to:
- Prompting + structured outputs (recipe, instructions)
- Modern LangChain updates (post-LLMChain changes)
- secret handling with `.env`
- Prototyping in Jupyter, before deploying on Streamlit

For now:
- Generate a recipe from a list of ingredients
- Prompt templating for consistent formatting
- Runs in a Jupyter Notebook for rapid iteration

Tech Stack
- Python
- Jupyter Notebook (`.ipynb`)
- LangChain (newer LCEL style)
- OpenAI API (via `OPENAI_API_KEY`)

Foklder
├── ai_recipe_app.ipynb
├── .gitignore
└── (optional later) app.py # Streamlit version

1) LangChain has breaking changes in newer versions
Older tutorials used patterns like:
from langchain.llms import OpenAI
LLMChain(...).run(...)
In newer LangChain, many integrations moved into separate packages and the recommended approach is:
install langchain-community and langchain-openai
replace LLMChain with LCEL pipelines (e.g., prompt | llm | parser)
use .invoke({...}) instead of .run(...)

2) .env loading depends on the working directory / environment
Even with python-dotenv installed, .env won’t load if:
the notebook/kernel is using a different interpreter than the terminal
the .env is not in the current working directory
Debugging steps that helped:
printing os.getcwd() to confirm the working directory
verifying .env exists with os.listdir()
using dotenv_values(".env") to confirm it is parsed correctly

Fixed missing module errors caused by LangChain splitting packages:
ModuleNotFoundError: langchain_community
Updated outdated imports to current packages (langchain_openai, langchain_core)
Updated chain execution from .run() to .invoke()
Resolved .env not loading by validating path + file parsing

```bash
git clone https://github.com/SV-Cookie/Recipe_Generator_OpenAI.git
cd  Recipe_Generator_OpenAI

