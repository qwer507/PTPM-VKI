from src.CheckLoginData import Authorization
from src.WorkWithUser import UserInteraction
from src.WorkWithEmail import OtherProgramInteraction
from src.WorkWithDB import WorkWithDB

class Controller:
    def __init__(self, auth: Authorization, db: WorkWithDB, user: UserInteraction, email: OtherProgramInteraction):
        self.check_login = auth
        self.db_interact = db
        self.user_interact = user
        self.email_interact = email

    def start(self):
        login_data = self.user_interact.getData()
        result = self.db_interact.find(login_data[0],login_data[1],login_data[2])
        if result is None:
            result = login_data + self.check_login.validation(login_data[0],login_data[1],login_data[2])
            self.db_interact.add(result[0],result[1],result[2],result[3],result[4])

        self.email_interact.sendInEmail(result)
        return result


