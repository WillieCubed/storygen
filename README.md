# A Cool AI Project Template

## How to Use

### Overview (Local installation)

Firstly, clone the repository.

- Replace all instances of "ai_project_template" with the name of your project,
all lowercase and with each word separated by underscores.
- Replace all instances of "ai-project-template" with the name of your project,
all lowercase and with each word separated by hyphens.

Now install the dependencies in `requirements.txt`. If using pip (hopefully with
a virtual environment):

```shell
python -m venv ~/environments/<project-name>
source ~/environments/<project-name>/bin/activate
pip install -r requirements.txt
```

### Overview (Docker)

After cloning the repository and customizing it to your needs, you can use it for
development via Docker. This may be very useful 

### Customizing the CLI

The default name of the CLI tool is `aicli`. T

To modify the name of the CLI, change it in `setup.py`

```python
setuptools.setup(
    # ...
    entry_points={
        "console_scripts": [
            "<cli_name_here>=ai_project_template.utils:run_cli",
        ]
    },
    # ...
)
```

### Extras

Replace this README with an actual description of your project.