from flask import Blueprint
from ..models.exeptions import BadRequest, InsufficientStorage, NotModified, CustomException, FilmNotFound, InvalidDataError

errors = Blueprint("errors", __name__)


