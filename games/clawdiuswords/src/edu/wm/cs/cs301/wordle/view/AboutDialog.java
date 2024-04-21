/**
 * The purpose of the AboutDialog class is to 
 * create a dialog that will display information about
 * the wordle game to a user upon the click of 
 * the 'About...' button in the menu bar.
 * 
 * @author Lekha Reddy
 */

package edu.wm.cs.cs301.wordle.view;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.KeyEvent;

import javax.swing.AbstractAction;
import javax.swing.ActionMap;
import javax.swing.BorderFactory;
import javax.swing.InputMap;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.KeyStroke;

public class AboutDialog extends JDialog {
	
	private static final long serialVersionUID = 1L;
	
	private final CancelAction cancelAction;
		
	private final String results;
	
	private final WordleFrame view;
	
	private final int winOrLose;

	

	public AboutDialog(WordleFrame view, String result, int endResult) {
		super(view.getFrame(), "About", true);
		this.cancelAction = new CancelAction();
		this.winOrLose = endResult;
		this.results = result;
		this.view = view;
		
		add(createMainPanel(), BorderLayout.CENTER);
		add(createButtonPanel(), BorderLayout.SOUTH);
		
		pack();
		setLocationRelativeTo(view.getFrame());
		setVisible(true);
		getResult();
	}
	
	private JPanel createMainPanel() {
		JPanel panel = new JPanel(new GridBagLayout());
		panel.setBorder(BorderFactory.createEmptyBorder(0, 5, 5, 5));
		Font titleFont = AppFonts.getTitleFont();
		Font textFont = AppFonts.getTextFont();
		
		GridBagConstraints gbc = new GridBagConstraints();
		gbc.anchor = GridBagConstraints.CENTER;
		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.insets = new Insets(0, 5, 5, 30);
		
		gbc.gridwidth = 2;
		gbc.gridx = 0;
		gbc.gridy = 0;
		JLabel label = new JLabel("Game Results");
		label.setFont(titleFont);
		label.setHorizontalAlignment(JLabel.CENTER);
		Color backgroundColor = label.getBackground();
		panel.add(label, gbc);
		
		gbc.gridy++;

		String text = results;
		JTextArea textArea = new JTextArea(4, 25);
		textArea.setBackground(backgroundColor);
		textArea.setEditable(false);
		textArea.setFont(textFont);
		textArea.setText(text);
		textArea.setLineWrap(true);

		textArea.setWrapStyleWord(true);
		panel.add(textArea, gbc);
		
		return panel;
	}
	
	private JPanel createButtonPanel() {
		JPanel panel = new JPanel(new FlowLayout());
		panel.setBorder(BorderFactory.createEmptyBorder(0, 5, 5, 5));
		
		InputMap inputMap = panel.getInputMap(JPanel.WHEN_IN_FOCUSED_WINDOW);
		inputMap.put(KeyStroke.getKeyStroke(KeyEvent.VK_ESCAPE, 0), "cancelAction");
		ActionMap actionMap = panel.getActionMap();
		actionMap.put("cancelAction", cancelAction);
		
		JButton button = new JButton("Go back to map");
		button.addActionListener(cancelAction);
		panel.add(button);
		
		return panel;
	}
	
	private class CancelAction extends AbstractAction {

		private static final long serialVersionUID = 1L;

		@Override
		public void actionPerformed(ActionEvent event) {
			dispose();
			view.shutdown();
		}
		
	}
	
	public int getResult() {
		//0 is lose, 1 is win
		return winOrLose;
	}

}
