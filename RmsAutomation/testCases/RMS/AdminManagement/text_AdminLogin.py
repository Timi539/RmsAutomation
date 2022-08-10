import time


class Test_002_Admin_Login:
    baseURL ="https://non-recurring-qa-rms.seamlesshiring.com/"
    admin_email = "email@gmail.com"
    admin_password = "password"

    def test_adminLogin(self, setup2):
        self.driver = setup2
        time.sleep(5)
