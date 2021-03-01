from exceptions import BaseError
from configparser import ConfigParser
print('Relaoded')

class ExceptionManager:

	critical_exc_counter: int
	regular_exc_counter: int
	_config: ConfigParser

	def __init__(self, config: str = 'config.ini') -> None:
		self.critical_exc_counter = 0
		self.regular_exc_counter = 0
		self._config = ConfigParser()
		self._config.read(config)

	def is_critical(self, exc: BaseError) -> bool:
		exec_name = exc.__class__.__name__
		print(exec_name)
		return self._config.getboolean(exec_name, '_is_critical')

	def check(self, exc: Exception) -> None:
		if not issubclass(type(exc), BaseError):
			return
		if self.is_critical(exc):
			self.critical_exc_counter += 1
		else:
			self.regular_exc_counter += 1
