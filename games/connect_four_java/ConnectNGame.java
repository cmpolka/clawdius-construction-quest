/**
 * The purpose of the ConnectNGame class is to begin a game with a game board of the correct size
 * and then alternate turns between HumanPlayer and ComputerPlayer. It also checks for when the game has been 
 * won and displays the leader board before a game begins. Additionally, it contains functions to check when 
 * a new high score has been achieved and update the leader board accordingly.
 * 
 * 
 * @author Lekha Reddy
 */
package edu.wm.cs.cs301.connectn;

import java.io.*;
import java.io.File;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ConnectNGame {
	private int rows;
	private int maxTurns;
	private int currBest;
	private int columns;
	private int toWin;
	private int lineNumber;
	private int nameLine;
	private String playerName;
	private String mode = " ";
	private int turns;
	private boolean want = true;
	private String again;
	
	public ConnectNGame() {		
		
	    while(want) {
	      do{
	    	  //ask for size of game board desired and set variables
		      Scanner myObj = new Scanner(System.in);  // Create a Scanner object
		      System.out.println("Chose Mode (S, M, or L):");

		      mode = myObj.nextLine();  // Read user input
		      System.out.println("whats your name:");
		      playerName = myObj.nextLine();  // Read user input

	      } while(!(mode.equalsIgnoreCase("S") | mode.equalsIgnoreCase("M") | mode.equalsIgnoreCase("L")));
	      if (mode.equalsIgnoreCase("S")){
			rows = 4;
			columns = 5;
			toWin = 3;
			maxTurns = 10;
		}
	      else if (mode.equalsIgnoreCase("M")){
			rows = 6;
			columns = 7;
			toWin = 4;
			maxTurns = 21;
		}
	      else if (mode.equalsIgnoreCase("L")){
			rows = 8;
			columns = 9;
			toWin = 5;
			maxTurns = 36;
		}
   
	      	//display leaderboard
		     File directory = new File("./resources/leaderboard.txt");
		     Scanner myReader = null;
			try {
				myReader = new Scanner(directory);
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		      while (myReader.hasNextLine()) {
		        String data = myReader.nextLine();
		        System.out.println(data);
		      }	
		turns =0;

		
	    GameBoard gameboard = new GameBoard(rows, columns, toWin, mode);
	    gameboard.displayBoard();
	    HumanPlayer humanPlayer = new HumanPlayer(gameboard);
	    ComputerPlayer computerPlayer = new ComputerPlayer(gameboard);
	    
	    while(!gameboard.isWinning()) {
		int humanCol = humanPlayer.takeTurn(gameboard);
		int humanRow = gameboard.drop(humanCol);
		gameboard.setSymbolAt(humanRow, humanCol, 'X');
		turns++;
	    gameboard.displayBoard();
	    if(gameboard.winner(gameboard)) {
	    	System.out.println("Congratulations! You won in " + turns + " moves!");
	    	if (turns < currentBestScore()) {
	    		updateLeader(turns, playerName);
	    	}
	    	break;
	    }
	    if (turns == maxTurns) {
	    	System.out.println("its a tie :/");
	    	break;
	    }
		int compCol = computerPlayer.takeTurn(gameboard);
		int compRow = gameboard.drop(compCol);
		gameboard.setSymbolAt(compRow, compCol, 'O');
	    gameboard.displayBoard();
	    if(gameboard.winner(gameboard)) {
	    	System.out.println("You lose :(");
	    	break;
	    }
	    } 
	    
	    
	    
	    // ask if they want to play again
	    do{
		      Scanner myObj2 = new Scanner(System.in);  // Create a Scanner object
		      System.out.println("Would you like to play again? (Y/N)?");

		      again = myObj2.nextLine();  // Read user input
	      } while(!(again.equalsIgnoreCase("Y") | again.equalsIgnoreCase("N")));
	    if (again.equalsIgnoreCase("Y")) {
	    	want = true;
	    }
	    if (again.equalsIgnoreCase("N")) {
		    want = false; 
	    }
	    
	}}
	

	
	//gets current best score from leaderboard to see if it needs updating
	public int currentBestScore() {
		if (mode.equalsIgnoreCase("S")) {
            lineNumber = 8; 
        }
        else if (mode.equalsIgnoreCase("M")) {
            lineNumber = 15; 
        }
        else if (mode.equalsIgnoreCase("L")) {
            lineNumber = 22; 
        }    
		try (BufferedReader reader = new BufferedReader(new FileReader("./resources/leaderboard.txt"))) {
        String line;
        int currentLine = 1;
        while ((line = reader.readLine()) != null) {
            if (currentLine == lineNumber) {
                if (line.isEmpty()) {
                    return 1000;
                }
                else {
                	currBest = Integer.valueOf(line);
                }
                break;
            }
            
            currentLine++;
        }
    } catch (IOException e) {
        e.printStackTrace();
    }
    return currBest;
    }
	
	
	//updates leaderboard
	public void updateLeader(int theirTurns, String theirName) {
		if (mode.equalsIgnoreCase("S")) {
            lineNumber = 8; 
        }
        else if (mode.equalsIgnoreCase("M")) {
            lineNumber = 15; 
        }
        else if (mode.equalsIgnoreCase("L")) {
            lineNumber = 22; 
        }    
		
		nameLine = lineNumber - 3;
				
        String newValue = String.valueOf(theirTurns); 

        // Read the file and store its content in memory
        StringBuilder content = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new FileReader("./resources/leaderboard.txt"))) {
            String line;
            int currentLine = 1;
            while ((line = reader.readLine()) != null) {
                if (currentLine == nameLine) {
                    // Modify the desired line
                    content.append(theirName).append("\n");
                }
                else if (currentLine == lineNumber) {
                    // Modify the desired line
                    content.append(newValue).append("\n");
                } 
                else {
                    // Keep the original line
                    content.append(line).append("\n");
                }
                currentLine++;
            }
        } catch (IOException e) {
            e.printStackTrace();
            return;
        }

        // Write the modified content back to the file
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("./resources/leaderboard.txt"))) {
            writer.write(content.toString());
        } catch (IOException e) {
            e.printStackTrace();
        }
	}
		
}
