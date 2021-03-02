from manager import ExceptionManager
from exceptions import CatIsNotFedError, KeyboardSpilledTeaError
from server import Server

import pytest


@pytest.mark.parametrize(
	'errors, critical_counter_expected, regular_counter_expected',
	[
		((), 0, 0),
		((CatIsNotFedError, CatIsNotFedError, CatIsNotFedError, KeyboardSpilledTeaError), 3, 1),
		((KeyboardSpilledTeaError, CatIsNotFedError, KeyboardSpilledTeaError), 1, 2),
	],
)
def test_counter(errors, critical_counter_expected, regular_counter_expected):
	em = ExceptionManager(Server())
	for error in errors:
		em.check(error())

	assert em.critical_exc_counter == critical_counter_expected
	assert em.regular_exc_counter == regular_counter_expected


@pytest.mark.parametrize(
	'error, critical',
	[(CatIsNotFedError, True), (KeyboardSpilledTeaError, False)],
)
def test_is_critical(error, critical):
	em = ExceptionManager(Server())
	assert em.is_critical(error()) is critical
