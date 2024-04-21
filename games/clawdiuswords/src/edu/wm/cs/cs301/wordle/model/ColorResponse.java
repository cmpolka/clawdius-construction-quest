/**
 * The purpose of the ColorResponse class is to 
 * create a ColorResponse object and supply methods for
 * retrieving the background color and foreground color 
 * of a ColorResponse.
 * 
 * @author Lekha Reddy
 */

package edu.wm.cs.cs301.wordle.model;

import java.awt.Color;

public class ColorResponse {
	
	private final Color backgroundColor, foregroundColor;

	public ColorResponse(Color backgroundColor, Color foregroundColor) {
		this.backgroundColor = backgroundColor;
		this.foregroundColor = foregroundColor;
	}

	public Color getBackgroundColor() {
		return backgroundColor;
	}

	public Color getForegroundColor() {
		return foregroundColor;
	}

}
