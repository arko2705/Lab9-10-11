package com.example.Lab10.controller; 
import org.springframework.beans.factory.annotation.Autowired; 
import org.springframework.http.ResponseEntity; 
import org.springframework.web.bind.annotation.*; 
import org.springframework.web.multipart.MultipartFile; 
import com.example.Lab10.service.UserService; 
import com.example.Lab10.entity.*;

import java.util.List; 
@RestController 
@RequestMapping("/customers") 
public class UserController { 
@Autowired 
private UserService userService; 
@PostMapping("/upload") 
public ResponseEntity<?> uploadFile(@RequestParam("file") MultipartFile file) { 
List<String> errorLogs = userService.processFile(file); 
if (errorLogs.isEmpty()) { 
return ResponseEntity.ok("File processed successfully!"); 
} else { 
return ResponseEntity.status(207).body(errorLogs); // Partial success 
} 
}

@PostMapping("/generate")
public ResponseEntity<List<User>> generateBulkCustomers(
        @RequestParam(defaultValue = "10") int count) {
    List<User> users = userService.generateBulkCustomers(count);
    return ResponseEntity.ok(users);
}

}