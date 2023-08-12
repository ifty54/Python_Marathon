<?php

#Propertise->attributes of a class
#Method->behavior of a class

class student{
    public $name;
    public $age;
    public $gender;
}

    function __construct($n,$a,$g){
        $this->name = $n;
        $this->age = $a;
        $this->gender = $g;
    }

#Method
    function info(){
        echo "<h3>Student Profile</h3>";
        echo "Student Name: " . $this->name . "<br>";
        echo "Student Age: " . $this->age . "<br>";
        echo "Student Gender: " . $this->gender . "<br>";
    }

#Object
$e1 = new student("John", 26, "male");
$e1->info();

?>
