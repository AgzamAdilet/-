using System;

interface IDatabaseConnection
{
    void Open();
    void Close();
}

interface IDatabaseCommand
{
    void Execute(string query);
}

interface IDatabaseTransaction
{
    void Begin();
    void Commit();
    void Rollback();
}


class MySQLConnection : IDatabaseConnection
{
    public void Open()
    {
        Console.WriteLine("MySQL базасына қосылды");
    }

    public void Close()
    {
        Console.WriteLine("MySQL базасы жабылды");
    }
}


class MySQLCommand : IDatabaseCommand
{
    public void Execute(string query)
    {
        Console.WriteLine("Сұраныс орындалды: " + query);
    }
}


class MySQLTransaction : IDatabaseTransaction
{
    public void Begin()
    {
        Console.WriteLine("Транзакция басталды");
    }

    public void Commit()
    {
        Console.WriteLine("Транзакция сақталды");
    }

    public void Rollback()
    {
        Console.WriteLine("Транзакция қайтарылды");
    }
}


class MySQLFactory
{
    public IDatabaseConnection CreateConnection()
    {
        return new MySQLConnection();
    }

    public IDatabaseCommand CreateCommand()
    {
        return new MySQLCommand();
    }

    public IDatabaseTransaction CreateTransaction()
    {
        return new MySQLTransaction();
    }
}


public class Program
{
    public static void Main(string[] args)
    {
        MySQLFactory factory = new MySQLFactory();

        IDatabaseConnection connection = factory.CreateConnection();
        IDatabaseCommand command = factory.CreateCommand();
        IDatabaseTransaction transaction = factory.CreateTransaction();

        connection.Open();

        transaction.Begin();

        command.Execute("SELECT * FROM users");

        transaction.Commit();

        connection.Close();
    }
}
