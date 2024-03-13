import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


"""
username: Fred123
password: 17fe38c02d
"""


def test_step_1(email_input, password_input, error, submit, error_result, site):
    input1 = site.find_element("xpath", email_input)
    input1.send_keys("test")
    input2 = site.find_element("xpath", password_input)
    input2.send_keys("test")
    btn = site.find_element("css", submit)
    btn.click()
    err_label = site.find_element("xpath", error)
    assert err_label.text == error_result


# test_step_1()

# css_selector = "span.mdc-text-field__ripple"
# print(site.get_element_property("css", css_selector, "height"))
#
# xpath = '//*[@id="login"]/div[1]/label/span[1]'
# print(site.get_element_property("xpath", xpath, "color"))
