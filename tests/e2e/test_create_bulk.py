from http import HTTPStatus
from unittest.mock import patch

from main import app
from src.domain.bulk.bulk_exception import BulkIdAlreadyExistsError


@patch('src.usecase.bulk.bulk_command_usecase.BulkCommandUseCaseImpl')
class TestCreateBulk:
    def test_create_bulk(self, mock_create_bulk):
        data = {
            'status': 1,
            'name': 'TestBulk'
        }

        response = app.test_client().post('/bulk', json=data)
        assert response.status_code == HTTPStatus.NO_CONTENT.value


    def test_create_bulk_internal_error(self, mock_create_bulk):
        mock_create_bulk.create_bulk.return_value = Exception("Internal Server Error")

        data = {
            'status': 1,
        }

        response = app.test_client().post('/bulk', json=data)
        assert response.status_code == 500
        assert response.get_json() == {'error': 'Internal Server Error'}
    