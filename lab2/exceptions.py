from typing import Optional

class BaseError(Exception):

	_is_critical: Optional[bool]

	@property
	def is_critical(self):
		return self._is_critical


class KeyboardSpilledTeaError(Exception):
	"""Anyways, you bought it for 10 bucks."""
	_is_critical = None
	


class CatIsNotFedError(Exception):
	"""You are dead meat."""
	_is_critical = None
	
