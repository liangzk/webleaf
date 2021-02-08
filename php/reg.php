<html>
<head>
<title>Thank you!</title>
</head>
<body>
<p><img src="/xss/logo.png" alt="" width="243" height="102"></p>
<h1>Thank you!</h1>
<p id="msg">Your registration to this event
has been recorded as follows:</p>
<?php
  $name = $_POST['name'];
  $name = htmlspecialchars($name);
  echo '<p>Name: '.$name.'</p>';
  $email = $_POST['email'];
  echo '<p>E-mail: '.$email.'</p>'; 
  $food = $_POST['food'];
  echo '<p>Food preference: '.$food.'</p>';
?>
</body>
</html>
