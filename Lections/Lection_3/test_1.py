from testpage import OperationsHelper
import logging
"""
username: Fred123
password: 17fe38c02d
"""


def test_step_1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


# def test_step_2(email_input, password_input, error, submit, error_result, site):
#     input1 = site.find_element("xpath", email_input)
#     input1.send_keys(testdata["email"])
#     input2 = site.find_element("xpath", password_input)
#     input2.send_keys(testdata["password"])
#     btn = site.find_element("css", submit)
#     btn.click()
#     hello_text = site.find_element("xpath", '// *[ @ id = "app"] / main / nav / ul / li[3] / a').text
#     assert f'Hello, {testdata["email"]}' == hello_text


# test_step_1()

# css_selector = "span.mdc-text-field__ripple"
# print(site.get_element_property("css", css_selector, "height"))
#
# xpath = '//*[@id="login"]/div[1]/label/span[1]'
# print(site.get_element_property("xpath", xpath, "color"))
