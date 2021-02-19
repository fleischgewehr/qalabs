class BaseError(Exception):

	_is_critical: bool

	@property
	def is_critical(self):
		raise NotImplementedError


class CriticalError(BaseError):

	_is_critical = True

	@property
	def is_critical(self):
		return self._is_critical


class RegularError(BaseError):

	_is_critical = False

	@property
	def is_critical(self):
		return self._is_critical


class KeyboardSpilledTeaError(RegularError):
	"""Anyways, you bought it for 10 bucks."""
	pass


class CatIsNotFedError(CriticalError):
	"""You are dead meat."""
	pass
