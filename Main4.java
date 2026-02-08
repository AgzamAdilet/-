public class Main4 {

    // ===== DRY PRINCIPLE =====
    static class LoggerService {
        public void log(String level, String message) {
            System.out.println(level + ": " + message);
        }
    }

    static class Config {
        public static final String CONNECTION_STRING =
                "Server=myServer;Database=myDb;User Id=myUser;Password=myPass;";
    }

    static class DatabaseService {
        public void connect() {
            String connectionString = Config.CONNECTION_STRING;
            System.out.println("Database connected: " + connectionString);
        }
    }

    static class LoggingService {
        public void logToDatabase(String message) {
            String connectionString = Config.CONNECTION_STRING;
            System.out.println("Log saved: " + message);
        }
    }

    // ===== KISS PRINCIPLE =====
    static class NumberProcessor {
        public void processNumbers(int[] numbers) {
            if (numbers == null || numbers.length == 0) return;

            for (int number : numbers) {
                if (number > 0) {
                    System.out.println(number);
                }
            }
        }
    }

    static class Calculator {
        public int divide(int a, int b) {
            if (b == 0) return 0;
            return a / b;
        }
    }

    // ===== YAGNI PRINCIPLE =====
    static class User {
        private String name;
        private String email;

        public User(String name, String email) {
            this.name = name;
            this.email = email;
        }

        public String getName() {
            return name;
        }
    }

    static class FileReaderService {
        public String readFile(String filePath) {
            return "file content";
        }
    }

    static class ReportGenerator {
        public void generatePdfReport() {
            System.out.println("PDF report generated");
        }
    }

    // ===== MAIN METHOD =====
    public static void main(String[] args) {

        LoggerService logger = new LoggerService();
        logger.log("INFO", "Бағдарлама басталды");

        DatabaseService db = new DatabaseService();
        db.connect();

        NumberProcessor processor = new NumberProcessor();
        processor.processNumbers(new int[]{-1, 5, 10, -3, 7});

        Calculator calc = new Calculator();
        System.out.println("Divide result: " + calc.divide(10, 2));

        User user = new User("Adilet", "adilet@mail.com");
        System.out.println("User: " + user.getName());

        ReportGenerator report = new ReportGenerator();
        report.generatePdfReport();
    }
}
