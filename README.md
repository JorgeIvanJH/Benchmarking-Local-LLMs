Requirements:
    LM Studio (app downloaded)
    python 3.12 (manually install requirements.txt)
    VSCode extension: Inspect AI 

In LM Studio enable developer mode
In LM Studio find and download models
In LM Studio go to Developer > Run local server and the downloaded models

in test.py specify the name of the model to test and then hit

    python test.py

In root of this repo execute the following to see logs in a UI on http://localhost:7575/

    inspect view

go to http://localhost:7575/ and see results

Note: in LM Studio you might want to set the context length to be the max allowed per model, otherwise benchmarks that involve open questions will fail to be answered (HealthBench)