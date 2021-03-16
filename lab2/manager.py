from exceptions import BaseError
from configparser import ConfigParser
from server import Server, Request, Response

class ConfigParserFactory():

	def create_parser(self, conf_path:str) -> None:
		conf = ConfigParser()
		conf.read(conf_path)
		return conf



class ExceptionManager:

	critical_exc_counter: int
	regular_exc_counter: int
	_config: ConfigParser
	_server: Server

	def __init__(self, server: Server, 
		config: ConfigParser = ConfigParserFactory().create_parser('manager.ini')
		) -> None:

		self._server = server
		self._config = config

		self.critical_exc_counter = 0
		self.regular_exc_counter = 0
		self.server_exc_not_handled = 0

	@property
	def server(self) -> None:
		return self._server

	@server.getter
	def server(self, value:ConfigParser) -> None:
		self._server = value

	def is_critical(self, exc: BaseError) -> bool:
		exec_name = exc.__class__.__name__
		return self._config.getboolean(exec_name, '_is_critical')

	def server_handle_exc(self, exc: Exception) -> None:
		request = Request(exc)
		response = self._server.handle_request(request).status.value
		return response

	def server_exc_inc(self) -> None:
		self.server_exc_not_handled += 1;

	def check(self, exc: Exception) -> None:
		if not self.server_handle_exc(exc):
			self.server_exc_inc()

		if not issubclass(type(exc), BaseError):
			return

		if self.is_critical(exc):
			self.critical_exc_counter += 1
		else:
			self.regular_exc_counter += 1

