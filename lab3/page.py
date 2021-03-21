from selenium.webdriver.common.keys import Keys

from element import BasePageElement
from locators import PageLocators
from utils import hover_element


class InputTextElement(BasePageElement):

	locator = '.new-todo'


class BasePage:

	def __init__(self, driver):
		self.driver = driver


class Page(BasePage):

	todo_input = InputTextElement()

	def is_title_matches(self):
		return 'TodoMVC' in self.driver.title

	def add_task(self, task):
		self.todo_input = task
		element = self.driver.find_element(*PageLocators.INPUT)
		element.send_keys(Keys.RETURN)

	def __get_tasks(self):
		ul = self.driver.find_element(*PageLocators.TODO_LIST)
		return ul.find_elements_by_tag_name('li')

	def __get_task(self, idx):
		return self.__get_tasks()[idx - 1]

	def finish_task(self, task_idx):
		task = self.__get_task(task_idx)
		checkbox = task.find_element(*PageLocators.CHECKBOX)
		checkbox.click()

	def delete_task(self, task_idx):
		task = self.__get_task(task_idx)
		hover_element(self.driver, task)
		delete_btn = task.find_element(*PageLocators.DELETE_BTN)
		delete_btn.click()

	def get_task(self, task_idx):
		return self.__get_task(task_idx).text

	def go_to_active(self):
		self.driver.find_element(*PageLocators.ACTIVE_TASKS_BTN).click()

	def go_to_completed(self):
		self.driver.find_element(*PageLocators.COMPLETED_TASKS_BTN).click()

	def count_tasks(self):
		return len(self.__get_tasks())
