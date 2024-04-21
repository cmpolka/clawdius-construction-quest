/**
 * The purpose of the WordleResponseTest class is to 
 * access the functionality of the WordleResponse class
 * 
 * @author Lekha Reddy
 */

package edu.wm.cs.cs301.wordle.model;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class WordleResponseTest {

	@Test
	private void setUp() throws Exception{

	}
	
	//tests if getChar() returns the correct character
	@Test
	void getCharTest() {
		WordleResponse wordleResponse = new WordleResponse('a', AppColors.GREEN, AppColors.WHITE);
		assertEquals(wordleResponse.getChar(), 'a');
	}
	
	//tests if getBackgroundColor returns the correct color
	@Test
	void backgroundColorTestWhite() {
		WordleResponse wordleResponse = new WordleResponse('b', AppColors.GRAY, AppColors.OUTLINE);
		assertEquals(wordleResponse.getBackgroundColor(), AppColors.GRAY);

	}
	
	@Test
	void backgroundColorTestGray() {
		WordleResponse wordleResponse = new WordleResponse('b', AppColors.GREEN, AppColors.WHITE);
		assertEquals(wordleResponse.getBackgroundColor(), AppColors.GREEN);

	}
	
	//tests if getForegroundColor returns the correct color
	@Test
	void foregroundColorTestWhite() {
		WordleResponse wordleResponse = new WordleResponse('c', AppColors.GREEN, AppColors.WHITE);
		assertEquals(wordleResponse.getForegroundColor(), AppColors.WHITE);

	}
	
	@Test
	void foregroundColorTestGrey() {
		WordleResponse wordleResponse = new WordleResponse('c', AppColors.GREEN, AppColors.GRAY);
		assertEquals(wordleResponse.getForegroundColor(), AppColors.GRAY);

	}
	
	@Test
	void foregroundColorTestOutline() {
		WordleResponse wordleResponse = new WordleResponse('c', AppColors.GRAY, AppColors.OUTLINE);
		assertEquals(wordleResponse.getForegroundColor(), AppColors.OUTLINE);

	}
	
	@Test
	private void tearDown() throws Exception{
		
	}

}
