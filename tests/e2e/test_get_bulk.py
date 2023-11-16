from unittest.mock import patch
from main import app


@patch('src.usecase.bulk.bulk_query_usecase.BulkQueryUseCaseImpl')
class TestGetBulk:
        
    def test_get_bulk_status(self, mock_bulk_query_usecase):
        mock_query_instance = mock_bulk_query_usecase.return_value
        mock_query_instance.fetch_bulks_by_status.return_value = [{'id': 1, 'status': 'TestStatus', 'name': 'TestBulk'}]
    
        response = app.test_client().get(f'/bulk/status/{6}')
        assert response.status_code == 200
        assert response.get_json() == []
    
