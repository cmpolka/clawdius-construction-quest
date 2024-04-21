/**
 * The purpose of the WordleResponse class is to 
 * create the WordleResponse object that will compose
 * the 2d array of the wordle grid. It also provides methods
 * get information about a WordleResponse object such as 
 * the character, the background color, and the foreground color.
 * 
 * @author Lekha Reddy
 */

package edu.wm.cs.cs301.wordle.model;

import java.awt.Color;

public class WordleResponse {
	
	private final char c;
	
	private final ColorResponse colorResponse;

	public WordleResponse(char c, Color backgroundColor, Color foregroundColor) {
		this.c = c;
		this.colorResponse = new ColorResponse(backgroundColor, foregroundColor);
	}
	
	public char getChar() {
		return c;
	}

	public Color getBackgroundColor() {
		return colorResponse.getBackgroundColor();
	}

	public Color getForegroundColor() {
		return colorResponse.getForegroundColor();
	}
	
}
