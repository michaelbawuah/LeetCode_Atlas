class Solution:
    def simplifyPath(self, path: str) -> str:
        components = []
        for part in path.split("/"):
            if not part or part == ".":
                continue
            if part == "..":
                if components:
                    components.pop()
            else:
                components.append(part)
        return "/" + "/".join(components)
