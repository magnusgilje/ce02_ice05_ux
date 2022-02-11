"""hugo pytest suite"""
# pylint: disable=unused-import, import-error, no-member

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class TestHugo:
    """Test Hugo site with Selenium"""

    def get_default_url(self,url):
        """get default url for site"""
        # pylint: disable=no-self-use, no-else-return

        if url[-1] != "/":
            return url + "/"
        else:
            return url

    def get_default_title(self):
        """get default title for site"""
        # pylint: disable=no-self-use
        return "Magnus's site"

    def get_button_by_link_name(self, linktext):
        """find a button based on in its link text"""
        return self.driver.find_element(By.LINK_TEXT, linktext)

    def wait_for_page_to_load(self,url,title):
        """wait 15 seconds to allow a page to fully load"""
        self.driver.get(url)
        WebDriverWait(self.driver, 15).until(
            lambda driver: title in self.driver.title
        )

    def load_index_page(self,url):
        """get the site main page"""
        self.wait_for_page_to_load(url,self.get_default_title())


    def test_index_page(self,url):
        """test the index page for a hugo site"""
        page_url = self.get_default_url(url)
        title = self.get_default_title()

        self.load_index_page(url)
        assert title == self.driver.title
        assert page_url == self.driver.current_url
        self.driver.save_screenshot("test_index_page_00.png")

    def test_lunchtime_post(self,url):
        """test the lunchtime post"""
        self.load_index_page(url)

        page_url = self.get_default_url(url)+"posts/lunchtime/"
        page_title = "Lunchtime | "+self.get_default_title()

        second_post = self.get_button_by_link_name("Lunchtime")
        second_post.click()

        self.wait_for_page_to_load(page_url,page_title)

        assert page_title == self.driver.title
        assert page_url == self.driver.current_url

        # social media links

        facebook_placeholder = self.driver.find_element(By.CSS_SELECTOR,'.facebook')
        assert facebook_placeholder is not None

        twitter_placeholder = self.driver.find_element(By.CSS_SELECTOR,".twitter")
        assert twitter_placeholder is not None

        linedin_placeholder = self.driver.find_element(By.CSS_SELECTOR,".linkedin")
        assert linedin_placeholder is not None


        self.driver.save_screenshot("test_lunchtime_page_00.png")

    def test_afternoon_post(self,url):
        """test the afternoon post"""
        self.load_index_page(url)

        page_url = self.get_default_url(url)+"posts/afternoon/"
        page_title = "RASCI | "+self.get_default_title()

        second_post = self.get_button_by_link_name("RASCI")
        second_post.click()

        self.wait_for_page_to_load(page_url,page_title)

        assert page_title == self.driver.title
        assert page_url == self.driver.current_url

        # social media links

        facebook_placeholder = self.driver.find_element(By.CSS_SELECTOR, '.facebook')
        assert facebook_placeholder is not None

        twitter_placeholder = self.driver.find_element(By.CSS_SELECTOR,".twitter")
        assert twitter_placeholder is not None

        linedin_placeholder = self.driver.find_element(By.CSS_SELECTOR,".linkedin")
        assert linedin_placeholder is not None


        self.driver.save_screenshot("test_afternoon_page_00.png")

    def test_another_page_post(self,url):
        """test the another_page post"""
        self.load_index_page(url)

        page_url = self.get_default_url(url)+"posts/another_page/"
        page_title = "Another_page | "+self.get_default_title()

        second_post = self.get_button_by_link_name("Another_page")
        second_post.click()

        self.wait_for_page_to_load(page_url,page_title)

        assert page_title == self.driver.title
        assert page_url == self.driver.current_url

        # social media links

        facebook_placeholder = self.driver.find_element(By.CSS_SELECTOR, '.facebook')
        assert facebook_placeholder is not None

        twitter_placeholder = self.driver.find_element(By.CSS_SELECTOR,".twitter")
        assert twitter_placeholder is not None

        linedin_placeholder = self.driver.find_element(By.CSS_SELECTOR,".linkedin")
        assert linedin_placeholder is not None


        self.driver.save_screenshot("test_another_page_page_00.png")

    def test_afternoon_post(self,url):
        """test the phoenix post"""
        self.load_index_page(url)

        page_url = self.get_default_url(url)+"posts/phoenix/"
        page_title = "Phoenix Project RASCI | "+self.get_default_title()

        second_post = self.get_button_by_link_name("Phoenix Project RASCI")
        second_post.click()

        self.wait_for_page_to_load(page_url,page_title)

        assert page_title == self.driver.title
        assert page_url == self.driver.current_url

        # social media links

        facebook_placeholder = self.driver.find_element(By.CSS_SELECTOR, '.facebook')
        assert facebook_placeholder is not None

        twitter_placeholder = self.driver.find_element(By.CSS_SELECTOR,".twitter")
        assert twitter_placeholder is not None

        linedin_placeholder = self.driver.find_element(By.CSS_SELECTOR,".linkedin")
        assert linedin_placeholder is not None


        self.driver.save_screenshot("test_phoenix_page_00.png")

    def test_my_first_post_post(self,url):
        """test the my-first-post post"""
        self.load_index_page(url)

        page_url = self.get_default_url(url)+"posts/my-first-post/"
        page_title = "My First Post | "+self.get_default_title()

        second_post = self.get_button_by_link_name("My First Post")
        second_post.click()

        self.wait_for_page_to_load(page_url,page_title)

        assert page_title == self.driver.title
        assert page_url == self.driver.current_url

        # social media links

        facebook_placeholder = self.driver.find_element(By.CSS_SELECTOR, '.facebook')
        assert facebook_placeholder is not None

        twitter_placeholder = self.driver.find_element(By.CSS_SELECTOR,".twitter")
        assert twitter_placeholder is not None

        linedin_placeholder = self.driver.find_element(By.CSS_SELECTOR,".linkedin")
        assert linedin_placeholder is not None


        self.driver.save_screenshot("test_my-first-post_page_00.png")


# pytest test_hugo.py -v --url http://localhost
# pytest test_hugo.py -v --url http:///ce02ice05.s3-website-eu-west-1.amazonaws.com/ --headless=yes
# pytest test_hugo.py -v --url http://stakubdevce02001huice05.z16.web.core.windows.net/ --headless=yes

    # def test_azure_post(self,url):
    #     """test the azure post"""
    #     self.load_index_page(url)

    #     page_url = self.get_default_url(url)+"posts/azure/"
    #     page_title = "Azure | "+self.get_default_title()

    #     second_post = self.get_button_by_link_name("Azure")
    #     second_post.click()

    #     self.wait_for_page_to_load(page_url,page_title)

    #     assert page_title == self.driver.title
    #     assert page_url == self.driver.current_url

    #     # social media links

    #     facebook_placeholder = self.driver.find_element_by_css_selector('.facebook')
    #     assert facebook_placeholder is not None

    #     twitter_placeholder = self.driver.find_element_by_css_selector(".twitter")
    #     assert twitter_placeholder is not None

    #     linedin_placeholder = self.driver.find_element_by_css_selector(".linkedin")
    #     assert linedin_placeholder is not None


    #     # mermaid diagram

    #     mermaid_placeholder = self.driver.find_element_by_class_name("mermaid")
    #     assert mermaid_placeholder is not None

    #     self.driver.save_screenshot("test_azure_page_00.png")

    # def test_aws_post(self,url):
    #     """test the aws post"""
    #     self.load_index_page(url)

    #     page_url = self.get_default_url(url)+"posts/aws/"
    #     page_title = "Aws | "+self.get_default_title()

    #     second_post = self.get_button_by_link_name("Aws")
    #     second_post.click()

    #     self.wait_for_page_to_load(page_url,page_title)

    #     assert page_title == self.driver.title
    #     assert page_url == self.driver.current_url

    #     # social media links

    #     facebook_placeholder = self.driver.find_element_by_css_selector('.facebook')
    #     assert facebook_placeholder is not None

    #     twitter_placeholder = self.driver.find_element_by_css_selector(".twitter")
    #     assert twitter_placeholder is not None

    #     linedin_placeholder = self.driver.find_element_by_css_selector(".linkedin")
    #     assert linedin_placeholder is not None


    #     self.driver.save_screenshot("test_aws_page_00.png")


    # def test_gcp_post(self,url):
    #     """test the gcp post"""
    #     self.load_index_page(url)

    #     page_url = self.get_default_url(url)+"posts/gcp/"
    #     page_title = "Gcp | "+self.get_default_title()

    #     second_post = self.get_button_by_link_name("Gcp")
    #     second_post.click()

    #     self.wait_for_page_to_load(page_url,page_title)

    #     assert page_title == self.driver.title
    #     assert page_url == self.driver.current_url

    #     # social media links

    #     facebook_placeholder = self.driver.find_element_by_css_selector('.facebook')
    #     assert facebook_placeholder is not None

    #     twitter_placeholder = self.driver.find_element_by_css_selector(".twitter")
    #     assert twitter_placeholder is not None

    #     linedin_placeholder = self.driver.find_element_by_css_selector(".linkedin")
    #     assert linedin_placeholder is not None



    #     self.driver.save_screenshot("test_gcp_page_00.png")

