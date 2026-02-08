class Order {
    public String productName;
    public int quantity;
    public double price;
}

class PriceCalculator {
    public double calculateTotal(Order order) {
        return order.quantity * order.price * 0.9; // 10% скидка
    }
}

class PaymentService {
    public void processPayment(String details) {
        System.out.println("Payment processed: " + details);
    }
}

class EmailService {
    public void sendEmail(String email) {
        System.out.println("Email sent to: " + email);
    }
}

interface SalaryCalculator {
    double calculate(double baseSalary);
}

class PermanentSalary implements SalaryCalculator {
    public double calculate(double baseSalary) {
        return baseSalary * 1.2;
    }
}

class ContractSalary implements SalaryCalculator {
    public double calculate(double baseSalary) {
        return baseSalary * 1.1;
    }
}

class InternSalary implements SalaryCalculator {
    public double calculate(double baseSalary) {
        return baseSalary * 0.8;
    }
}

interface IPrint {
    void print(String content);
}

interface IScan {
    void scan(String content);
}

interface IFax {
    void fax(String content);
}

class BasicPrinter implements IPrint {
    public void print(String content) {
        System.out.println("Printing: " + content);
    }
}

class AllInOnePrinter implements IPrint, IScan, IFax {
    public void print(String content) {
        System.out.println("Printing: " + content);
    }

    public void scan(String content) {
        System.out.println("Scanning: " + content);
    }

    public void fax(String content) {
        System.out.println("Faxing: " + content);
    }
}

interface MessageSender {
    void send(String message);
}

class EmailSender implements MessageSender {
    public void send(String message) {
        System.out.println("Email sent: " + message);
    }
}

class SmsSender implements MessageSender {
    public void send(String message) {
        System.out.println("SMS sent: " + message);
    }
}

class NotificationService {
    private MessageSender sender;

    public NotificationService(MessageSender sender) {
        this.sender = sender;
    }

    public void notifyUser(String message) {
        sender.send(message);
    }
}

public class practika3 {
    public static void main(String[] args) {

        Order order = new Order();
        order.productName = "Laptop";
        order.quantity = 2;
        order.price = 500;

        PriceCalculator priceCalculator = new PriceCalculator();
        double total = priceCalculator.calculateTotal(order);
        System.out.println("Total price: " + total);

        PaymentService paymentService = new PaymentService();
        paymentService.processPayment("Card 1234");

        EmailService emailService = new EmailService();
        emailService.sendEmail("user@mail.com");


        // ===== OCP TEST =====
        SalaryCalculator permanent = new PermanentSalary();
        SalaryCalculator intern = new InternSalary();

        System.out.println("Permanent salary: " + permanent.calculate(1000));
        System.out.println("Intern salary: " + intern.calculate(1000));

        BasicPrinter basicPrinter = new BasicPrinter();
        basicPrinter.print("Hello World");

        AllInOnePrinter allPrinter = new AllInOnePrinter();
        allPrinter.print("Doc");
        allPrinter.scan("Doc");
        allPrinter.fax("Doc");

        NotificationService emailNotify = new NotificationService(new EmailSender());
        emailNotify.notifyUser("Hello via Email");

        NotificationService smsNotify = new NotificationService(new SmsSender());
        smsNotify.notifyUser("Hello via SMS");
    }
}