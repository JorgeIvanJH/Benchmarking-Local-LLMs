import os
import dotenv
from inspect_ai import eval
from inspect_evals.medqa import medqa
from inspect_evals.pubmedqa import pubmedqa
from inspect_evals.healthbench  import healthbench

dotenv.load_dotenv()

modelname = "medgemma-4b-it" # CHANGE THIS TO YOUR MODEL NAME

results = eval(
    tasks=[
        medqa(),
        pubmedqa(),
        healthbench()
        ],
    model=f"openai/{modelname}",
    model_base_url="http://localhost:1234/v1",
)
