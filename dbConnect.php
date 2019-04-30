<?php
 
/**
 * A class file to connect to database
 */
class dbConnect {
 
    // constructor
    private $con; 
    function __construct() {
        
    }
 
    // destructor
//    function __destruct() {
//        // closing db connection
//        $this->close();
//    }
 
    /**
     * Function to connect with database
     */
    function connect() {
        // import database connection variables
        include_once dirname(__FILE__).'/constants.php';
 
        // Connecting to mysql database
        $this->con = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
 
   
       if(mysqli_connect_errno()){
				echo "Failed to connect with database".mysqli_connect_err(); 
			}
 
        // returing connection cursor
        return  $this->con; 
    }
 
    /**
     * Function to close db connection
     */
//    function close() {
//        // closing db connection
//        mysql_close();
//    }
 
}
?>