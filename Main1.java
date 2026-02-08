import java.util.ArrayList;
import java.util.List;

class User {
    private String name;
    private String email;
    private String role;

    public User(String name, String email, String role) {
        this.name = name;
        this.email = email;
        this.role = role;
    }

    public String getEmail() {
        return email;
    }

    public void update(String name, String email, String role) {
        this.name = name;
        this.email = email;
        this.role = role;
    }

    @Override
    public String toString() {
        return name + " | " + email + " | " + role;
    }
}

class UserManager {
    private List<User> users = new ArrayList<>();

    public void addUser(User user) {
        users.add(user);
    }

    public void removeUser(String email) {
        users.removeIf(u -> u.getEmail().equals(email));
    }

    public void updateUser(String email, String newName, String newEmail, String newRole) {
        for (User user : users) {
            if (user.getEmail().equals(email)) {
                user.update(newName, newEmail, newRole);
            }
        }
    }

    public void printUsers() {
        for (User user : users) {
            System.out.println(user);
        }
    }
}

public class Main1 {
    public static void main(String[] args) {

        UserManager manager = new UserManager();

        manager.addUser(new User("Adilet", "a@mail.com", "Admin"));
        manager.addUser(new User("Ali", "ali@mail.com", "User"));

        System.out.println("Users:");
        manager.printUsers();

        manager.updateUser("ali@mail.com", "Alihan", "alih@mail.com", "User");

        System.out.println("\nAfter update:");
        manager.printUsers();

        manager.removeUser("a@mail.com");

        System.out.println("\nAfter remove:");
        manager.printUsers();
    }
}
