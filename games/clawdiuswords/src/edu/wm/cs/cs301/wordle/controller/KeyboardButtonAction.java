/**
 * The purpose of the KeyboardButtonAction class is to 
 * add functionality to the keys/buttons selected by the 
 * user on the KeyboardPanel
 * 
 * @author Lekha Reddy
 */

package edu.wm.cs.cs301.wordle.controller;

import java.awt.event.ActionEvent;

import javax.swing.AbstractAction;
import javax.swing.JButton;

import wordle.model.AppColors;
import wordle.model.WordleModel;
import wordle.model.WordleResponse;
import view.AboutDialog;
import view.WordleFrame;

public class KeyboardButtonAction extends AbstractAction {

	private static final long serialVersionUID = 1L;
	
	private final WordleFrame view;
	
	private final WordleModel model;
	

	public KeyboardButtonAction(WordleFrame view, WordleModel model) {
		this.view = view;
		this.model = model;
	}

	
	@Override
	public void actionPerformed(ActionEvent event) {
		JButton button = (JButton) event.getSource();
		String text = button.getActionCommand();
		switch (text) {
		case "Enter":
			if (model.getCurrentColumn() >= (model.getColumnCount() - 1)) {
				boolean moreRows = model.setCurrentRow();
				WordleResponse[] currentRow = model.getCurrentRow();
				int greenCount = 0;
				for (WordleResponse wordleResponse : currentRow) {
					view.setColor(Character.toString(wordleResponse.getChar()),
							wordleResponse.getBackgroundColor(), 
							wordleResponse.getForegroundColor());
					if (wordleResponse.getBackgroundColor().equals(AppColors.GREEN)) {
						greenCount++;
					} 
				}
				
				if (greenCount >= model.getColumnCount()) {
					view.repaintWordleGridPanel();
					new AboutDialog(view, "nice win!", 1);
				} else if (!moreRows) {
					view.repaintWordleGridPanel();
					new AboutDialog(view, "better luck next time", 0);
				} else {
					view.repaintWordleGridPanel();
				}
			}
			break;
		case "Backspace":
			model.backspace();
			view.repaintWordleGridPanel();
			break;
		case "Hint":
			WordleResponse[] currentRow = model.getCurrentRow();
			int colToReplace = 0;
			for (WordleResponse wordleResponse : currentRow) {
				//find gray letter
				if (wordleResponse.getBackgroundColor().equals(AppColors.GRAY)) {
					String rightWord = model.getCurrentWord();
					char rightLetter = rightWord.charAt(colToReplace);
					//replace current letter with correct letter
					currentRow[colToReplace] = new WordleResponse(rightLetter, AppColors.GREEN, AppColors.WHITE);
					view.repaintWordleGridPanel();
					//adjust keyboard so the inserted correct letter's key is green
					view.setColor(Character.toString(currentRow[colToReplace].getChar()),
							currentRow[colToReplace].getBackgroundColor(), 
							currentRow[colToReplace].getForegroundColor());
					break;
				}
				else {
					colToReplace++;
				}

				}
			//check if hint replacement has won the game
			int greenCount = 0;
			for (WordleResponse wordleResponse : currentRow) {
				if (wordleResponse.getBackgroundColor().equals(AppColors.GREEN)) {
					greenCount++;
				}
			}
			if (greenCount >= model.getColumnCount()) {
				new AboutDialog(view, "nice win!", 1);
			}
			break;
		default:
			model.setCurrentColumn(text.charAt(0));
			view.repaintWordleGridPanel();
			break;
		}
		
	}

}
