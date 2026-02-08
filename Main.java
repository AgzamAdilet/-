import java.util.ArrayList;
import java.util.List;

interface IPayment {
    void processPayment(double amount);
}

class CreditCardPayment implements IPayment {
    public void processPayment(double amount) { System.out.println("Картамен төленді: " + amount + " тг."); }
}

class PayPalPayment implements IPayment {
    public void processPayment(double amount) { System.out.println("PayPal-мен төленді: " + amount + " тг."); }
}
interface IDelivery {
    void deliverOrder(Order order);
}

class CourierDelivery implements IDelivery {
    public void deliverOrder(Order order) { System.out.println("Курьер арқылы жеткізу дайындалуда."); }
}

class PickUpPointDelivery implements IDelivery {
    public void deliverOrder(Order order) { System.out.println("Алып кету нүктесіне жіберілді."); }
}

interface INotification {
    void sendNotification(String message);
}

class EmailNotification implements INotification {
    public void sendNotification(String message) { System.out.println("Email: " + message); }
}

class DiscountCalculator {
    public double calculateDiscount(double amount) {
        return amount > 10000 ? amount * 0.1 : 0; 
    }
}

class Order {
    private List<Double> items = new ArrayList<>();
    private IPayment payment;
    private IDelivery delivery;

    public void addItem(double price) { items.add(price); }

    public void setPayment(IPayment payment) { this.payment = payment; }
    public void setDelivery(IDelivery delivery) { this.delivery = delivery; }

    public double calculateTotal() {
        return items.stream().mapToDouble(Double::doubleValue).sum();
    }

    public void process(DiscountCalculator calculator, INotification notification) {
        double total = calculateTotal();
        double discount = calculator.calculateDiscount(total);
        double finalPrice = total - discount;

        System.out.println("Тапсырыстың жалпы сомасы: " + total + " тг.");
        payment.processPayment(finalPrice);
        delivery.deliverOrder(this);
        notification.sendNotification("Тапсырыс сәтті өңделді!");
    }
}
public class Main {
    public static void main(String[] args) {
        Order order = new Order();
        order.addItem(15000.0);
        order.setPayment(new CreditCardPayment());
        order.setDelivery(new CourierDelivery());
        order.process(new DiscountCalculator(), new EmailNotification());
    }
}