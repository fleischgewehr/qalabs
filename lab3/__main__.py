import unittest
from selenium import webdriver

import page


class TodoTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.get('http://todomvc.com/examples/angularjs/')

	def test_todo_list(self):
		p = page.Page(self.driver)
		assert p.is_title_matches(), 'whoops, title mismatches'

		p.add_task('wake up')
		p.add_task('praise the sun')
		p.add_task('do nothing')
		p.add_task('take a rest')
		assert p.count_tasks() == 4, 'not all initial tasks were added'
		assert p.get_task(3) == 'do nothing', 'task mismatches'

		p.finish_task(1)
		p.go_to_completed()
		assert p.count_tasks() == 1, 'task was not completed'
		p.go_to_active()
		assert p.count_tasks() == 3, 'completed task is still in active'

		p.delete_task(2)
		assert p.count_tasks() == 2, 'task was not deleted'

	def tearDown(self):
		self.driver.close()


if __name__ == '__main__':
	unittest.main()
