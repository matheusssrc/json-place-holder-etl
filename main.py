import subprocess
from os import makedirs

import papermill as pm

if __name__ == "__main__":

    makedirs("notebook_outputs", exist_ok=True)

    subprocess.run(["python", "ingestion.py"], check=True)

    pm.execute_notebook(
        "bronze.ipynb", 
        "notebook_outputs/bronze_output.ipynb",
    )

    pm.execute_notebook(
        "silver.ipynb", 
        "notebook_outputs/silver_output.ipynb",
    )

    print("Pipeline Execution Completed!")