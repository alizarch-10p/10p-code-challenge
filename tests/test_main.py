import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_create_document():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/documents/", json={"content": "Example document content"})
    assert response.status_code == 200
    assert "document_id" in response.json()


@pytest.mark.asyncio
async def test_get_document():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        post_response = await ac.post("/documents/", json={"content": "Example document content"})
        document_id = post_response.json()['document_id']

        get_response = await ac.get(f"/documents/{document_id}")
    assert get_response.status_code == 200
    assert "content" in get_response.json()


@pytest.mark.asyncio
async def test_search_documents():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/search/?query=Example")
    assert response.status_code == 200
    assert isinstance(response.json()['results'], list)


@pytest.mark.asyncio
async def test_get_answer():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/answer/?query=Example")
    assert response.status_code == 200
    assert "answer" in response.json()
