import os
from pathlib import Path

project_name = "visa_prediction"
config_dir = "config"

file_list = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    f"{config_dir}/model.yml",
    f"{config_dir}/schema.yml",
    "main.py",
    "README.md",
    ".gitignore",
    "requirements.txt",
    "setup.py",
]

for filepath in file_list:
    filepath = Path(filepath)
    dir_path = filepath.parent
    if not dir_path.exists():
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")
    if not filepath.exists():
        filepath.touch()
        print(f"Created file: {filepath}")
    else:
        print(f"Already exists: {filepath}")
