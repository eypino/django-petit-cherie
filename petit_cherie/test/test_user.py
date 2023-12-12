import pytest
from apps.usuario.models import Usuario


def test_user_creation():
    user = Usuario.objects.create_user(
        username='dasdas',
        email='asdasda@gmail.com',
        password='12345'
    )
    assert user.username == 'dasdas'