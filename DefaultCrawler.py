from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class DefaultCrawler:
	instruction = None
	crawler_object = None
	def __init__(self, instruction):
		self.instruction = instruction
		self.crawler_object = {'log': [], 'products': [], 'descriptions': []}

	def execute(self):
		method = self.instruction.get_kind_display().lower()
		if method == 'product':
			self.product()
		elif method == 'solution':
			self.solution()
		else:
			self.service()
		return self.crawler_object
	
	def product(self):
		chrome_options = Options()
		chrome_options.add_argument("--start-maximized")
		driver = webdriver.Chrome(chrome_options=chrome_options)
		driver.get(self.instruction.url)
		driver.find_element_by_partial_link_text('PRODUTOS').click()
		product_container = driver.find_elements_by_css_selector('div.section')
		outher_product_container = driver.find_elements_by_css_selector('div.aio-icon-component')
		products = []
		descriptions = []
		for element in product_container:
			self.crawler_object['products'].append(element.find_element_by_css_selector('h2.vc_custom_heading').text)
			self.crawler_object['descriptions'].append(element.find_element_by_css_selector('p').text)
		for element in outher_product_container:
			self.crawler_object['products'].append(element.find_element_by_class_name('aio-icon-title').text)
			self.crawler_object['descriptions'].append(element.find_element_by_css_selector('p:nth-child(2)').text)
		driver.close()
		return

	def solution(self):
		chrome_options = Options()
		chrome_options.add_argument("--start-maximized")
		driver = webdriver.Chrome(chrome_options=chrome_options)
		driver.get(self.instruction.url)
		driver.find_element_by_partial_link_text('SOLUÇÕES').click()
		containers = driver.find_elements_by_css_selector('div.aio-icon-box')
		products = []
		descriptions = []
		for element in containers:
			self.crawler_object['products'].append(element.find_element_by_class_name('aio-icon-title').text)
			self.crawler_object['descriptions'].append(element.find_element_by_css_selector('p:nth-child(2)').text)
		driver.close()

	def service(self):
		chrome_options = Options()
		chrome_options.add_argument("--start-maximized")
		driver = webdriver.Chrome(chrome_options=chrome_options)
		driver.get(self.instruction.url)
		driver.find_element_by_partial_link_text('CONSULTORIA').click()
		containers = driver.find_elements_by_css_selector('div.aio-icon-box')
		products = []
		descriptions = []
		for element in containers:
			self.crawler_object['products'].append(element.find_element_by_class_name('aio-icon-title').text)
			self.crawler_object['descriptions'].append(element.find_element_by_css_selector('p:nth-child(2)').text)
		driver.close()