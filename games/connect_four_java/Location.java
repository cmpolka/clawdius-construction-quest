/**
 * The Location class assigns an empty string to be the original token associated with a location.
 * It also contains methods to change/set the symbol of a particular location, check whether
 * a location is empty, check which symbol is at a certain location, and compare the symbol at
 * one location to the symbol at another location.
 * 
 * @author Lekha Reddy
 */
package edu.wm.cs.cs301.connectn;

public class Location {
	private Character symbol;
	private String setSymbol;

	
	public Location() {
        this.symbol = ' ';

	}
	
	//to change the symbol of a certain location
    public void setSymbol(Character symbol) {
        this.symbol = symbol;
    }
	
    
   //to check if a location has no X or O
	public boolean isEmpty() {
		if (this.getToken() == ' ' || this.getToken() == null) {
			return true;
		}
		return false;
	}
	
	//to check which symbol is at a location
	public Character getToken() {
		return symbol;
	}
	
	//to check if one location's object is the same as another
	@Override
	public boolean equals(Object other) {
	    if (this == other) {
	        return true; // Same object reference
	    }
	    Location location = (Location)other; // Cast the other object to Location

	    if (!(location.getToken().equals('O')) && !(this.getToken().equals('O'))) {
	    	return true;
	    }
	    if ((location.getToken().equals('X')) && (this.getToken().equals('X'))) {
	    	return true;
	    }
//        if (this.getToken().equals(' ') || location.getToken().equals(' ')) {
//            return false;
////        }

	    return false;
	}
	
	
	
}
