from manager import ExceptionManager, ConfigParserFactory
from exceptions import CatIsNotFedError, KeyboardSpilledTeaError, SomeExtraordinaryError
from server import Server, Response

from configparser import ConfigParser
from unittest.mock import MagicMock

import pytest


class FakeConfigParser(ConfigParser):
	is_critical: bool

	def getboolean(self, *_):
		return self.is_critical


class FakeConfigCreator(ConfigParserFactory):
	def create_parser(self, is_critical):
		parser = FakeConfigParser()
		parser.is_critical = is_critical
		return parser


@pytest.mark.parametrize(
	'errors, critical_status, critical_counter_expected, regular_counter_expected',
	[
		((CatIsNotFedError, KeyboardSpilledTeaError),(True,False), 1, 1),
		((CatIsNotFedError, CatIsNotFedError),(True,True), 2, 0),
		((KeyboardSpilledTeaError, KeyboardSpilledTeaError),(False,False), 0, 2),
	],
)
def test_constructor(errors, critical_status,
	critical_counter_expected, regular_counter_expected):
	config = FakeConfigParser() 
	em = ExceptionManager(Server(), config)
	
	for error, is_critical, in zip(errors, critical_status):
		config.is_critical = is_critical
		em.check(error())

	assert em.critical_exc_counter == critical_counter_expected
	assert em.regular_exc_counter == regular_counter_expected


@pytest.mark.parametrize(
	'errors, critical_status, critical_counter_expected, regular_counter_expected',
	[
		((CatIsNotFedError, KeyboardSpilledTeaError),(True,False), 1, 1),
		((CatIsNotFedError, CatIsNotFedError),(True,True), 2, 0),
		((KeyboardSpilledTeaError, KeyboardSpilledTeaError),(False,False), 0, 2),
	],
)
def test_property(errors, critical_status,
 	critical_counter_expected, regular_counter_expected):
	config = FakeConfigParser() 
	em = ExceptionManager(Server())
	
	for error, is_critical, in zip(errors, critical_status):
		config.is_critical = is_critical
		em.config = config
		em.check(error())

	assert em.critical_exc_counter == critical_counter_expected
	assert em.regular_exc_counter == regular_counter_expected


@pytest.mark.parametrize(
	'errors, critical_status, critical_counter_expected, regular_counter_expected',
	[
		((CatIsNotFedError, KeyboardSpilledTeaError),(True,False), 1, 1),
		((CatIsNotFedError, CatIsNotFedError),(True,True), 2, 0),
		((KeyboardSpilledTeaError, KeyboardSpilledTeaError),(False,False), 0, 2),
	],
)
def test_factory(errors, critical_status, 
	critical_counter_expected, regular_counter_expected):
	config_creator = FakeConfigCreator().create_parser
	em = ExceptionManager(Server())
	
	for error, is_critical, in zip(errors, critical_status):
		config = config_creator(error)
		em.config = config
		em.check(error())

	assert em.critical_exc_counter == critical_counter_expected
	assert em.regular_exc_counter == regular_counter_expected


@pytest.mark.parametrize(
	'errors, critical_counter_expected, regular_counter_expected',
	[
		((CatIsNotFedError, KeyboardSpilledTeaError), 1, 1),
		((CatIsNotFedError, CatIsNotFedError), 2, 0),
		((KeyboardSpilledTeaError, KeyboardSpilledTeaError), 0, 2),
	],
)
def test_server_handle_error(errors, critical_counter_expected, 
	regular_counter_expected):
	mock_server = Server()
	mock_server.handle_request = MagicMock(return_value=Response(False))
	em = ExceptionManager(server = mock_server)
	
	for error in errors:
		em.check(error())

	assert em.critical_exc_counter == critical_counter_expected
	assert em.regular_exc_counter == regular_counter_expected
	assert em.server_exc_not_handled == len(errors)
