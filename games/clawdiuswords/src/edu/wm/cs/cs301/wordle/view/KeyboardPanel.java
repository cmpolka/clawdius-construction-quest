/**
 * The purpose of the KeyboardPanel class is to 
 * organize the layout of the keyboard section of the frame.
 * 
 * @author Lekha Reddy
 */

package edu.wm.cs.cs301.wordle.view;

import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.Image;
import java.awt.event.KeyEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;


import javax.swing.ActionMap;
import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.InputMap;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.KeyStroke;

import controller.KeyboardButtonAction;
import model.AppColors;
import model.WordleModel;
import model.WordleResponse;

public class KeyboardPanel {

	private int buttonIndex, buttonCount;

	private final JButton[] buttons;
	

	private final JPanel panel;

	private final KeyboardButtonAction action;

	private final WordleModel model;

	public KeyboardPanel(WordleFrame view, WordleModel model) {
		this.model = model;
		this.buttonIndex = 0;
		this.buttonCount = firstRow().length + secondRow().length
				+ thirdRow().length + 1;
		this.buttons = new JButton[buttonCount];
		this.action = new KeyboardButtonAction(view, model);
		this.panel = createMainPanel();
	}

	private JPanel createMainPanel() {
		JPanel panel = new JPanel(new GridLayout(0, 1, 0, 0));
		panel.setBorder(BorderFactory.createEmptyBorder(10, 5, 0, 5));

		panel.add(createHintPanel());
		panel.add(createQPanel());
		panel.add(createAPanel());
		panel.add(createZPanel());
		panel.add(createTotalPanel());
		

		return panel;
	}
	
	private JPanel createHintPanel() {
		JPanel panel = new JPanel(new FlowLayout());
		panel.setBorder(BorderFactory.createEmptyBorder(0, 5, 0, 5));
//		Font textfont = AppFonts.getTextFont();

		
	    ImageIcon icon = new ImageIcon("resources/clawdius_red.png");
	    Image scaledImage = icon.getImage().getScaledInstance(20, 20, Image.SCALE_SMOOTH);
	    ImageIcon scaledIcon = new ImageIcon(scaledImage);
	    

		JButton button = new JButton(scaledIcon);
	    button.setBorder(null); // Remove border
	    button.setContentAreaFilled(false);
//	    button.setIcon(scaledIcon);


		button.setEnabled(false);
		button.addActionListener(action);
//		button.setFont(textfont);
		buttons[0] = button;
		buttonIndex++;
//		panel.add(button);
        JLabel label = new JLabel(scaledIcon);

        label.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
//                JOptionPane.showMessageDialog(null, "Yay you clicked me!");
            	System.out.println("Yay you clicked me!");
            }

        });
        panel.add(label);
        
        


        		

		
	    panel.setBackground(new Color(255, 234, 193));

		return panel;
	}


	
	private JPanel createQPanel() {
		JPanel panel = new JPanel(new FlowLayout());
		panel.setBorder(BorderFactory.createEmptyBorder(0, 5, 0, 5));
		Font textfont = AppFonts.getTextFont();

		String[] letters = firstRow();

		for (int index = 0; index < letters.length; index++) {
			JButton button = new JButton(letters[index]);
			setKeyBinding(button, letters[index]);
			button.addActionListener(action);
			button.setFont(textfont);
			buttons[buttonIndex++] = button;
			panel.add(button);
		}

	    panel.setBackground(new Color(255, 234, 193));
		
		return panel;
	}

	private String[] firstRow() {
		String[] letters = { "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
				"Backspace" };
		return letters;
	}

	private JPanel createAPanel() {
		JPanel panel = new JPanel(new FlowLayout());
		panel.setBorder(BorderFactory.createEmptyBorder(0, 5, 0, 5));
		Font textfont = AppFonts.getTextFont();

		String[] letters = secondRow();

		for (int index = 0; index < letters.length; index++) {
			JButton button = new JButton(letters[index]);
			setKeyBinding(button, letters[index]);
			button.addActionListener(action);
			button.setFont(textfont);
			buttons[buttonIndex++] = button;
			panel.add(button);
		}
	    panel.setBackground(new Color(255, 234, 193));

		return panel;
	}

	private String[] secondRow() {
		String[] letters = { "A", "S", "D", "F", "G", "H", "J", "K", "L",
				"Enter" };
		return letters;
	}

	private JPanel createZPanel() {
		JPanel panel = new JPanel(new FlowLayout());
		panel.setBorder(BorderFactory.createEmptyBorder(0, 5, 0, 5));
		Font textfont = AppFonts.getTextFont();

		String[] letters = thirdRow();

		for (int index = 0; index < letters.length; index++) {
			JButton button = new JButton(letters[index]);
			setKeyBinding(button, letters[index]);
			button.addActionListener(action);
			button.setFont(textfont);
			buttons[buttonIndex++] = button;
			panel.add(button);
		}
	    panel.setBackground(new Color(255, 234, 193));


		return panel;
	}

	private String[] thirdRow() {
		String[] letters = { "Z", "X", "C", "V", "B", "N", "M" };
		return letters;
	}

	private void setKeyBinding(JButton button, String text) {
		InputMap inputMap = button.getInputMap(JButton.WHEN_IN_FOCUSED_WINDOW);
		if (text.equalsIgnoreCase("Backspace")) {
			inputMap.put(KeyStroke.getKeyStroke(KeyEvent.VK_BACK_SPACE, 0),
					"action");
		} else {
			inputMap.put(KeyStroke.getKeyStroke(text.toUpperCase()), "action");
		}
		ActionMap actionMap = button.getActionMap();
		actionMap.put("action", action);
	}

	private JPanel createTotalPanel() {
		JPanel panel = new JPanel(new FlowLayout());
		panel.setBorder(BorderFactory.createEmptyBorder(0, 5, 0, 5));
		Font footerFont = AppFonts.getFooterFont();

		String text = String.format("%,d", model.getTotalWordCount());
		text += " possible " + model.getColumnCount() + "-letter words!";
		JLabel label = new JLabel(text);
		label.setFont(footerFont);
		panel.add(label);
	    panel.setBackground(new Color(255, 234, 193));


		return panel;
	}

	public void setColor(String letter, Color backgroundColor,
			Color foregroundColor) {
		for (JButton button : buttons) {
			//check if hint should be enables
			buttons[0].setEnabled(grayChecking()); 
			if (button.getActionCommand().equals(letter)) {
				Color color = button.getBackground();
				if (color.equals(AppColors.GREEN)) {
					// Do nothing
				} else if (color.equals(AppColors.YELLOW)
						&& backgroundColor.equals(AppColors.GREEN)) {
					button.setBackground(backgroundColor);
					button.setForeground(foregroundColor);
				} else {
					button.setBackground(backgroundColor);
					button.setForeground(foregroundColor);
				}
				break;
			}
		}
	}
	
	//use this to check if conditions that disable hint are present
	public boolean grayChecking() {
		int grayCount = 0;
		WordleResponse[] currentRow = model.getCurrentRow();
		for (WordleResponse wordleResponse : currentRow) {
			if (wordleResponse.getBackgroundColor().equals(AppColors.GRAY)) {
				grayCount++;
			}
		}
		if(grayCount == 0) {
			return false;
		}
		return true;
	}

	public void resetDefaultColors() {
		for (JButton button : buttons) {
			button.setBackground(null);
			button.setForeground(null);
		}
	}

	public JPanel getPanel() {
		return panel;
	}

}
