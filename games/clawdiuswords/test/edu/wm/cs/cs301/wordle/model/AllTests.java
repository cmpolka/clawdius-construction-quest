/**
 * The purpose of the AllTests class is to 
 * access the functionality of each test case in the
 * test suite
 * 
 * @author Lekha Reddy
 */

package edu.wm.cs.cs301.wordle.model;

import org.junit.platform.suite.api.SelectClasses;
import org.junit.platform.suite.api.Suite;

@Suite
@SelectClasses({ WordleModelTest.class, WordleResponseTest.class })
public class AllTests {

}
