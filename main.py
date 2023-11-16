from flask import Flask, jsonify, request
import logging
from logging import config
from sqlalchemy.orm import Session

from docs.swagger_docs import bulk_create_doc, get_bulk_status_doc
from src.domain.bulk.bulk_repository import BulkRepository
from src.infrastructure.sqlite.bulk.bulk_query_service import (
    BulkQueryServiceImpl
)
from src.infrastructure.sqlite.bulk.bulk_repository import (
    BulkRepositoryImpl,
    BulkCommandUseCaseUnitOfWorkImpl
)
from src.infrastructure.sqlite.database import (
    SessionLocal,
    create_tables
)
from src.usecase.bulk.bulk_command_model import BulkCreateModel
from src.usecase.bulk.bulk_command_usecase import (
    BulkCommandUseCase,
    BulkCommandUseCaseUnitOfWork,
    BulkCommandUseCaseImpl
)
from src.usecase.bulk.bulk_query_service import BulkQueryService
from src.usecase.bulk.bulk_query_usecase import (
    BulkQueryUseCase, BulkQueryUseCaseImpl
)
from flasgger import Swagger
from flasgger.utils import swag_from

config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)


app = Flask(__name__)
Swagger(app)
create_tables()


def get_session() -> Session:
    """Get a session from the database."""
    session: Session = SessionLocal()
    try:
        return session
    finally:
        session.close()


def bulk_query_usecase(session: Session = get_session()) -> BulkQueryUseCase:
    """Get a bulk query use case."""
    bulk_query_service: BulkQueryService = BulkQueryServiceImpl(session)
    return BulkQueryUseCaseImpl(bulk_query_service)


def bulk_command_usecase(session: Session = get_session()) -> BulkCommandUseCase:
    """Get a bulk command use case."""
    bulk_repository: BulkRepository = BulkRepositoryImpl(session)
    uow: BulkCommandUseCaseUnitOfWork = BulkCommandUseCaseUnitOfWorkImpl(
        session, bulk_repository=bulk_repository
    )
    return BulkCommandUseCaseImpl(uow)


@app.route("/bulk", methods=['POST'])
@swag_from(bulk_create_doc)
def create_bulk(
    bulk_command_usecase=bulk_command_usecase()
):
    """Create a bulk."""
    try:
        data = request.json
        bulk_command_usecase.create_bulk(
            BulkCreateModel(
                **data
            )
        )
        return jsonify({}), 204
    except Exception as e:
        logger.error(e)
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/bulk/status/<status>", methods=['GET'])
@swag_from(get_bulk_status_doc)
def get_bulk_status(
        status,
        bulk_query_usecase=bulk_query_usecase()
):
    try:
        bulk = bulk_query_usecase.fetch_bulks_by_status(status)
        return jsonify(bulk)
    except Exception as err:
        logger.error(err)
        return jsonify({"error": f"Internal Server Error :: {err}"}), 500
