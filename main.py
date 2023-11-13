from typing import Iterator

from flask import Flask, jsonify, request
import logging
from logging import config
from sqlalchemy.orm import Session

from src.domain.bulk.bulk_exception import BulkIdAlreadyExistsError, BulksNotFoundError
from src.domain.bulk.bulk_repository import BulkRepository
from src.infrastructure.sqlite.bulk.bulk_query_service import BulkQueryServiceImpl
from src.infrastructure.sqlite.bulk.bulk_repository import BulkRepositoryImpl, BulkCommandUseCaseUnitOfWorkImpl
from src.infrastructure.sqlite.database import SessionLocal, create_tables
from src.usecase.bulk.bulk_command_usecase import BulkCommandUseCase, BulkCommandUseCaseUnitOfWork, \
    BulkCommandUseCaseImpl
from src.usecase.bulk.bulk_query_service import BulkQueryService
from src.usecase.bulk.bulk_query_usecase import BulkQueryUseCase, BulkQueryUseCaseImpl

config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)


app = Flask(__name__)
create_tables()


def get_session() -> Iterator[Session]:
    """Get a session from the database."""
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def bulk_query_usecase(session: Session) -> BulkQueryUseCase:
    """Get a bulk query use case."""
    bulk_query_service: BulkQueryService = BulkQueryServiceImpl(session)
    return BulkQueryUseCaseImpl(bulk_query_service)


def bulk_command_usecase(session: Session) -> BulkCommandUseCase:
    """Get a bulk command use case."""
    bulk_repository: BulkRepository = BulkRepositoryImpl(session)
    uow: BulkCommandUseCaseUnitOfWork = BulkCommandUseCaseUnitOfWorkImpl(
        session, bulk_repository=bulk_repository
    )
    return BulkCommandUseCaseImpl(uow)


@app.route("/bulk", methods=['POST'])
def create_bulk():
    """Create a bulk."""
    try:
        data = request.json
        bulk_command_usecase = bulk_command_usecase(get_session())
        bulk = bulk_command_usecase.create_bulk(data)
        return jsonify(bulk)
    except BulkIdAlreadyExistsError as e:
        return jsonify({"error": e.message}), 409
    except Exception as e:
        logger.error(e)
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/bulk/status/<status>", methods=['GET'])
def get_bulk_status(
        status
):
    try:
        bulk_query_usecase = bulk_query_usecase(get_session())
        bulk = bulk_query_usecase.fetch_bulk_by_id(status)
        return jsonify(bulk)
    except BulksNotFoundError as err:
        return jsonify({"error": err.message}), 404
    except Exception as err:
        logger.error(err)
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    app.run(debug=True)
