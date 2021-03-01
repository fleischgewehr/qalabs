from configparser import ConfigParser
from exceptions import BaseError
print('reloaded')

class Request():
	_exception: str

	def __init__(self, exc: BaseError) -> None:
		self._exception = exc.__class__.__name__

	@property
	def exception(self):
		return self._exception


class Response():
	_handled: bool

	def __init__(self, handled: bool) -> None:
		self._handled = handled

	@property
	def handled(self):
		return self._handled


class Server():
	_config: ConfigParser

	def __init__(self, config='server.ini') -> None:
		self._config = ConfigParser()
		self._config.read(config)

	def send_request(self, request: Request) -> Response:
		exec_name = request.exception
		handled = self._config.getboolean(exec_name, '_can_handle')
		return self.__send_responce(handled)

	def __send_responce(self, handled:bool) -> Response:
		return Response(handled)




