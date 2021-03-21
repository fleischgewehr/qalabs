from selenium.webdriver import ActionChains


def hover_element(driver, element):
	action = ActionChains(driver)
	action.move_to_element(element)
	action.perform()
