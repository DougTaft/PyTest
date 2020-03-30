
from datetime import datetime
today = datetime.now().strftime("%y-%m-%d")

class PythonProjects2():
    def __init__(self,msg):
        self.msg = msg
        self.print_message()
        util = Utilities()
        util.print_message_with_time(msg)

    def print_message(self):
        print(self.msg)

class Utilities():
    def print_message_with_time(self,msg):
        print(msg + ' @ ' + today)


bob = PythonProjects2("This is only a test")

bob.print_message()