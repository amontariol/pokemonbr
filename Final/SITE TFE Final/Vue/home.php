<?php
session_start();
echo"<!DOCTYPE html>
<html lang='en'>

<head>

  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'>
  <meta name='description' content=''>
  <meta name='author' content=''>
  <meta http-equiv='X-UA-Compatible' content='IE=edge'>

  <title>Pokemon Battle Royale - Wiki</title>

  <!-- Bootstrap core CSS -->
  <link href='../vendor/bootstrap/css/bootstrap.min.css' rel='stylesheet'>

  <!-- Custom fonts for this template -->
  <link href='../vendor/fontawesome-free/css/all.min.css' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Montserrat:400,700' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Kaushan+Script' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700' rel='stylesheet' type='text/css'>


  <!-- Custom styles for this template -->
  <link href='../css/agency.min.css' rel='stylesheet'>

</head>

<body id='page-top'>";

if ($_SESSION['logged']===FALSE)
{
  echo"  <!-- Navigation -->
  <nav class='navbar navbar-expand-lg navbar-dark fixed-top' id='mainNav'>
      <div class='container'>
        <a class='navbar-brand js-scroll-trigger' href='#page-top'>Pokemon Battle Royale</a>
        <button class='navbar-toggler navbar-toggler-right collapsed' type='button' data-toggle='collapse' data-target='#navbarResponsive' aria-controls='navbarResponsive' aria-expanded='false' aria-label='Toggle navigation'>
          <i class='fas fa-bars'></i>
        </button>
        <div class='collapse navbar-collapse' id='navbarResponsive'>
          <ul class='navbar-nav text-uppercase ml-auto'>
            <li class='nav-item'>
              <a class='nav-link js-scroll-trigger' href='#about'>About</a>
            </li>
            <li class='nav-item'>
              <a class='nav-link js-scroll-trigger' href='#stats'>Stats</a>
            </li>
            <li class='nav-item'>
              <a class='nav-link js-scroll-trigger' href='#team'>Team</a>
            </li>
            <li class='nav-item'>
              <a class='nav-link js-scroll-trigger' href='../Controleur/controleur_wiki.php'>Wiki</a>
            </li>
            <li class='nav-item'>
              <a href='#myloginModal' class=' nav-link trigger-btn' data-toggle='modal'>Login</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <div id='myloginModal' class='modal fade'>
    <div class='modal-dialog modal-login'>
      <div class='modal-content'>
        <div class='modal-header'>			
          <h4 class='modal-title'>Member Login</h4>	
                  <button type='button' class='close' data-dismiss='modal' aria-hidden='true'>&times;</button>
        </div>
        <div class='modal-body'>
          <form action='../Controleur/controleur_connexion.php' method='post'>
            <div class='form-group'>
              <input type='text' class='form-control' name='login' placeholder='Login' required='required'>		
            </div>
            <div class='form-group'>
              <input type='password' class='form-control' name='password' placeholder='Password' required='required'>	
            </div>        
            <div class='form-group'>
              <button type='submit' class='btn btn-primary btn-lg btn-block login-btn'>Login</button>
            </div>
          </form>
        </div>
        <div class='modal-footer' id='modalcontainer'>
          <a href='#myforgotModal' class=' nav-link trigger-btn' data-toggle='modal' data-dismiss='modal'>Forgot Password?</a>

          <a href='#myregisterModal' class=' nav-link trigger-btn' data-toggle='modal' data-dismiss='modal'>new User?</a>
        </div>
      </div>
    </div>
  </div>  

  <div id='myregisterModal' class='modal fade'>
    <div class='modal-dialog modal-login'>
      <div class='modal-content'>
        <div class='modal-header'>			
          <h4 class='modal-title'>New Member? Sign-up!</h4>	
                  <button type='button' class='close' data-dismiss='modal' aria-hidden='true'>&times;</button>
        </div>
        <div class='modal-body'>
          <form action='../Controleur/controleur_inscription.php' method='post'>
            <div class='form-group'>
              <input type='text' class='form-control' name='Firstname' placeholder='First Name' required='required'>		
            </div>
            <div class='form-group'>
              <input type='text' class='form-control' name='Lastname' placeholder='Last Name' required='required'>		
            </div>
            <div class='form-group'>
              <input type='text' class='form-control' name='emailadress' placeholder='Email Adress' required='required'>		
            </div>
            <div class='form-group'>
              <input type='text' class='form-control' name='login' placeholder='Login' required='required'>    
            </div>
            <div class='form-group'>
              <input type='password' class='form-control' name='password' placeholder='Password' required='required'>	
            </div>  

            <div class='form-group'>
              <button type='submit' class='btn btn-primary btn-lg btn-block login-btn'>Sign up</button>
            </div>
          </form>
        </div>
        <div class='modal-footer' id='modalcontainer'>
          <a href='#myloginModal' class=' nav-link trigger-btn' data-toggle='modal' data-dismiss='modal'>Already Signed up?</a>
        </div>
      </div>
    </div>
  </div>  

  <div id='myforgotModal' class='modal fade'>
    <div class='modal-dialog modal-login'>
      <div class='modal-content'>
        <div class='modal-header'>			
          <h4 class='modal-title'>Forgot Password?</h4>	
          <button type='button' class='close' data-dismiss='modal' aria-hidden='true'>&times;</button>
        </div>
        <div class='modal-body'>
          <form action='../Controleur/controleur_mdp_oublie.php' method='post'>
            <div class='form-group'>
              <input type='text' class='form-control' name='emailadress' placeholder='Email Adress:' required='required'>		
            </div>      
            <div class='form-group'>
              <button type='submit' class='btn btn-primary btn-lg btn-block login-btn'>Send</button>
            </div>
          </form>
        </div>
        <div class='modal-footer' id='modalcontainer'>
          <a href='#myloginModal' class=' nav-link trigger-btn' data-toggle='modal' data-dismiss='modal'>Cancel</a>
        </div>
      </div>
    </div>
  </div> ";
}
else
{
  echo"  <!-- Navigation -->
  <nav class='navbar navbar-expand-lg navbar-dark fixed-top' id='mainNav'>
  <div class='container'>
    <a class='navbar-brand js-scroll-trigger' href='#page-top'>Pokemon Battle Royale</a>
    <button class='navbar-toggler navbar-toggler-right collapsed' type='button' data-toggle='collapse' data-target='#navbarResponsive' aria-controls='navbarResponsive' aria-expanded='false' aria-label='Toggle navigation'>
      <i class='fas fa-bars'></i>
    </button>
    <div class='collapse navbar-collapse' id='navbarResponsive'>
      <ul class='navbar-nav text-uppercase ml-auto'>
        <li class='nav-item'>
          <a class='nav-link js-scroll-trigger' href='#about'>About</a>
        </li>
        <li class='nav-item'>
          <a class='nav-link js-scroll-trigger' href='#stats'>Stats</a>
        </li>
        <li class='nav-item'>
          <a class='nav-link js-scroll-trigger' href='#team'>Team</a>
        </li>
        <li class='nav-item'>
          <a class='nav-link js-scroll-trigger' href='wiki.php'>Wiki</a>
        </li>
        <li class='nav-item'>
          <a href='../Downloads/Final.zip' class='nav-link'>Download the game</a>
        </li>
        <li class='nav-item'>
          <a href='../Controleur/controleur_home' class='nav-link'>Log-out</a>
        </li>
      </ul>
    </div>
  </div>
</nav>";
}

  /*Header -->*/
echo"  <header class='masthead'>
    <div class='container'>
      <div class='intro-text'>
        <div class='intro-lead-in'>Welcome to our website</div>
        <div class='intro-heading text-uppercase'>Pokemon Battle Royale</div>
        <a class='btn btn-primary btn-xl text-uppercase js-scroll-trigger' href='#about'>Learn more</a>
      </div>
    </div>
  </header>

<!-- About -->
  <section id='about'>
    <div class='container'>
      <div class='row'>
        <div class='col-lg-12 text-center'>
          <h2 class='section-heading text-uppercase'>About</h2>
          <h3 class='section-subheading text-muted'>Learn about our game.</h3>
        </div>
      </div>
      <div class='row'>
        <div class='col-lg-12'>
          <ul class='timeline'>
            <li>
              <div class='timeline-image'>
                <img class='rounded-circle img-fluid' src='../img/about/1.jpg' alt=''>
              </div>
              <div class='timeline-panel'>
                <div class='timeline-heading'>
                  <h4>January-February 2019</h4>
                  <h4 class='subheading'>Our First steps...</h4>
                </div>
                <div class='timeline-body'>
                  <p class='text-muted'>For the first two months of our project, we had to figure out what our subject would be. We landed on Pokemon and we decided to combine it with the evermore popular Battle Royale format.</p>
                </div>
              </div>
            </li>
            <li class='timeline-inverted'>
              <div class='timeline-image'>
                <img class='rounded-circle img-fluid' src='../img/about/2.jpg' alt=''>
              </div>
              <div class='timeline-panel'>
                <div class='timeline-heading'>
                  <h4>February 27 - March 1st</h4>
                  <h4 class='subheading'>Expanding on our 1st ideas...</h4>
                </div>
                <div class='timeline-body'>
                  <p class='text-muted'>for three days, we got to work on our project non-stop. During those 3 days, we analysed our ideas and mapped everything out on paper. We also got help from our IT teachers regarding python, php and more.</p>
                </div>
              </div>
            </li>
            <li>
              <div class='timeline-image'>
                <img class='rounded-circle img-fluid' src='../img/about/3.jpg' alt=''>
              </div>
              <div class='timeline-panel'>
                <div class='timeline-heading'>
                  <h4>March 2019</h4>
                  <h4 class='subheading'>Analyzing different situations</h4>
                </div>
                <div class='timeline-body'>
                  <p class='text-muted'>In the month of March, we started thinking of how to's regarding code. We had to think of different methods that would allow us to achieve our goals.</p>
                </div>
              </div>
            </li>
            <li class='timeline-inverted'>
              <div class='timeline-image'>
                <img class='rounded-circle img-fluid' src='../img/about/4.jpg' alt=''>
              </div>
              <div class='timeline-panel'>
                <div class='timeline-heading'>
                  <h4>April - May 2019</h4>
                  <h4 class='subheading'>Coding</h4>
                </div>
                <div class='timeline-body'>
                  <p class='text-muted'>For these 2 months, we coded. We first programmed our launcher fulfilling our requirements for Tkinter. We then started coding in pygame and php/html. </p>
                </div>
              </div>
            </li>
            <li class='timeline-inverted'>
              <div class='timeline-image'>
                <h4>The
                  <br><hr/>end!</h4>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>

<!-- Stats -->
  <section id='stats'>
    <div class='container'>
      <div class='row'>
        <div class='col-lg-12 text-center'>
          <h2 class='section-heading text-uppercase'>Stats</h2>
          <h3 class='section-subheading text-muted'>Learn about the best players and their stats.</h3>
        </div>
      </div>
      <div class='row text-center'>
        <div class='col-md-6'>";


        require('../Model/model.php');//appel de model.php
        $db = new User();//instanciation d'un nouvel objet

        $result = $db->recupmembre2();//appel d'une fonction pour récupérer des champs specifiques de la db
      //creation de la tables
        echo "<table class='table'><caption>List of top players</caption><thead>
                <tr>
                  <th scope='col'>Name</th>
                  <th scope='col'>Number of Wins</th>
                  <th scope='col'>Number of Games</th>
                  <th scope='col'>Best Score</th>
                </tr>
                </thead>
                <tbody>";

        foreach($result as $ligne)//creation des elements de la table en fonction du renvoi de la fonction
              {
                    echo "<tr>";
                    echo "<th scope='row'> $ligne[Login]</th>";
                    echo "<td> $ligne[nbwins]</td>";
                    echo "<td> $ligne[nbparties]</td>";
                    echo "<td> $ligne[scoremax]</td>";
                    echo "</tr>";
              }
        echo '</div>';
        
 
        echo "</tbody></table></div><div class='col-md-6'>";
        //voir au dessus
        $result = $db->recuppokemon();

        echo "<table class='table'><caption>List of top pokemon</caption><thead>
                <tr>
                  <th scope='col'>#</th>
                  <th scope='col'>Name</th>
                  <th scope='col'>Type</th>
                </tr>
                </thead>
                <tbody>";

        foreach($result as $ligne)
              {
                    echo "<tr>";
                    echo "<th scope='row'> $ligne[id]</th>";
                    echo "<td> $ligne[Nom]</td>";
                    echo "<td> $ligne[numberofuses]</td>";
                    echo "</tr>";
              }
        
 
        echo "</tbody></table>";
      echo"
       
  </section>

  <!-- Team -->
  <section class='bg-light' id='team'>
    <div class='container'>
      <div class='row'>
        <div class='col-lg-12 text-center'>
          <h2 class='section-heading text-uppercase'>Our Amazing Team</h2>
          <h3 class='section-subheading text-muted'>Meet our team.</h3>
        </div>
      </div>
      <div class='row'>
        <div class='col-sm-6'>
          <div class='team-member'>
            <img class='mx-auto rounded-circle' src='../img/team/1.jpg' alt=''>
            <h4>Adrien Montariol</h4>
          </div>
        </div>
        <div class='col-sm-6'>
          <div class='team-member'>
            <img class='mx-auto rounded-circle' src='../img/team/3.jpg' alt=''>
            <h4>Alexandre Wery</h4>
          </div>
        </div>
      </div>
      <div class='row'>
        <div class='col-lg-8 mx-auto text-center'>
          <p class='large text-muted'>This is us. We're the ones who coded this wonderful game and website. </p>
        </div>
      </div>
    </div>
  </section>

 

  <!-- Footer -->
  <footer class='bg-dark'>
    <div class='container'>
      <div class='row'>
        <div class='col-md-6'>
          <span class='copyright'>Copyright &copy; Pokemon Battle Royale</span>
        </div>
        <div class='col-md-6'>
          <ul class='list-inline quicklinks'>
            <li class='list-inline-item'>
              <a href='#'>IPET Nivelles</a>
            </li>
            <li class='list-inline-item'>
              <a href='#'>TFE 2018-2019</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
  <!-- Bootstrap core JavaScript -->
  <script src='../vendor/jquery/jquery.min.js'></script>
  <script src='../vendor/bootstrap/js/bootstrap.bundle.min.js'></script>

  <!-- Plugin JavaScript -->
  <script src='../vendor/jquery-easing/jquery.easing.min.js'></script>

  <!-- Contact form JavaScript -->
  <script src='../js/jqBootstrapValidation.js'></script>
  <script src='../js/contact_me.js'></script>

  <!-- Custom scripts for this template -->
  <script src='../js/agency.min.js'></script>


</body>

</html>";
?>
