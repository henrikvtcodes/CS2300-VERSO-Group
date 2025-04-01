import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class datetime_convert {
    public static void main(String[] args) {
        String dateStr = "2022-03-17 10:45:30"; //Start with a string of the date and time.
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"); //Create a formatter object with a specific pattern
        LocalDateTime dateObj = LocalDateTime.parse(dateStr, formatter); //create a date object using your provided date and time and the formatter you created
        String formattedDate = dateObj.format(DateTimeFormatter.ofPattern("MM/dd/yyyy HH:mm:ss")); //Create the string

        System.out.println(formattedDate);
    }
}
