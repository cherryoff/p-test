from selenium import webdriver

from pages.auth_page import AuthPage

def test_main():
  a = AuthPage('Google')

  print(a.get_param())
  # print(selenium)

  driver = webdriver.Firefox()
  driver.get('https://google.com')

  assert a.get_param() == driver.title
