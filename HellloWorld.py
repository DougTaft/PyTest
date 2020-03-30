#print('Hello World')

class PythonProjects():
    def say_hello(self):
        print('Hello World!')
    def print_fullname(self):
        first_name = 'bob'
        last_name = 'robertson'
        full_name = first_name + ' ' + last_name
        print(full_name.title())

bob = PythonProjects()

bob.say_hello()
bob.print_fullname()