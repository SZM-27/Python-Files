import paramiko


class SSHClientHandler:
    def __init__(self, host, port, username, password):
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password
        self.__client = None
        self.__shell = None
        self.connect()

    def connect(self):
        self.__client = paramiko.SSHClient()
        self.__client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__client.connect(self.__host, port=self.__port, username=self.__username, password=self.__password)

    def open_shell(self):
        if self.__client:
            self.__shell = self.__client.invoke_shell()

    def send_shell_command(self, command):
        if self.__shell:
            self.__shell.send(command + "\n")
            output = ""
            while not self.__shell.recv_ready():
                pass
            while self.__shell.recv_ready():
                output += self.__shell.recv(4096).decode()
            self.save_output(command, output)

    from datetime import datetime

    today = datetime.now()
    year = today.year
    month = today.month
    day = today.day
    hour = today.hour
    minute = today.minute
    second = today.second

    open(f"config_backup_{year}-{month}-{day}-{hour}-{minute}-{second}.txt", "w").write()

    def __del__(self):
        if self.__client:
            self.__client.close()

    def save_output(self, command, output):
        pass

