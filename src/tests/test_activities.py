def test_root_redirects_to_static_index(client):
    # Arrange
    # (no setup needed)

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_name = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    body = response.json()
    assert expected_name in body
    activity = body[expected_name]
    assert set(activity.keys()) == {"description", "schedule", "max_participants", "participants"}
    assert isinstance(activity["participants"], list)
