import unittest

from django.test import LiveServerTestCase

from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys

from blog.models import Category
from blog.factories import PostFactory, CategoryFactory
from users.factories import UserFactory
from django.conf import settings

class FunctionalTest(unittest.TestCase):
    def setUp(self):
        self.browser = Firefox()
        self.url = 'http://127.0.0.1:8000/'

    def tearDown(self):
        self.browser.quit()
        super().tearDown()

    def test_visit_index_page(self):
        title = "首页 - " + settings.MY_TITLE
        self.browser.get(self.url)
        self.assertIn(title, self.browser.title)
        self.assertIn('教程', self.browser.page_source)
        self.assertIn('分类', self.browser.page_source)
        self.assertIn('归档', self.browser.page_source)

    def test_visit_tutorial_list_page(self):
        title = "教程 - " + settings.MY_TITLE
        self.browser.get(self.url)
        self.browser.find_element_by_link_text("教程").click()
        self.assertIn(title, self.browser.title)
        self.assertIn('教程', self.browser.page_source)
        self.assertIn('分类', self.browser.page_source)
        self.assertIn('归档', self.browser.page_source)

    def test_visit_category_list_page(self):
        title = "分类 - " + settings.MY_TITLE
        self.browser.get(self.url)
        self.browser.find_element_by_link_text("分类").click()
        self.assertIn(title, self.browser.title)
        self.assertIn('教程', self.browser.page_source)
        self.assertIn('分类', self.browser.page_source)
        self.assertIn('归档', self.browser.page_source)

    def test_search(self):
        title = "搜索结果 - " + settings.MY_TITLE
        self.browser.get(self.url)
        self.browser.find_element_by_name('q').send_keys(Keys.RETURN)
        self.assertIn(title, self.browser.title)
        self.assertIn("请输入搜索关键词，例如 django", self.browser.page_source)

        self.browser.get(self.url)
        search_input = self.browser.find_element_by_name('q')
        search_input.clear()
        search_input.send_keys("no exist")
        search_input.send_keys(Keys.RETURN)
        self.assertIn(title, self.browser.title)
        self.assertIn("没有搜索到你想要的结果！", self.browser.page_source)

        self.browser.get(self.url)
        search_input = self.browser.find_element_by_name('q')
        search_input.clear()
        search_input.send_keys("post")
        search_input.send_keys(Keys.RETURN)
        self.assertIn(title, self.browser.title)
        self.assertNotIn('没有搜索到你想要的结果！', self.browser.page_source)

    def test_anonymous_user_visit_notification_list_page(self):
        title = "登录 - " + settings.MY_TITLE
        self.browser.get(self.url)
        self.browser.find_element_by_css_selector('.notification').click()
        self.assertIn(title, self.browser.title)
        self.assertIn("使用第三方账户账户登录", self.browser.page_source)

    def test_authenticated_user_visit_notification_list_page(self):
        title = "通知 - " + settings.MY_TITLE
        self.browser.get(self.url + 'admin/')
        self.browser.find_element_by_class_name('submit-row').find_element_by_tag_name('input').submit()
        self.browser.get(self.url)
        self.browser.find_element_by_css_selector('.notification').click()
        self.assertIn(title, self.browser.title)
        self.assertIn("通知", self.browser.page_source)
        self.assertIn("全部", self.browser.page_source)
        self.assertIn("未读", self.browser.page_source)


