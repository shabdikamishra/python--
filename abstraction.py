class Item:
    def __connect(self):
        pass

    def __prepare_body(self):
        return f"Hello, we have {self.name} in stock."

    def __send(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()