package us.airraisin.dailyprogrammer;

import java.io.IOException;
import java.text.MessageFormat;
import java.util.Scanner;

public class PromptName 
{
    public static void main( String[] args )
    {
    	String name = null, userName = null;
    	int age = 0;
    
    	try (Scanner scanner = new Scanner(System.in)) { 
	    	while (name == null) {
		    	System.out.println("What is your name? ");
				name = scanner.next();
	    	}
	    	
	    	while (age <= 0) {
	    		System.out.println("What is your age? ");
	    		age = scanner.nextInt();
	    	}
	    	
	    	while (userName == null) {
	        	byte [] buff = new byte [1024];
		    	System.out.println("What is your Reddit username? ");
				userName = scanner.next();
	    	}
    	}
    	
    	System.out.println(MessageFormat.format("your name is {0}, you are {1} years old, and your username is {2}", name, age, userName));
    }
}
