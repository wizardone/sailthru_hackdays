class User:
    email = 'no@no.com'
    def __init__(name, age):
        self.name = name
        self.age = age

    def display_from_file(filename):
        f = open(filename, 'r')
        for line in f:
            lines.append(line.strip('\n'))
        return lines

    def execute(cmd):
        try:
            retcode = subprocess.call(cmd, shell=True)
        except OSError as e:
            print("Something went wrong")

    def test():
        print("I am a test")
