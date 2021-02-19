"""
Лабораторна робота №1. Створення модульних тестів

Розробити систему управління виключними ситуаціями (ExceptionManager).
Система повинна виконувати наступні функції:
Визначення чи є виключна ситуація критичною. (Приймає об’єкти, які є нащадками класу Exception. Повертає булеве значення. Перелік виключних ситуацій, що є критичними зберігаємо безпосередньо в коді.)
Обробка виключних ситуацій. (Приймає об’єкти, які є нащадками класу Exception. Якщо оброблювана виключна ситуація є критичною - збільшує лічильник критичних виключних ситуацій, в іншому разі - збільшує лічильник звичайних виключних ситуацій.)

Покриття модульними тестами.
Необхідно покрити зазначений функціонал модульними тестами з позитивними та негативними сценаріями для різних видів виключних ситуацій.
Схожі тести об’єднати в параметризовані тести (атрибут [TestCase]) з передачею відповідних параметрів.
"""
from qa.exceptions import BaseError


class ExceptionManager:

	critical_exc_counter: int
	regular_exc_counter: int

	def __init__(self) -> None:
		self.critical_exc_counter = 0
		self.regular_exc_counter = 0

	def is_critical(self, exc: BaseError) -> bool:
		return exc.is_critical

	def check(self, exc: Exception) -> None:
		if not issubclass(type(exc), BaseError):
			return
		if self.is_critical(exc):
			self.critical_exc_counter += 1
		else:
			self.regular_exc_counter += 1
