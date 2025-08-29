def test_create_question(client):
    response = client.post("/questions/", json={"text": "Что такое FastAPI?"})
    assert response.status_code == 201
    data = response.json()
    assert data["text"] == "Что такое FastAPI?"
    assert "id" in data

def test_get_questions_list(client):
    client.post("/questions/", json={"text": "Первый вопрос"})
    response = client.get("/questions/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["text"] == "Первый вопрос"

def test_delete_question_cascade(client):
    q = client.post("/questions/", json={"text": "Вопрос с ответами"}).json()
    q_id = q["id"]
    client.post(f"/questions/{q_id}/answers/", json={"user_id": "u1", "text": "Ответ"})
    response = client.delete(f"/questions/{q_id}")
    assert response.status_code == 204
    response = client.get(f"/questions/{q_id}")
    assert response.status_code == 404
