import time

from pageObjects.RMS.Authentication.CandidateLogin import CandidateLogin


class Test_001_Candidate_Login:
    baseURL ="https://non-recurring-qa-rms.seamlesshiring.com/"
    email = "Dakolo@seamlesshr.com"
    password = "password"


    def test_candidateLogin(self,setup1):
        self.driver = setup1
        time.sleep(5)
       # self.Lp=CandidateLogin(self.driver)
        #self.Lp.setEmail(self.email)
        #self.Lp.setPassword(self.password)

        #time.sleep(5)
        #self.Lp.clickLogin()
        #act_title=self.driver.title
        #if act_title=="SeamlessHiring":
           # assert True
       # else:
            #assert False

        #self.driver.close()
