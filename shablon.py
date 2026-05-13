
class IDatabaseConnection:
    def open(self):
        pass

    def close(self):
        pass


class IDatabaseCommand:
    def execute(self, query):
        pass


class IDatabaseTransaction:
    def begin(self):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass


class MySQLConnection(IDatabaseConnection):
    def open(self):
        print("MySQL базасына қосылды")

    def close(self):
        print("MySQL базасы жабылды")


class MySQLCommand(IDatabaseCommand):
    def execute(self, query):
        print("Сұраныс орындалды:", query)


class MySQLTransaction(IDatabaseTransaction):
    def begin(self):
        print("Транзакция басталды")

    def commit(self):
        print("Транзакция сақталды")

    def rollback(self):
        print("Транзакция қайтарылды")


class MySQLFactory:
    def create_connection(self):
        return MySQLConnection()

    def create_command(self):
        return MySQLCommand()

    def create_transaction(self):
        return MySQLTransaction()


factory = MySQLFactory()

connection = factory.create_connection()
command = factory.create_command()
transaction = factory.create_transaction()

connection.open()

transaction.begin()

command.execute("SELECT * FROM users")

transaction.commit()

connection.close()
