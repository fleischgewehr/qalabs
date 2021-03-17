from configparser import ConfigParser
from exceptions import BaseError
from enum import Enum
from typing import List


class Status(Enum):
	ERR = False
	OK = True

class Request():
	_exception: str

	def __init__(self, exc: BaseError) -> None:
		self._exception = exc.__class__.__name__

	@property
	def exception(self):
		return self._exception


class Response():
	_status: str

	def __init__(self, handled: bool) -> None:
		self._status = Status(handled)

	@property
	def status(self):
		return self._status


class Server():

	_allowed_errors: List[str] = [
	'KeyboardSpilledTeaError',
	'CatIsNotFedError'
	]

	def __init__(self, config='server.ini') -> None:
		pass

	def handle_request(self, request: Request) -> Response:
		exc = request.exception

		handled = exc in self._allowed_errors
		return self.send_response(handled)

	def send_response(self, handled:bool) -> Response:
		return Response(handled)




