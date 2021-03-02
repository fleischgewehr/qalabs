from typing import Optional
print('reloaded')

class BaseError(Exception):

	_is_critical: Optional[bool]

	@property
	def is_critical(self):
		return self._is_critical


class KeyboardSpilledTeaError(BaseError):
	"""Anyways, you bought it for 10 bucks."""
	_is_critical = None
	


class CatIsNotFedError(BaseError):
	"""You are dead meat."""
	_is_critical = None
	

class SomeExtraordinaryError(Exception):
	"""I don't even know what it is."""
	_is_critical = None