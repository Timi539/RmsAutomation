import configparser

config = configparser.RawConfigParser()
config.read("Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        email = config.get('common info','email')
        return email


    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password

    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getAdminemail():
        admin_email = config.get('common info', 'admin_email')
        return admin_email

    @staticmethod
    def getAdminpassword():
        admin_password = config.get('common info', 'admin_password')
        return admin_password


