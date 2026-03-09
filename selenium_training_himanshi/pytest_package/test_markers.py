'''
Markers :   There are 2 types
            *   custom marker
            *   inbuilt marker

'''

import pytest

# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")

# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")

# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")

'''
skip
'''
# @pytest.mark.skip
# def test_login():
#     print("login executing")
#
# def test_reg():
#     print("reg executing")
#
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.skip
# def test_logout():
#     print("logout executing")

# @pytest.mark.skip
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#

'''
skipif  :   
'''

# @pytest.mark.skipif(True, reason="login already executed")
# def test_login():
#     print("login executing")

# @pytest.mark.skipif(False, reason="login already executed")
# def test_login():
#     print("login executing")

# @pytest.mark.skipif(reason="login already executed")
# def test_login():
#     print("login executing")

# @pytest.mark.skipif(True)
# def test_login():
#     print("login executing")

'''
xfail   :   
'''

# @pytest.mark.xfail
# def test_login():
#     raise Exception

# @pytest.mark.xfail
# def test_login():
#     print("login")
#
'''
paramterize     :   
'''

# @pytest.mark.parametrize("a, b", [(10, 20)])
# def test_add(a, b):
#     print(a + b)

# @pytest.mark.parametrize("a, b", [(10, 20), (1, 2), (10, -10), (1, 1)])
# def test_add(a, b):
#     print(a + b)


import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait_obj = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[TimeoutException])


@pytest.mark.parametrize("username, password", [('standard_user', 'secret_sauce'), ('abcdefgh', '12345678')])
def test_login(username, password):
    driver.get('https://www.saucedemo.com/')
    time.sleep(2)
    driver.find_element('id', 'user-name').send_keys(username)
    time.sleep(1)
    driver.find_element('id', 'password').send_keys(password)
    time.sleep(1)
    driver.find_element('id', 'login-button').click()
    time.sleep(3)

    assert wait_obj.until(EC.visibility_of_element_located(('xpath', '//span[text()="Products"]')))






























































































































































