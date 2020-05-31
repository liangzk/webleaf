<html>
  <head>
    <title>PHP Hello</title>
  </head>
  <body>
    <?php 
      # Demonstration of command line injection
      echo shell_exec('cat ' . $_GET['filename']); 
    ?> 
  </body>
</html>
