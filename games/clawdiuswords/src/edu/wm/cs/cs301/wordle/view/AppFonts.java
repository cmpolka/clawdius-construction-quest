/**
 * The purpose of the AppFonts class is to 
 * provide fonts that will be used on text in 
 * the game
 * 
 * @author Lekha Reddy
 */

package edu.wm.cs.cs301.wordle.view;

import java.awt.Font;

public class AppFonts {
	
	public static Font getTitleFont() {
		return new Font("Dialog", Font.BOLD, 36);
	}
	
	public static Font getTextFont() {
		return new Font("Dialog", Font.PLAIN, 16);
	}
	
	public static Font getFooterFont() {
		return new Font("Dialog", Font.PLAIN, 12);
	}

}