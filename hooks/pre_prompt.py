import json
import os
import uuid
import subprocess
from pathlib import Path


PRIVATE_TEMPLATE_ACCESS = os.getenv("PRIVATE_TEMPLATE_ACCESS")
PRIVATE_TEMPLATE_REPOSITORY = os.getenv("PRIVATE_TEMPLATE_REPOSITORY")


def clone_private_cookiecutter_templates():
    # Check for env var settings access
    if not PRIVATE_TEMPLATE_ACCESS:
        return
    
    # Check for env var settings repo
    if not PRIVATE_TEMPLATE_REPOSITORY:
        raise Exception("PRIVATE_TEMPLATE_REPOSITORY environ variable not set.")

    # Clone and copy bs templates into directory
    dir_name = f"/tmp/templates-{uuid.uuid4()}"
    cloning_process = subprocess.run(["git", "clone", "--depth", "1", PRIVATE_TEMPLATE_REPOSITORY, dir_name])
    if cloning_process.returncode != 0:
        raise Exception("You are not allowed to access to BS repository.")

    subprocess.run(["cp", "-r", f"{dir_name}/templates/", "templates/"])

    # Rewrite cookiecutter file merging cookiecutter config file from private template with the public one
    with open(f"{dir_name}/cookiecutter.json", "r") as f:
        bs_config = json.load(f)

    cookiecutter_file = Path("cookiecutter.json")
    config = json.loads(cookiecutter_file.read_text())
    config["template"] = config["template"] + bs_config["template"]
    cookiecutter_file.write_text(json.dumps(config, indent=4))


if __name__ == "__main__":
   clone_private_cookiecutter_templates()
    
