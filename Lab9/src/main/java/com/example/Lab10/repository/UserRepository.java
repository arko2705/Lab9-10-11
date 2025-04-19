package com.example.Lab10.repository;
import org.springframework.data.jpa.repository.JpaRepository; 
import com.example.Lab10.entity.User; 
public interface UserRepository extends JpaRepository<User, Long> { 
} 

