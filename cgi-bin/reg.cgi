#!/usr/bin/perl
use CGI qw(:standard);
use HTML::Entities; 

print <<END;
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
END

$regfile = 'registrations.tsv';

$name = param('name');
#HTML::Entities::encode($name); 
$email = param('email');
$food = param('food');

#open(REG,">>$regfile") or fail();
#print REG "$name\t$email\t$food\n";
#close(REG);

($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) =
    gmtime(time);
$now = sprintf "%4d-%02d-%02dT%02d:%02dZ\n",
    1900+$year,$mon+1,$mday,$hour,$min;

print <<END;
<html>
<head>
<title>Thank you!</title>
</head>
<body>
<p><img src="/logo.png" alt="" width="243" height="102"></p>
<h1>Thank you!</h1>
<p id="msg">Your registration to this event
has been recorded as follows:</p>
<p>Name: $name</p>
<p>E-mail: $email</p>
<p>Food preference: $food</p>
</body>
</html>
END

sub fail {
   print "<title>Error</title>",
   "<p>Error: cannot record your registration!</p>";
   exit; }

