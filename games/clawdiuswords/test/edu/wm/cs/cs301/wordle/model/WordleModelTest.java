/**
 * The purpose of the WordleModelTest class is to 
 * access the functionality of the WordleModel class
 * 
 * @author Lekha Reddy
 */

package edu.wm.cs.cs301.wordle.model;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;


class WordleModelTest {

	private WordleModel model;
	private String word;
	
	//setup for testing kids mode
	@Test
	private void setUpKids(){
		this.model = new WordleModel(3, 4);
		this.word = model.getCurrentWord();
	}
	
	//setup for testing normal mode
	@Test
	private void setUpNormal(){
		this.model = new WordleModel(5, 6);
		this.word = model.getCurrentWord();
	}
	
	//setup for testing hard mode
	@Test
	private void setUpHard(){
		this.model = new WordleModel(7, 8);
		this.word = model.getCurrentWord();
	}
	

	//tests if generateCurrentWord() selects a current word from the word list
	@Test
	void generateCurWordTestKids() {
		setUpKids();
		assertTrue(model.getTotalWordCount()>10);
		assertNotNull(word);
	}
	
	@Test
	void generateCurWordTestNorm() {
		setUpNormal();
		assertTrue(model.getTotalWordCount()>10);
		assertNotNull(word);
	}
	
	@Test
	void generateCurWordTestHard() {
		setUpHard();
		assertTrue(model.getTotalWordCount()>10);
		assertNotNull(word);
	}
	
	
	//tests if getCurrentWord() returns the current word after it has been generated
	@Test
	void getCurWordTestKids() {
		setUpKids();
		assertTrue(word.length() > 0);
	}
	
	@Test
	void getCurWordTestNorm() {
		setUpNormal();
		assertTrue(word.length() > 0);
	}
	
	@Test
	void getCurWordTestHard() {
		setUpHard();
		assertTrue(word.length() > 0);
	}
	

	//tests if setCurrentColumn() updates the current column number
	@Test
	void setCurColNumTestKids() {
		setUpKids();
		int first = model.getCurrentColumn();
		model.setCurrentColumn('a');
		int second = model.getCurrentColumn();
		assertTrue(first<second);
	}
	
	@Test
	void setCurColNumTestNorma() {
		setUpNormal();
		int first = model.getCurrentColumn();
		model.setCurrentColumn('a');
		int second = model.getCurrentColumn();
		assertTrue(first<second);
	}
	
	@Test
	void setCurColNumTestHard() {
		setUpHard();
		int first = model.getCurrentColumn();
		model.setCurrentColumn('a');
		int second = model.getCurrentColumn();
		assertTrue(first<second);
	}
	
	//tests if setCurrentColumn() creates a WordleResponse object with a given char at the correct location on the grid
	@Test
	void setCurColCharTestKids() {
		setUpKids();
		model.setCurrentColumn('a');
		int col = model.getCurrentColumn();
		WordleResponse[][] row = model.getWordleGrid();
		assertEquals('a', row[model.getCurrentRowNumber()+1][col].getChar());
	}
	
	@Test
	void setCurColCharTestNormal() {
		setUpNormal();
		model.setCurrentColumn('a');
		int col = model.getCurrentColumn();
		WordleResponse[][] row = model.getWordleGrid();
		assertEquals('a', row[model.getCurrentRowNumber()+1][col].getChar());
	}
	
	@Test
	void setCurColCharTestHard() {
		setUpHard();
		model.setCurrentColumn('a');
		int col = model.getCurrentColumn();
		WordleResponse[][] row = model.getWordleGrid();
		assertEquals('a', row[model.getCurrentRowNumber()+1][col].getChar());
	}
	
	//tests if backspace() decreases the column number
	@Test
	void backspaceTestKids() {
		setUpKids();
		model.setCurrentColumn('a');
		int first = model.getCurrentColumn();
		model.backspace();
		int second = model.getCurrentColumn();
		assertTrue(first>second);
	}
	
	@Test
	void backspaceTestNorm() {
		setUpNormal();
		model.setCurrentColumn('a');
		int first = model.getCurrentColumn();
		model.backspace();
		int second = model.getCurrentColumn();
		assertTrue(first>second);
	}
	
	@Test
	void backspaceTestHard() {
		setUpHard();
		model.setCurrentColumn('a');
		int first = model.getCurrentColumn();
		model.backspace();
		int second = model.getCurrentColumn();
		assertTrue(first>second);
	}
	
	//tests if backspace() changes a cell on the grid from a WordleResponse to null
	@Test
	void backspaceNullTestKids() {
		setUpKids();
		model.setCurrentColumn('a');
		WordleResponse[][] row = model.getWordleGrid();
		int first = model.getCurrentColumn();
		assertTrue(row[model.getCurrentRowNumber()+1][first] != null);
		model.backspace();
		assertEquals(row[model.getCurrentRowNumber()+1][first], null);
	}
	
	@Test
	void backspaceNullTestNormal() {
		setUpNormal();
		model.setCurrentColumn('a');
		WordleResponse[][] row = model.getWordleGrid();
		int first = model.getCurrentColumn();
		assertTrue(row[model.getCurrentRowNumber()+1][first] != null);
		model.backspace();
		assertEquals(row[model.getCurrentRowNumber()+1][first], null);
	}
	
	@Test
	void backspaceNullTestHard() {
		setUpHard();
		model.setCurrentColumn('a');
		WordleResponse[][] row = model.getWordleGrid();
		int first = model.getCurrentColumn();
		assertTrue(row[model.getCurrentRowNumber()+1][first] != null);
		model.backspace();
		assertEquals(row[model.getCurrentRowNumber()+1][first], null);
	}
	
	//tests if backspace() only works when it is not called at the leftmost column
	@Test
	void backspaceOnFirstTestKids() {
		setUpKids();
		int first = model.getCurrentColumn();
		model.backspace();
		int second = model.getCurrentColumn();
		assertEquals(first, second);
	}
	
	@Test
	void backspaceOnFirstTestNorm() {
		setUpNormal();
		int first = model.getCurrentColumn();
		model.backspace();
		int second = model.getCurrentColumn();
		assertEquals(first, second);
	}
	
	@Test
	void backspaceOnFirstTestHard() {
		setUpHard();
		int first = model.getCurrentColumn();
		model.backspace();
		int second = model.getCurrentColumn();
		assertEquals(first, second);
	}
	
	//tests if getCurrentRow() returns an array containing each cell on the current row
	@Test
	void getCurrentRowTestKids() {
		setUpKids();
		model.setCurrentRow();
		WordleResponse[] currentRow = model.getCurrentRow();
		assertNotNull(currentRow);
		for (WordleResponse wordleResponse : currentRow) {
			assertNotNull(wordleResponse);
			assertNotNull(wordleResponse.getChar());
			assertNotNull(wordleResponse.getForegroundColor());
			assertNotNull(wordleResponse.getBackgroundColor());
		}
	}
	
	@Test
	void getCurrentRowTestNorm() {
		setUpNormal();
		model.setCurrentRow();
		WordleResponse[] currentRow = model.getCurrentRow();
		assertNotNull(currentRow);
		for (WordleResponse wordleResponse : currentRow) {
			assertNotNull(wordleResponse);
			assertNotNull(wordleResponse.getChar());
			assertNotNull(wordleResponse.getForegroundColor());
			assertNotNull(wordleResponse.getBackgroundColor());
		}
	}
	
	@Test
	void getCurrentRowTestHard() {
		setUpHard();
		model.setCurrentRow();
		WordleResponse[] currentRow = model.getCurrentRow();
		assertNotNull(currentRow);
		for (WordleResponse wordleResponse : currentRow) {
			assertNotNull(wordleResponse);
			assertNotNull(wordleResponse.getChar());
			assertNotNull(wordleResponse.getForegroundColor());
			assertNotNull(wordleResponse.getBackgroundColor());
		}
	}
	
	//tests if getCurrentRowNumber() returns an integer representing the current row
	@Test
	void getCurRowNumTestKids() {
		setUpKids();
		assertNotNull(model.getCurrentRowNumber());
		assertEquals(model.getCurrentRowNumber(), -1);
		model.setCurrentRow();
		assertEquals(model.getCurrentRowNumber(), 0);
	}
	
	@Test
	void getCurRowNumTestNorm() {
		setUpNormal();
		assertNotNull(model.getCurrentRowNumber());
		assertEquals(model.getCurrentRowNumber(), -1);
		model.setCurrentRow();
		assertEquals(model.getCurrentRowNumber(), 0);
	}
	
	@Test
	void getCurRowNumTestHard() {
		setUpHard();
		assertNotNull(model.getCurrentRowNumber());
		assertEquals(model.getCurrentRowNumber(), -1);
		model.setCurrentRow();
		assertEquals(model.getCurrentRowNumber(), 0);
	}
	
	//tests if setCurrentRow() returns the boolean indicated whether there are available empty rows on the grid
	@Test
	void setCurRowFalseTestKids() {
		setUpKids();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		assertFalse(model.setCurrentRow());
	}
	
	@Test
	void setCurRowFalseTestNorm() {
		setUpNormal();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		assertFalse(model.setCurrentRow());
	}
	
	@Test
	void setCurRowFalseTestHard() {
		setUpHard();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		assertFalse(model.setCurrentRow());
	}
	
	@Test
	void setCurRowTrueTestKids() {
		setUpKids();
		assertTrue(model.setCurrentRow());
	}
	
	@Test
	void setCurRowTrueTestNorm() {
		setUpNormal();
		assertTrue(model.setCurrentRow());
	}
	
	@Test
	void setCurRowTrueTestHard() {
		setUpHard();
		assertTrue(model.setCurrentRow());
	}
	
	//tests if getWordleGrid() successfully returns a 2d array of empty WordleResponses
	@Test
	void getWordleGridEmptyTestKids() {
		setUpKids();
		WordleResponse[][] grid = model.getWordleGrid();
		assertNotNull(grid);
		for (int row = 0; row < grid.length; row++) {
			for (int column = 0; column < grid[row].length; column++) {
				assertNull(grid[row][column]);
			}}	
	}
	
	@Test
	void getWordleGridEmptyTestNorm() {
		setUpNormal();
		WordleResponse[][] grid = model.getWordleGrid();
		assertNotNull(grid);
		for (int row = 0; row < grid.length; row++) {
			for (int column = 0; column < grid[row].length; column++) {
				assertNull(grid[row][column]);
			}}	
	}
	
	@Test
	void getWordleGridEmptyTestHard() {
		setUpHard();
		WordleResponse[][] grid = model.getWordleGrid();
		assertNotNull(grid);
		for (int row = 0; row < grid.length; row++) {
			for (int column = 0; column < grid[row].length; column++) {
				assertNull(grid[row][column]);
			}}	
	}
	
	//tests if getWordleGrid() successfully returns a 2d array of filled WordleResponses
	@Test
	void getWordleGridFilledTestKids() {
		setUpKids();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		WordleResponse[][] grid = model.getWordleGrid();
		for (int row = 0; row < grid.length; row++) {
			for (int column = 0; column < grid[row].length; column++) {
				assertNotNull(grid[row][column]);
			}}	
	}
	
	@Test
	void getWordleGridFilledTestNorm() {
		setUpNormal();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		WordleResponse[][] grid = model.getWordleGrid();
		for (int row = 0; row < grid.length; row++) {
			for (int column = 0; column < grid[row].length; column++) {
				assertNotNull(grid[row][column]);
			}}	
	}
	
	@Test
	void getWordleGridFilledTestHard() {
		setUpHard();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		model.setCurrentRow();
		WordleResponse[][] grid = model.getWordleGrid();
		for (int row = 0; row < grid.length; row++) {
			for (int column = 0; column < grid[row].length; column++) {
				assertNotNull(grid[row][column]);
			}}	
	}
	
	//tests if getMaximumRows() returns the maximum number of rows that the grid may have
	@Test
	void getMaxRowsTestKids() {
		setUpKids();
		assertEquals(4, model.getMaximumRows());
	}
	
	@Test
	void getMaxRowsTestNorm() {
		setUpNormal();
		assertEquals(6, model.getMaximumRows());
	}
	
	@Test
	void getMaxRowsTestHard() {
		setUpHard();
		assertEquals(8, model.getMaximumRows());
	}
	
	//tests if getColumnCount() returns the number of columns the grid has
	@Test
	void getColCountTestKids() {
		setUpKids();
		assertEquals(3, model.getColumnCount());
	}
	
	@Test
	void getColCountTestNorm() {
		setUpNormal();
		assertEquals(5, model.getColumnCount());
	}
	
	@Test
	void getColCountTestHard() {
		setUpHard();
		assertEquals(7, model.getColumnCount());
	}
	
	//tests if getCurrentColumn() returns which column that the user is currently typing into
	@Test
	void getCurrColTestKids() {
		setUpKids();
		assertNotNull(model.getCurrentColumn());
		assertEquals(-1, model.getCurrentColumn());
		model.setCurrentColumn('a');
		assertEquals(0, model.getCurrentColumn());
	}
	
	@Test
	void getCurrColTestNorm() {
		setUpNormal();
		assertNotNull(model.getCurrentColumn());
		assertEquals(-1, model.getCurrentColumn());
		model.setCurrentColumn('a');
		assertEquals(0, model.getCurrentColumn());
	}
	
	@Test
	void getCurrColTestHard() {
		setUpHard();
		assertNotNull(model.getCurrentColumn());
		assertEquals(-1, model.getCurrentColumn());
		model.setCurrentColumn('a');
		assertEquals(0, model.getCurrentColumn());
	}
	
	//tests if getTotalWordCount() returns the size of the word list
	@Test
	void getTotWordCountTestKids() {
		setUpKids();
		assertTrue(model.getTotalWordCount() == 635);		
	}
	
	@Test
	void getTotWordCountTestNorm() {
		setUpNormal();
		assertTrue(model.getTotalWordCount() == 4435);		
	}
	
	@Test
	void getTotWordCountTestHard() {
		setUpHard();
		assertTrue(model.getTotalWordCount() == 9415);		
	}
	
	
	

}
