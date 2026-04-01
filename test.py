import os
import dotenv
from inspect_ai import eval
from inspect_evals.medqa import medqa
from inspect_evals.pubmedqa import pubmedqa
from inspect_evals.healthbench  import healthbench

dotenv.load_dotenv()

modelname = "jsl-medllama-3-8b-v2.0"

results = eval(
    tasks=healthbench(),
    model=f"openai/{modelname}",
    model_base_url="http://localhost:1234/v1",
)
