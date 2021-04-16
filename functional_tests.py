from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(unittest.TestCase):	#(1)

	def setUp(self): 		#(3)
		self.browser = webdriver.Firefox()

	def tearDown(self): 	# (3)
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self): 		# (2)
		# Edith has heard about a cool new online to-do app. She goes
		# to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)		# (4)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)

		inputbox.send_keys('Buy peacock feathers')

		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows)
			)
		self.fail('Finish the test!')   # (5)


if __name__ == '__main__': 			# (6)
	unittest.main(warnings = 'ignore')		# (7)

