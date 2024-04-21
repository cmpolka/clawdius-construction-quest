/**
 * The purpose of the ComputerPlayer class is to return a column number that the 
 * computer player has chosen to drop a token into for its turn. This choice is based on an algorithm
 * that first checks whether the computer player can make a winning move, then it checks if the computer player 
 * can block a winning move of the human player, and if no winning moves are present then it chooses randomly.
 * 
 * @author Lekha Reddy
 * 
 */
package edu.wm.cs.cs301.connectn;
import java.util.Random;

public class ComputerPlayer implements Player {
	private boolean could = false;
	private int oneLess;
	private int colForWin;
	private int thisCol;
	private int same;
	GameBoard gameBoard;

    
	public ComputerPlayer(GameBoard board) {
		gameBoard = board;
		board.getBoard();
		oneLess = board.almostNumber(board);
	}

	//checks whether the computer player can make a winning move, then it checks if the computer player 
	//can block a winning move of the human player, and if no winning moves are present then it chooses randomly and
	//returns the integer choice of colummn
	@Override
	public int takeTurn(GameBoard board) {
		if (couldWinAcross(board, oneLess, 'O')|| couldWinDown(board, oneLess, 'O') || couldWinLDiag(board, oneLess, 'O') || couldWinRDiag(board, oneLess, 'O')) {
			System.out.println(colForWin);
			return colForWin;
		}
		else if((couldWinAcross(board, oneLess, 'X')|| couldWinDown(board, oneLess, 'X') || couldWinLDiag(board, oneLess, 'X') || couldWinRDiag(board, oneLess, 'X'))) {
			System.out.println(colForWin);
			return colForWin;
		}
		else{
//		System.out.println("randomly choosing");
	    Random random = new Random();
	    do {
	    	thisCol = random.nextInt(board.getCols());
	    }
	    while(board.columnFull(thisCol));
	    }
	    return thisCol;
		}
	

	//checks if theres a possible across win
	public boolean couldWinAcross(GameBoard board , int oneLess, Character symbol) {
		for(int i = 0 ; i < board.getRows() ;i++) {
			for (int j=0 ; j < board.getCols()- (oneLess); j++) {
				int spaceCount = 0;
				int oCount = 0;
				for (int k = 0 ; k <= oneLess ; k++) {
					if (board.whichSymbol(i, j+k)==(' ')) {
						spaceCount++;
						if (spaceCount > 1) {
							break;
						}
						colForWin = j+k;
					}
					else if (board.whichSymbol(i, j+k)==(symbol)){
						oCount++;
					}
				}
				if(spaceCount == 1 && oCount == oneLess){
					System.out.println("Could Win Across");
					return true;
				}
			}
		}
		return false;}
	
	//checks if there's a potential down win
	public boolean couldWinDown(GameBoard board, int oneLess, Character symbol) {
		for(int i =0 ; i < board.getCols() ; i++) {
			for (int j = board.getRows() - 1 ; j > (oneLess-1); j--) {
				for (int k=0; k<oneLess;k++) {
					same =1;
//					System.out.println("in a row: "+ same + " at col " + i);
					if(board.whichSymbol(j-k, i) == symbol) {
						same++;
//						System.out.println("ins a row: "+ same + " at col " + i);
						if (same == oneLess) {
							if (board.whichSymbol(j-k-1, i) == ' ') {
								colForWin = i;
								could =true;
								System.out.println("Could Win Down");
								return could;
							}
					}}
					else {
						could = false;
						same = 0;
					}
					
				}
			}
		}
		return could;
	}
	
	//checks if there's a potential diagonal left win
	public boolean couldWinLDiag(GameBoard board, int oneLess, Character symbol) {
		for (int i= 0 ; i<board.getRows() ; i++) {
			for (int j = 0 ; j< board.getCols() ; j++) {
				int spaceCount = 0;
				int oCount = 0;
				for (int k = 0 ; k<= oneLess ; k++) {
				if((i + k < board.getRows()) && (j+k < board.getCols())){
					if (board.whichSymbol(i+k, j+k) == (' ')) {
						spaceCount++;
						if (spaceCount > 1) {
							break;
						}
						colForWin = j+k;
					}
					if (board.whichSymbol(i+k, j+k) == (symbol)) {
						oCount++;
					}
				}
					if (spaceCount == 1 && oCount == oneLess) {
						System.out.println("could win l diagonally");
						return true;
					}
				}
			}
		}
		return false;
	}
	

	//checks if there's a potential diagonal right win
	public boolean couldWinRDiag(GameBoard board, int oneLess, Character symbol) {
		for (int i= 0 ; i<board.getRows() ; i++) {
			for (int j = 0 ; j< board.getCols() ; j++) {
				int spaceCount = 0;
				int oCount = 0;
				for (int k = 0 ; k<= oneLess ; k++) {
				if((i + k < board.getRows()) && (j-k >= 0)){
					if (board.whichSymbol(i+k, j-k) == (' ')) {
						spaceCount++;
						if (spaceCount > 1) {
							break;
						}
						colForWin = j-k;
					}
					if (board.whichSymbol(i+k, j-k) == (symbol)) {
						oCount++;
					}
				}
					if (spaceCount == 1 && oCount == oneLess) {
						System.out.println("could win diagonally");
						return true;
					}
				}
			}
		}
		return false;
	}
}






