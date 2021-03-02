from exceptions import BaseError
from configparser import ConfigParser
from server import Server, Request, Response


class ExceptionManager:

	critical_exc_counter: int
	regular_exc_counter: int
	_config: ConfigParser
	_server: Server

	def __init__(self, server: Server, config: str = 'manager.ini') -> None:
		self._server = server
		self._config = ConfigParser()
		self._config.read(config)

		self.critical_exc_counter = 0
		self.regular_exc_counter = 0
		self.server_exc_not_handled = 0

	def is_critical(self, exc: BaseError) -> bool:
		exec_name = exc.__class__.__name__
		return self._config.getboolean(exec_name, '_is_critical')

	def server_handle_exc(self, exc: Exception) -> None:
		request = Request(exc)
		response = self._server.handle_request(request).status.value

		return response


	def check(self, exc: Exception) -> None:
		
		if not self.server_handle_exc(exc):
			self.server_exc_not_handled += 1

		if not issubclass(type(exc), BaseError):
			return

		if self.is_critical(exc):
			self.critical_exc_counter += 1
		else:
			self.regular_exc_counter += 1

