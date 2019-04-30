<?php

class dbOperations
{
    private $con;
    
    function __construct() {
        require_once dirname(__FILE__).'/dbConnect.php';
        $db=new dbConnect();
        $this->con=$db->connect();
       
    }
    
    public function createUser($username,$pass,$email)
    {
        //d2i2a 4:51 tut3
       // INSERT INTO `user` (`id`, `u_type`, `fname`, `lname`, `dob`, `Email`, `username`, `password`, `Gender`, `phoneno`) VALUES (NULL, '1', 'mo', 'me', '2019-04-10', 'mok@miu.com', 'mok', 'mok', '2', '012255445');
        $password=md5($pass);
        $stmt= $this->con->prepare("INSERT INTO `user` (`username`, `password`, `email`)  VALUES (?, ?, ?);");
        $stmt->bind_param("sss",$username,$password,$email);
        if($stmt->execute())
        {return true;}
        else 
        {return false;}
    }
    
    
    
//    function insertDS($u_id,$image,$imageSlat,$imageSlng,$imageDlat,$imageDlng)
//    {
//        $
//    }
}



?>