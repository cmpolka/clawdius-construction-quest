/**
 * The purpose of the GameBoard class is to dictate how a GameBoard should be composed of 
 * a chosen number of location objects. Additionally, It contains methods to update the token at a certain 
 * cell in the board, return which symbol is at a certain cell, return which row a dropped
 * token should land at, display the gameboard to the user, gets the number of rows and columns in the
 * board, and checks if there is a winning pattern present in the board.
 * 
 * @author Lekha Reddy
 */
package edu.wm.cs.cs301.connectn;

import java.util.Scanner;

public class GameBoard {
	private Location[][] board;			//do not change!
	private boolean first = true;
	private String answer;
	private int needToWin;
	private int place;
	private boolean win = false;
	private String gamemode;
	private int totalTurns = 1;
	private int helper;
	private int almostWin;
	
	//creates a gameboard with the correct number of rows and columns. Stores the number of tokens
	//that need to be in a row to win the game and the game mode into variables.
	public GameBoard(int row, int col, int needed, String mode) {
		board = new Location[row][col];
		needToWin = needed;
		gamemode = mode;
		almostWin = needed - 1 ;
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				board[i][j] = new Location();
			}
		}
	}
	
	//returns one less than the number that a player needs to win a certain board.
	public int almostNumber(GameBoard board) {
		return almostWin;
	}
	
	//checks whether a column in the board has an empty space left
	public boolean columnFull(int col) {
		for (int i = board.length-1 ; i >= 0 ; i--) {
//			System.out.println("i is" + i);
			if(board[i][col].getToken() == ' ') {
				return false;}
		}
		return true;
	}
	
	//changes the symbol of a certain location
    public void setSymbolAt(int row, int column, char symbol) {
        board[row][column].setSymbol(symbol);
    }
    
    public Location[][] getBoard() {
        return board;
    }
    
    //returns the symbol present at a certain location
    public Character whichSymbol(int row, int col) {
    	return board[row][col].getToken();
    }
    
    //returns the row that a dropped token will land at
    public int drop(int col) {
    	int current = board.length-1;
    	while (!(board[current][col].isEmpty())) {
    		current--;
    	}	
    	return current;
    }
    
    //displays the game board to the user
	public void displayBoard() {
		if(!first) {
		}
		//take column number and symbol as input 
		System.out.println("Turn: " + totalTurns);
        // Print the board row by row
    	if (gamemode.equalsIgnoreCase("S")) {
    		System.out.println("   1   2   3   4   5  ");
    		System.out.println(" =====================");}
    	else if (gamemode.equalsIgnoreCase("M")) {
    		System.out.println("   1   2   3   4   5   6   7  ");
    		System.out.println(" =============================");}
    	else if (gamemode.equalsIgnoreCase("L")) {
    		System.out.println("   1   2   3   4   5   6   7   8   9  ");
    		System.out.println(" =====================================");}
        for (int i = 0; i < board.length; i++) {
            System.out.print("|| ");
            // Print each row
            for (int j = 0; j < board[0].length; j++) {
                Character token = board[i][j].getToken();
                // Print the token or an empty space if the location is empty
                if (token == null) {
                	System.out.print(" ");
                }
                else if (token != null) {
                	System.out.print(token);
                }
                // Print a separator between columns
                if (j < board[0].length-1) {
                    System.out.print(" | ");
                }
            }
            System.out.print(" ||");
            // Move to the next row
            System.out.println();
            // Print a separator between rows
           if (i<board.length-1) {
      	   if (gamemode.equalsIgnoreCase("S")) {
    			System.out.println(" ---------------------");
    			}  	
      	   else if (gamemode.equalsIgnoreCase("M")) {
    			System.out.println(" -----------------------------");
    			}  	
      	   else if (gamemode.equalsIgnoreCase("L")) {
    			System.out.println(" -------------------------------------");
    			}  	
           };

           
        }
 	   if (gamemode.equalsIgnoreCase("S")) {
 			System.out.println(" =====================");
 			}  	  
 	   else if (gamemode.equalsIgnoreCase("M")) {
 				System.out.println(" =============================");
 			}  
 	   else if (gamemode.equalsIgnoreCase("L")) {
		System.out.println(" =====================================");
		}   
       System.out.println();
		System.out.println("you need " + needToWin + " in a row to win");
	       System.out.println();


		helper++;
		if (helper % 2 == 0) {
			totalTurns++;
		}
		
}

	public int getRows() {
		return board.length;
	}
	
	public int getCols() {
		return board[0].length;
	}
	
	//returns whether the game board has been won
	public boolean isWinning() {
		return win;
	}
	
	//returns whether the game board contains a winning pattern in any direction
	public boolean winner(GameBoard board) {
		if (winAcross(board, needToWin) || winDown(board, needToWin) || winLDiag(board, needToWin) || winRDiag(board, needToWin)) {
			return true;
		}
		return false;
	}
	
	//checks if there is a horizontal winning pattern
	public boolean winAcross(GameBoard board , int toWin) {
		for(int i = 0 ; i < board.getRows() ;i++) {
			for (int j=0 ; j < board.getCols()- (toWin -1); j++) {
				boolean found = true;
				for (int k = 1 ; k < toWin ; k++) {
					if (board.whichSymbol(i, j) == ' ' || board.whichSymbol(i, j+k) == ' ' || board.whichSymbol(i, j) != board.whichSymbol(i, j+k)) {
						found = false;
						break;
					}
				}
				if (found) {
					win = true;
					return true;
				}		
		}
			}
		return false;}
	
	//checks if there is a vertical winning pattern
	public boolean winDown(GameBoard board , int toWin) {
		for(int i = 0 ; i < board.getCols() ;i++) {
			for (int j=0 ; j < board.getRows()-(toWin-1); j++) {
				boolean found = true;
				for (int k = 1 ; k < toWin ; k++) {
					if (board.whichSymbol(j, i) == ' ' || board.whichSymbol(j+k, i) == ' ' || board.whichSymbol(j, i) != board.whichSymbol(j+k, i)) {
						found = false;
						break;
					}
				}
				if (found) {
					win = true;
					return true;
				}		
		}
			}
		return false;}
	
	//checks if there is a Diagonal win left
	public boolean winLDiag(GameBoard board , int toWin) {
	    for (int i = 0; i < board.getCols(); i++) {
	        for (int j = 0; j < board.getRows() - (toWin - 1); j++) {
	            boolean found = true;
	            for (int k = 1; k < toWin; k++) {
	                // Check if indices are within bounds
	                if (i + k >= board.getCols() || j + k >= board.getRows() || board.whichSymbol(j, i) == ' ' || board.whichSymbol(j + k, i + k) == ' ' || board.whichSymbol(j, i) != board.whichSymbol(j + k, i + k)) {
	                    found = false;
	                    break;
	                }
	            }
	            if (found) {
	                win = true;
	                return true;
	            }
	        }
	    }
	    return false;
	
	}

	
	//checks if there is Diagonal win right 
	public boolean winRDiag(GameBoard board, int toWin) {
	    for (int i = 0; i < board.getCols(); i++) {
	        for (int j = 0; j < board.getRows() - (toWin - 1); j++) {
	            boolean found = true;
	            for (int k = 1; k < toWin; k++) {
	                // Check if indices are within bounds
	                if (i - k < 0 || j + k >= board.getRows() || board.whichSymbol(j, i) == ' ' || board.whichSymbol(j + k, i - k) == ' ' || board.whichSymbol(j, i) != board.whichSymbol(j + k, i - k)) {
	                    found = false;
	                    break;
	                }
	            }
	            if (found) {
	                win = true;
	                return true;
	            }
	        }
	    }
	    return false;
	}
	
	

//	
	}

