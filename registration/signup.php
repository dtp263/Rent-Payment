<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

 

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

 
    <head>
        <meta charset="utf-8">
        <title>Credit 2 Rent</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <link rel="stylesheet" href="../css/bootstrap.min.css">
        <link rel="stylesheet" href="../css/bootstrap-theme.min.css">
        <link rel="stylesheet" href="../css/main.css">
        <link rel="stylesheet" href="../css/signup.css">

  </head>
  <body>

  	<?php include('./templates/header.php');?>




  	<div class="signUpForm">
		<form name="login" action="index_submit" method="get" accept-charset="utf-8">  
			<ul>  
				<li>
					<label for="usermail">Email</label>  
					<input type="email" name="usermail" placeholder="yourname@email.com" required>
				</li>  
				<li>
					<label for="password">Password</label>  
					<input type="password" name="password" placeholder="password" required>
				</li>  
				<li>  
				<input type="submit" value="Login">
				</li>  
			</ul>  
		</form>
	</div>





	<div class="blueBorder"></div>
	<div class="footer">
	  <p>&copy; Rent2Share 2013</p>
	</div>        



	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
	<script src="http://code.jquery.com/ui/1.9.2/jquery-ui.js"></script>
	<script src="../js/vendor/bootstrap.min.js"></script>
	<script src="../js/main.js"></script>
  
  </body>
</html>
