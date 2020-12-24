import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        base_url = config.get('common info', 'base_url')
        return base_url

    @staticmethod
    def get_user_email():
        user_email = config.get('common info', 'user_email')
        return user_email

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
