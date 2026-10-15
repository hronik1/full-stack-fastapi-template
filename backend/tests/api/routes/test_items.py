import uuid

from fastapi.testclient import TestClient

from app.core.config import settings

ITEMS_URL = f"{settings.API_V1_STR}/items/"


def create_item(client: TestClient, title: str = "Foo") -> dict:
    response = client.post(ITEMS_URL, json={"title": title, "description": "Fighters"})
    assert response.status_code == 200
    return response.json()


def test_create_item(client: TestClient) -> None:
    content = create_item(client)
    assert content["title"] == "Foo"
    assert content["description"] == "Fighters"
    assert "id" in content


def test_read_item(client: TestClient) -> None:
    item = create_item(client)
    response = client.get(f"{ITEMS_URL}{item['id']}")
    assert response.status_code == 200
    assert response.json() == item


def test_read_item_not_found(client: TestClient) -> None:
    response = client.get(f"{ITEMS_URL}{uuid.uuid4()}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_read_items(client: TestClient) -> None:
    create_item(client, "A")
    create_item(client, "B")
    content = client.get(ITEMS_URL).json()
    assert content["count"] == 2
    assert {i["title"] for i in content["data"]} == {"A", "B"}


def test_update_item(client: TestClient) -> None:
    item = create_item(client)
    response = client.put(f"{ITEMS_URL}{item['id']}", json={"title": "Updated"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated"
    assert response.json()["description"] == "Fighters"


def test_update_item_not_found(client: TestClient) -> None:
    response = client.put(f"{ITEMS_URL}{uuid.uuid4()}", json={"title": "x"})
    assert response.status_code == 404


def test_delete_item(client: TestClient) -> None:
    item = create_item(client)
    response = client.delete(f"{ITEMS_URL}{item['id']}")
    assert response.status_code == 200
    assert client.get(f"{ITEMS_URL}{item['id']}").status_code == 404


def test_create_item_requires_title(client: TestClient) -> None:
    assert client.post(ITEMS_URL, json={"title": ""}).status_code == 422
