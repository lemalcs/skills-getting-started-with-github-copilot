import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities

# Snapshot of the original in-memory data, restored after every test
_original_activities = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    yield
    # Mutate in place: other modules hold a reference to this same dict object
    activities.clear()
    activities.update(copy.deepcopy(_original_activities))


@pytest.fixture
def client():
    return TestClient(app)
