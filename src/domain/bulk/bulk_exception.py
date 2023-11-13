class BulkIdAlreadyExistsError(Exception):
    message = "The bulk with the Id code you specified already exists."

    def __str__(self):
        return BulkIdAlreadyExistsError.message


class BulksNotFoundError(Exception):
    """BulksNotFoundError is an error that occurs when bulks are not found."""
    message = "No bulks were found."

    def __str__(self):
        return BulksNotFoundError.message
