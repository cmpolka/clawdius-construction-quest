/**
 * The purpose of Player interface is to provide the takeTurn method that is
 * implemented by the ComputerPlayer and HumanPlayer classes
 * 
 * @author Lekha Reddy 
 */
package edu.wm.cs.cs301.connectn;

public interface Player {
	public int takeTurn(GameBoard board);

	
}
