"""Reproducible property testing across Python versions and CI hosts."""

from hypothesis import settings

settings.register_profile("atlas", max_examples=150, deadline=None, derandomize=True)
settings.load_profile("atlas")
