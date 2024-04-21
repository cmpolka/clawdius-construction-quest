/**
 * The purpose of the Wordle class is to being a Wordle
 * game with the default dimensions of 5 columns
 * and 6 rows
 * 
 * @author Lekha Reddy
 */

package edu.wm.cs.cs301.wordle;

import javax.swing.SwingUtilities;
import javax.swing.UIManager;

import edu.wm.cs.cs301.wordle.model.WordleModel;
import edu.wm.cs.cs301.wordle.view.WordleFrame;

// import view.WordleFrame;
// import games.clawdiuswords.src.edu.wm.cs.cs301.wordle.view.WordleFrame.java;

public class Wordle implements Runnable {
	
	public static void main(String[] args) {
		SwingUtilities.invokeLater(new Wordle());
		
		//Can't use the Cross-Platform Look and Feel on Windows - Needs investigation
		if (!System.getProperty("os.name").contains("Windows")) {
			//Must use cross-platform look and feel so button backgrounds work on Mac
			try {
			    UIManager.setLookAndFeel( UIManager.getCrossPlatformLookAndFeelClassName() );
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	}

	@Override
	public void run() {
		new WordleFrame(new WordleModel(5, 6));
	}

}
