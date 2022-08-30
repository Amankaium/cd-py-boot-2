from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Product


class TestHomepage(TestCase):
    def test_open_homepage_should_be_success(self): # expected success
        c = Client()
        response = c.get("http://127.0.0.1:8000/")
        assert "Hello world!" in str(response.content)
        assert response.status_code == 200

    def test_post_homepage_should_return_405(self): # expected fail
        c = Client()
        response = c.post("http://127.0.0.1:8000/")
        assert response.status_code == 405, f"{response.status_code} should be 405"


class TestProductCreate(TestCase):
    def test_should_allow_only_post(self):
        c = Client()
        response = c.get("http://127.0.0.1:8000/product/")
        assert response.status_code == 405
        response = c.put("http://127.0.0.1:8000/product/")
        assert response.status_code == 405
        response = c.delete("http://127.0.0.1:8000/product/")
        assert response.status_code == 405
        response = c.patch("http://127.0.0.1:8000/product/")
        assert response.status_code == 405

    def test_should_create_product(self):
        c = Client()
        response = c.post(
            "http://127.0.0.1:8000/product/",
            data={
                "name": "test product 1",
                "price": 1200
            }
        )
        assert response.status_code == 201

    def test_too_long_name_should_fail(self):
        c = Client()
        text = "a" * 300
        response = c.post(
            "http://127.0.0.1:8000/product/",
            data={
                "name": text,
                "price": 1200
            }
        )
        assert response.status_code == 400

        # неверный тип в форме
        # методы
        # нет обязательных полей
        # ненужные поля
        # несколько одинаковых полей

    def test_create_product_with_user(self):
        user = User(
            username="test1",
            email="test1@mail.com",
            password="test1",
        )
        user.save()
        print(f"\n{user}\n")
        p = Product(
            name="яблоко",
            price=100,
            user=user
        )
        p.save()

        assert user.id == p.user.id
        print(f"\nour test done\n")
