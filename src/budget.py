import json
from github import download_from_github
from config import BUDGET_LOCAL_PATH


def load_budget():
    """Load budget data from a JSON file."""
    download_from_github("json")
    with open(BUDGET_LOCAL_PATH, "r") as file:
        budget = json.load(file)

    cat_budget = {}
    categories = budget["categories"].keys()
    for category in categories:
        cat_sum = sum(budget["categories"][category].values())
        cat_budget[category] = cat_sum
        print(f"{category}: {cat_sum}")
    return cat_budget