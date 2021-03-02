from configparser import ConfigParser
from exceptions import BaseError
print('reloaded')

class Request():
	_exception: str

	def __init__(self, exc: BaseError) -> None:
		if not issubclass(type(exc), BaseError):
			raise TypeError
		else:
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

	def __init__(self, config='server.ini') -> None:
		pass

	def send_request(self, request: Request) -> Response:
		handled = True 
		return self.__send_responce(handled)

	def __send_responce(self, handled:bool) -> Response:
		return Response(handled)




