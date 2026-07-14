from datetime import datetime

from src.core.execution_context import (
    ExecutionContext
)


def test_should_create_execution_context():

    context = ExecutionContext(
        started_at=datetime.now()
    )

    assert context.results == []