<html>
<body>
<form action="index.php" method="post">
Number <input type="number" name="num"><br>
<input type="submit" name="show table">
<?php
$num=$_POST["num"];
echo "<br>"; 
         for( $i = 0; $i<20; $i++ ) {
            $res=$num*$i;
            echo $num."*".$i."=".$res."<br>";
         }
?>
</form>
</body>
</html> 
