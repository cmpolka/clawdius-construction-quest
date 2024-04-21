/**
 * The purpose of the HumanPlayer class is to ask the user which column they would like to place a token in,
 * check whether they entered a valid value, and return the column number that they chose.
 * 
 *@author Lekha Reddy
 */
package edu.wm.cs.cs301.connectn;

import java.util.Scanner;

public class HumanPlayer implements Player {
	GameBoard gameBoard;
	private String choice;
	private int place;
	private int whichRow;
	private boolean number;
	private boolean valid = true;
	private int turnCounter;
	
	public HumanPlayer(GameBoard board) {
		gameBoard = board;
		board.getBoard();
	}

	@Override
	public int takeTurn(GameBoard board) {
			return promptUser(board);

		   }


//ask user which column they'd like to drop a token in and return that integer
public int promptUser(GameBoard board) {
	Scanner myObj = new Scanner(System.in);  // Create a Scanner object
do{
	System.out.println("Choose a slot (1 - " + board.getCols() + ") to place your piece or QUIT to quit the game:");
     choice = myObj.nextLine();  // Read user input
		 if (choice.equals("QUIT")) {
			 System.exit(0);
		 }
}while ( !(isInteger(choice)) || (Integer.valueOf(choice)) > board.getCols() || (Integer.valueOf(choice)) < 1|| board.columnFull(Integer.valueOf(choice) - 1) );
place = Integer.valueOf(choice) - 1 ;
	return place;
//	}
}


//check whether a string that the user entered in an integer
public boolean isInteger( String input ) {
    try {
        Integer.parseInt( input );
        return true;
    }
    catch( Exception e ) {
    	return false;
    }

}



}
