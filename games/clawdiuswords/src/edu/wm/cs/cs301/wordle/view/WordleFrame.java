/**
  * The purpose of the WordleFrame class is to 
 * organize the layout of the game's interface.
 * It also provides methods to shut down the game,
 * reset the colors, repaint the grid, and get the grid.
 * 
 * @author Lekha Reddy
 */

package edu.wm.cs.cs301.wordle.view;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

import javax.swing.AbstractAction;
import javax.swing.ActionMap;
import javax.swing.BorderFactory;
import javax.swing.InputMap;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.KeyStroke;

import model.WordleModel;

public class WordleFrame {
	
	private final JFrame frame;
	
	private final KeyboardPanel keyboardPanel;
	
	private final WordleModel model;
	
	private final WordleGridPanel wordleGridPanel;
	

	public WordleFrame(WordleModel model) {
		this.model = model;
		this.keyboardPanel = new KeyboardPanel(this, model);
		int width = keyboardPanel.getPanel().getPreferredSize().width;
		this.wordleGridPanel = new WordleGridPanel(this, model, width);
		this.frame = createAndShowGUI();
	}
	
	
	private JFrame createAndShowGUI() {
		JFrame frame = new JFrame("Clawdius' Words");
		frame.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
		frame.setJMenuBar(createMenuBar());
		frame.setResizable(false);
		frame.addWindowListener(new WindowAdapter() {
			@Override
			 public void windowClosing(WindowEvent event) {
				shutdown();
			}
		});
		
		frame.add(createTitlePanel(), BorderLayout.NORTH);
		frame.add(wordleGridPanel, BorderLayout.CENTER);
		frame.add(keyboardPanel.getPanel(), BorderLayout.SOUTH);
		wordleGridPanel.setBackground(new Color(135, 206, 235));
		keyboardPanel.getPanel().setBackground(new Color(255, 234, 193));



		frame.pack();
		frame.setLocationByPlatform(true);
		frame.setVisible(true);
		
		System.out.println("Frame size: " + frame.getSize());
		
		return frame;
	}
	
	
	
	private JMenuBar createMenuBar() {
		JMenuBar menuBar = new JMenuBar();
		
		
		JMenuItem instructionsItem = new JMenuItem("How to Play");
		instructionsItem.addActionListener(event -> new InstructionsDialog(this));
		menuBar.add(instructionsItem);
		
//		String text = "Clawdius needs help after a rough day,"
//				+ "he was swimming College Creek and now can't"
//				+ "seem to remember his favorite words\n"
//				+"\n"
//				+ "You are able to guess Clawdius' words 6 times"
//				+ "Similar to the NYT's Wordle game, the letters"
//				+ "change color based on whether they are in the word"
//				+ "and the correct position\n"
//				+"\n"
//				+ "";
		
		
//		JMenu difficultyMenu = new JMenu("Difficulty");
//		menuBar.add(difficultyMenu);
//		
//		JMenuItem kidsItem = new JMenuItem("Kids");
//		ActionListener kidsAction = new ActionListener() {
//		    @Override
//		    public void actionPerformed(ActionEvent e) {
//		    	frame.dispose();
//				new WordleFrame(new WordleModel(3, 4));
//		    }
//		};
//		kidsItem.addActionListener(kidsAction);
//		difficultyMenu.add(kidsItem);
//		
//		JMenuItem normalItem = new JMenuItem("Normal");
//		ActionListener normalAction = new ActionListener() {
//		    @Override
//		    public void actionPerformed(ActionEvent e) {
//		    	frame.dispose();
//				new WordleFrame(new WordleModel(5, 6));
//		    }
//		};
//		normalItem.addActionListener(normalAction);
//		difficultyMenu.add(normalItem);
//		
//		JMenuItem hardItem = new JMenuItem("Hard");
//		ActionListener hardAction = new ActionListener() {
//		    @Override
//		    public void actionPerformed(ActionEvent e) {
//		    	frame.dispose();
//				new WordleFrame(new WordleModel(7, 8));
//		    }
//		};
//		
//		hardItem.addActionListener(hardAction);
//		difficultyMenu.add(hardItem);
					
		
		return menuBar;
	}
	
	
	
	private JPanel createTitlePanel() {
		JPanel panel = new JPanel(new FlowLayout());
		panel.setBorder(BorderFactory.createEmptyBorder(0, 5, 5, 5));
		
		InputMap inputMap = panel.getInputMap(JPanel.WHEN_IN_FOCUSED_WINDOW);
		inputMap.put(KeyStroke.getKeyStroke(KeyEvent.VK_ESCAPE, 0), "cancelAction");
		ActionMap actionMap = panel.getActionMap();
		actionMap.put("cancelAction", new CancelAction());
		
		JLabel label = new JLabel("Clawdius' Words!");
		label.setFont(AppFonts.getTitleFont());
		panel.add(label);
		
		return panel;
	}
	
	public void shutdown() {
//		model.getStatistics().writeStatistics();
		frame.dispose();
		System.exit(0);
	}
	
	public void resetDefaultColors() {
		keyboardPanel.resetDefaultColors();
	}
	
	public void setColor(String letter, Color backgroundColor, Color foregroundColor) {
		keyboardPanel.setColor(letter, backgroundColor, foregroundColor);
	}
	
	public void repaintWordleGridPanel() {
		wordleGridPanel.repaint();
	}

	public JFrame getFrame() {
		return frame;
	}
	
	private class CancelAction extends AbstractAction {

		private static final long serialVersionUID = 1L;

		@Override
		public void actionPerformed(ActionEvent event) {
			shutdown();
		}
		
	}

}
