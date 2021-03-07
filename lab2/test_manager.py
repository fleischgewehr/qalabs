from manager import ExceptionManager, ConfigParserFactory
from exceptions import CatIsNotFedError, KeyboardSpilledTeaError, SomeExtraordinaryError
from server import Server
from configparser import ConfigParser
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
def test_constructor(errors, critical_status, critical_counter_expected, regular_counter_expected):
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
def test_property(errors, critical_status, critical_counter_expected, regular_counter_expected):
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
def test_factory(errors, critical_status, critical_counter_expected, regular_counter_expected):
	config_creator = FakeConfigCreator().create_parser
	em = ExceptionManager(Server())
	
	for error, is_critical, in zip(errors, critical_status):
		config = config_creator(error)
		em.config = config
		em.check(error())

	assert em.critical_exc_counter == critical_counter_expected
	assert em.regular_exc_counter == regular_counter_expected



# @pytest.mark.parametrize(
# 	'error, critical',
# 	[(CatIsNotFedError, True), (KeyboardSpilledTeaError, False)],
# )
# def test_property(error, critical):
# 	em = ExceptionManager(Server())
# 	error.is_critical = critical
# 	em.is_critical = lambda error: error.is_critical

# 	assert em.is_critical(error()) is critical


# @pytest.mark.parametrize(
# 	'error, handled, crit_counter_exp, reg_counter_exp, server_counter_exp',
# 	[
# 	(CatIsNotFedError, True, 1, 0, 0), 
# 	#(KeyboardSpilledTeaError, False, 0, 1, 0),
# 	#(SomeExtraordinaryError, False, 0, 0, 1)
# 	],
# )
# def test_server_exc_counter(error, handled, crit_counter_exp, reg_counter_exp, server_counter_exp):
# 	em = ExceptionManager(Server())

# 	em.server_handle_exc = lambda _: handled

# 	em.check(error)
# 	print(error)
# 	print(em.critical_exc_counter)
# 	print(crit_counter_exp)

# 	assert em.critical_exc_counter == crit_counter_exp
# 	#assert em.regular_exc_counter == reg_counter_exp
# 	#assert em.server_exc_not_handled == server_counter_exp