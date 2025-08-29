def test_add_and_get_answer(client):
    q = client.post("/questions/", json={"text": "Вопрос?"}).json()
    q_id = q["id"]

    response = client.post(f"/questions/{q_id}/answers/", json={"user_id": "user1", "text": "Ответ!"})
    assert response.status_code == 201
    ans = response.json()
    assert ans["text"] == "Ответ!"
    ans_id = ans["id"]

    response = client.get(f"/answers/{ans_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Ответ!"

def test_delete_answer(client):
    q = client.post("/questions/", json={"text": "Удаление ответа"}).json()
    q_id = q["id"]
    ans = client.post(f"/questions/{q_id}/answers/", json={"user_id": "u2", "text": "Ответ"}).json()
    ans_id = ans["id"]

    response = client.delete(f"/answers/{ans_id}")
    assert response.status_code == 204

    response = client.get(f"/answers/{ans_id}")
    assert response.status_code == 404