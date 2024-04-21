/**
 * The purpose of the main class is to provide the player with instructions and begins 
 * a connectN game. 
 * 
 * @author Lekha Reddy
 */
package edu.wm.cs.cs301.connectn;

import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;

//import javax.swing.JOptionPane;

public class Main {


	public static void main(String[] args) {

        System.out.println(" \t\tWelcome Player!\n\n"
				+ " In this game you will alternate turns against\n a computer to be the first player to "
				+ "form a pattern of n\n consecutive symbols. N is based on the size of board\n that you choose The pattern may be vertical, horizontal, or diagonal.\n "
				+ "The objective is to complete the pattern before your \n opponent and in as few turns as possible.\n");
//		JOptionPane.showMessageDialog(null,	"        	                 Welcome Player! \n"
//				+ " In this game you will alternate turns against\n a computer to be the first player to"
//				+ "form a pattern of n\n consecutive symbols. The pattern may be vertical,\n horizontal, or diagonal. "
//				+ "The objective is to complete the\n pattern before your opponent and in as few turns as possible");
//		
	    
//	     File directory = new File("./resources/leaderboard.txt");
//	     Scanner myReader = null;
//		try {
//			myReader = new Scanner(directory);
//		} catch (FileNotFoundException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
//	      while (myReader.hasNextLine()) {
//	        String data = myReader.nextLine();
//	        System.out.println(data);
//	      }	
	      
		   new ConnectNGame();

		 
}}
