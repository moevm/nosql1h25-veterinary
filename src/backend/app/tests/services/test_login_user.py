import unittest
from unittest.mock import patch, MagicMock
from werkzeug.security import generate_password_hash
from app.services.auth_service import login_user


class TestLoginUser(unittest.TestCase):

    @patch('app.services.auth_service.check_password_hash')
    @patch('app.services.auth_service.get_user_by_login')
    def test_login_user_success(self, mock_get_user_by_login, mock_check_password):
        """Тестируем корректную авторизацию"""
        test_login = "testuser"
        test_password = "secretpassword"
        hashed_password = generate_password_hash(test_password)

        mock_user = MagicMock()
        mock_user.password_hash = hashed_password
        mock_get_user_by_login.return_value = mock_user

        mock_check_password.return_value = True

        data = {"login": test_login, "password": test_password}
        print("Mocked user:", mock_get_user_by_login.return_value)
        print("Password hash:", hashed_password)
        print("check_password_hash called:", mock_check_password.call_count)

        user = login_user(data)

        self.assertEqual(user, mock_user)
        mock_get_user_by_login.assert_called_once_with(test_login)
        mock_check_password.assert_called_once_with(hashed_password, test_password)

    @patch('app.services.auth_service.get_user_by_login')
    @patch('werkzeug.security.check_password_hash')
    def test_login_user_invalid_login(self, mock_check_password, mock_get_user_by_login):
        """Тестируем авторизацию с неверным логином"""
        test_login = "wronguser"
        test_password = "wrongpassword"

        mock_get_user_by_login.return_value = None

        data = {"login": test_login, "password": test_password}
        with self.assertRaises(ValueError) as context:
            login_user(data)

        self.assertEqual(str(context.exception), "Invalid login or password")
        mock_get_user_by_login.assert_called_once_with(test_login)
        mock_check_password.assert_not_called()

    @patch('app.services.auth_service.check_password_hash')
    @patch('app.services.auth_service.get_user_by_login')
    def test_login_user_invalid_password(self, mock_get_user_by_login, mock_check_password):
        """Тестируем авторизацию с неверным паролем"""
        test_login = "testuser"
        test_password = "secretpassword"
        wrong_password = "wrongpassword"
        hashed_password = generate_password_hash(test_password)

        mock_user = MagicMock()
        mock_user.password_hash = hashed_password
        mock_get_user_by_login.return_value = mock_user

        mock_check_password.return_value = False

        data = {"login": test_login, "password": wrong_password}
        with self.assertRaises(ValueError) as context:
            login_user(data)

        self.assertEqual(str(context.exception), "Invalid login or password")
        mock_get_user_by_login.assert_called_once_with(test_login)
        mock_check_password.assert_called_once_with(hashed_password, wrong_password)

    def test_login_user_missing_fields(self):
        """Тестируем случай, когда отсутствуют необходимые поля"""
        data = {"login": "testuser"}

        with self.assertRaises(ValueError) as context:
            login_user(data)

        self.assertEqual(str(context.exception), "Login and password are required")


if __name__ == "__main__":
    unittest.main()


