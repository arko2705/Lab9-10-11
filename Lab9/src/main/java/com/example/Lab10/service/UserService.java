package com.example.Lab10.service; 
import org.apache.poi.ss.usermodel.*; 
import org.apache.poi.xssf.usermodel.XSSFWorkbook; 
import org.slf4j.Logger; 
import org.slf4j.LoggerFactory; 
import org.springframework.stereotype.Service; 
import org.springframework.transaction.annotation.Transactional; 
import org.springframework.web.multipart.MultipartFile; 
import com.example.Lab10.entity.User; 
import com.example.Lab10.repository.UserRepository; 
import java.io.IOException; 
import java.util.ArrayList; 
import java.util.List; 
import com.github.javafaker.Faker; 
@Service 
public class UserService { 
    private final Faker faker = new Faker(); // Initialize Faker

private final UserRepository userRepository; 
private final Logger logger = LoggerFactory.getLogger(UserService.class); 
public UserService(UserRepository userRepository) { 
this.userRepository = userRepository; 
} 
@Transactional 
public List<String> processFile(MultipartFile file) { 
List<String> errorLogs = new ArrayList<>(); 
try (Workbook workbook = new XSSFWorkbook(file.getInputStream())) { 
Sheet sheet = workbook.getSheetAt(0); 
for (int i = 1; i <= sheet.getLastRowNum(); i++) { // Skip header row 
Row row = sheet.getRow(i); 
try { 
Long userId = (long) row.getCell(0).getNumericCellValue(); // Assuming userId is numeric 
String name = row.getCell(1).getStringCellValue(); 
String email = row.getCell(2).getStringCellValue(); 
User user = new User(userId, name, email); 
userRepository.save(user); 
} catch (Exception e) { 
logger.error("Error processing row {}: {}", i, e.getMessage()); 
errorLogs.add("Row " + i + ": " + e.getMessage()); 
} 
} 
} catch (IOException e) { 
logger.error("Error reading file: {}", e.getMessage()); 
errorLogs.add("File error: " + e.getMessage()); 
} 
return errorLogs; 
} 
@Transactional
public List<User> generateBulkCustomers(int count) {
    List<User> users = new ArrayList<>();
    for (int i = 0; i < count; i++) {
        User user = new User();
        user.setUserId((long) (i + 1)); // Auto-increment ID (if not using DB auto-generation)
        user.setUser_id((long) (i + 1000)); // Custom user ID
        user.setName(faker.name().fullName()); // Random name
        user.setEmail(faker.internet().emailAddress()); // Random email
        users.add(user);
    }
    return userRepository.saveAll(users); // Batch insert
}
} 