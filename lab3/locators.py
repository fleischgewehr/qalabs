from selenium.webdriver.common.by import By


class PageLocators:

	TODO_LIST = By.CLASS_NAME, 'todo-list'
	INPUT = By.CLASS_NAME, 'new-todo'
	CHECKBOX = By.CLASS_NAME, 'toggle'
	DELETE_BTN = By.CLASS_NAME, 'destroy'
	ACTIVE_TASKS_BTN = By.LINK_TEXT, 'Active'
	COMPLETED_TASKS_BTN = By.LINK_TEXT, 'Completed'
