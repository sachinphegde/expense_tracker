import json
# from config import BUDGET_FILE_PATH

def load_budget(file_path="budget.json"):
    """Load budget data from a JSON file."""
    with open(file_path, "r") as file:
        budget = json.load(file)

    categories = budget["categories"].keys()
    for category in categories:
        cat_sum = sum(budget["categories"][category].values())
        print(f"{category}: {cat_sum}")


def main():
    load_budget()


if __name__ == "__main__":
    main()
