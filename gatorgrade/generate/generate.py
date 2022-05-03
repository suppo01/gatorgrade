"""Generate a GatorGrade configuration file.

Gatorgrade file will include paths to whitelisted files
and default GatorGrader checks.
"""

# Import the necessary libraries


def create_targeted_paths_list():
    """Generate a list of targeted paths by walking the paths."""
    # Go through the root repo, the sub dictionaries and files.
    # Select only files in the dictionaries with specific names.
    # Add those targeted file paths into a list and returns it.


def write_yaml_of_paths_list(path_names):  # expected input: A path list
    """Write YAML file to create gatorgrade file and set default messages."""
    files_list = [
        {
            "path/to": [
                {
                    "file.py": [
                        {
                            "description": "Complete all TODOs",
                            "check": "MatchFileFragment",
                            "options": {"fragment": "TODO", "count": 0, "exact": True},
                        }
                    ]
                },
                {
                    "file2.py": [
                        {
                            "description": "Complete all TODOs",
                            "check": "MatchFileFragment",
                            "options": {"fragment": "TODO", "count": 0, "exact": True},
                        }
                    ]
                },
            ]
        }
    ]
    # Write the default set up messages in YAML file.

    with open('gatorgrade.yml', 'w') as file:
        # Open the YAML file gatorgrade 
        data = yaml.dump(files_list, file)
        # Yaml dump accepts a python object and produces a YAML document.
