import sender_stand_request
import data


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


# 1. Тест. Допустимое количество символов в поле name (1)
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("А")
    kit_response = sender_stand_request.post_new_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]


# 2. Тест. Допустимое количество символов в поле name (511)
def test_create_kit_511_letter_in_name_get_success_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    kit_response = sender_stand_request.post_new_kit(kit_body)
    assert kit_response.status_code == 201


# 3. Тест. Недопустимое количество символов в поле name (0)
def test_create_kit_empty_name_get_error_response():
    kit_body = get_kit_body("")
    response = sender_stand_request.post_new_kit(kit_body)
    assert response.status_code == 400


# 4. Тест. Недопустимое количество символов в поле name (512)
def test_negative_assert_512_letter_in_name():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    response = sender_stand_request.post_new_kit(kit_body)
    assert response.status_code == 400


# 5. Тест. Разрешены английские буквы в поле name
def test_create_kit_english_letter_in_name_get_success_response():
    kit_body = get_kit_body("QWErty")
    kit_response = sender_stand_request.post_new_kit(kit_body)
    assert kit_response.status_code == 201


# 6. Тест. Разрешены русские буквы в поле name
def test_create_kit_russian_letter_in_name_get_success_response():
    kit_body = get_kit_body("Мария")
    kit_response = sender_stand_request.post_new_kit(kit_body)
    assert kit_response.status_code == 201


# 7. Тест. Разрешены спецсимволы в поле name
def test_create_kit_has_special_symbol_letter_in_name_get_success_reponse():
    kit_body = get_kit_body("\"№%@\",")
    kit_response = sender_stand_request.post_new_kit(kit_body)
    assert kit_response.status_code == 201


# 8. Тест. Разрешены пробелы в поле name
def test_create_kit_has_space_in_name():
    kit_body = get_kit_body("Человек И КО")
    kit_response = sender_stand_request.post_new_kit(kit_body)
    assert kit_response.status_code == 201


# 9. Тест. Разрешены цифры в поле name
def test_create_kit_has_numder_in_name():
    kit_body = get_kit_body("123")
    kit_response = sender_stand_request.post_new_kit(kit_body)
    assert kit_response.status_code == 201


def negative_assert_no_name(kit_body):
    response = sender_stand_request.post_new_kit(kit_body)  # сохранен результат вызова функции
    assert response.status_code == 400
    assert response.json()["code"] == 400  # проверяем, что код ответа - 400


# 10. Тест. Параметр name не передан
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    response = sender_stand_request.post_new_kit(kit_body)
    assert response.status_code == 400


# 11. Тест. Передан другой тип параметра
def test_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(1234)
    response = sender_stand_request.post_new_kit(kit_body)
    assert response.status_code == 400

def test_integer_division():
    a = 5//2
    a == 2

test_integer_division();