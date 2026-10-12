from collections import defaultdict, deque


class Solution:
    def findAllRecipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        waiting = defaultdict(list)
        needed = [len(items) for items in ingredients]
        for recipe, items in enumerate(ingredients):
            for ingredient in items:
                waiting[ingredient].append(recipe)
        pending = deque(supplies)
        answers = []
        while pending:
            item = pending.popleft()
            for recipe in waiting[item]:
                needed[recipe] -= 1
                if needed[recipe] == 0:
                    answers.append(recipes[recipe])
                    pending.append(recipes[recipe])
        return answers
