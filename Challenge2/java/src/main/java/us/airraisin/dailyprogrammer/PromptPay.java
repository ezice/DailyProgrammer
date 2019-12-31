package us.airraisin.dailyprogrammer;

import java.io.IOException;
import java.text.MessageFormat;
import java.util.Scanner;

public class PromptPay 
{
    public static void main( String[] args )
    {
    	int hoursPerWeek = 0, salary = 0, rate = 0;
    	boolean valid = false;
    
    	try (Scanner scanner = new Scanner(System.in)) { 
        	while (!valid) {
        		int answered = 0;
        		System.out.println("Please answer two of the three following questions.  Enter 0 to calculate.");
        		
	    		System.out.println("What is your hourly pay rate? ");
	    		rate = scanner.nextInt();
		    	
	    		System.out.println("How many hours per week do you work? ");
	    		hoursPerWeek = scanner.nextInt();
	    	
	    		System.out.println("What is your expected annual salary? ");
	    		salary = scanner.nextInt();
		    	
		    	if (rate != 0) answered++; 
		    	if (hoursPerWeek != 0) answered++; 
		    	if (salary != 0) answered++; 
		    	
		    	if (answered > 2) {
		    		System.out.println("Please answer only two of the questions.\n\n");	    		
		    	} else if (answered < 2) {
		    		System.out.println("You must answer two of the questions.\n\n");
		    	} else {
		    		valid = true;
		    	}
        	}
    	}
    	
    	if (salary == 0) {
    		salary = rate * hoursPerWeek * 52;
    		System.out.println(MessageFormat.format("At ${0}/hr, working {1} hours per week, your annual salary is ${2}", rate, hoursPerWeek, salary));
    	} else if (rate == 0) {
    		rate =  salary / (hoursPerWeek * 52);
    		System.out.println(MessageFormat.format("working {1} hours per week, to make {2}, you''ll need to make {0} per hour", rate, hoursPerWeek, salary));
    	} else {
    		hoursPerWeek = salary / (rate * 52);
    		System.out.println(MessageFormat.format("working at {0}/hr, to make {2}, you'll need to work {1} per week", rate, hoursPerWeek, salary));
    	}
    }
}
