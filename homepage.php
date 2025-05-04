<?php include('navbar.php'); ?>
<?php
$visits = 12000;
$play_time = 3500;
$gestures = 1200000;
?>

<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page 1</title>
  <link rel="stylesheet" media="screen" href="css/style.css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">

  <style>
    .card {
      width: 75%;
      max-width: 350px; 
      margin: auto; 
    }

    .card-body {
      padding: 3rem; 
    }

     .card {
      transition: transform 0.3s ease, box-shadow 0.3s ease; 
    }

    .card:hover {
      transform: translateY(-10px); 
      box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); 
    }

        .testimonial-card {
      background-color: #f9f9f9;
      border-radius: 20px;
      padding: 30px;
      text-align: center;
      height: 100%;
    }

    .testimonial-img {
      width: 70px;
      height: 70px;
      border-radius: 50%;
      object-fit: cover;
      margin-bottom: 15px;
    }

    .testimonial-name {
      font-weight: 600;
      margin-bottom: 10px;
    }

    .testimonial-text {
      color: #6c757d;
      font-size: 15px;
    }

     @media (max-width: 906px) {
    .fs-responsive h1 {
      font-size: 1.5rem !important; /* Smaller heading */
    }

    .fs-responsive p {
      font-size: 0.95rem !important; /* Smaller paragraph */
    }

    .fs-responsive .btn {
      font-size: 0.85rem !important; /* Smaller buttons */
      padding: 0.5rem 1rem !important;
    }
  }

    
  </style>

<link href="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>

</head>

<body>


  <div class="position-absolute top-0 start-0 w-100 h-100">
    <div id="particles-js"></div>

    <div class="position-absolute text-white p-3 fs-responsive" style="top: 50%; left: 8%; transform: translateY(-50%);">

      <h1 class="display-6 fw-bold mb-4">Control the Future With a Wave</h1>
      
      <p class="lead fs-5">
        Experience seamless interaction with your devices using just natural gestures. <br>
        <strong>GESTURO</strong> brings touchless control to life.
      </p>

      <div class="mt-4">
        <a href="#" class="btn btn-primary btn-lg me-3 px-3 py-2">Get Started</a>
        <a href="#" class="btn btn-outline-light btn-lg px-3 py-2">Watch Demo</a>
      </div>

    </div>

    <div class="container py-5">

      <div class="text-center mb-5">
        <h2 class="fw-bold display-6">Features</h2>
      </div>

      <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-5 mt-5 mb-5">
        <!-- Card 1 -->
        <div class="col">
          <div class="card shadow-lg border-light h-100">
            <div class="card-body text-center">
              <i class="fas fa-hand-paper fs-3 mb-3"></i>
              <h5 class="card-title">Gesture Detection</h5>
              <p class="card-text">Accurately detects and interprets your gestures for seamless interaction.</p>
            </div>
          </div>
        </div>
        <!-- Card 2 -->
        <div class="col">
          <div class="card shadow-lg border-light h-100">
            <div class="card-body text-center">
              <i class="fas fa-gamepad fs-3 mb-3"></i>
              <h5 class="card-title">Gesture-Based Gaming</h5>
              <p class="card-text">Control games using simple hand gestures for a fully immersive experience.</p>
            </div>
          </div>
        </div>
        <!-- Card 3 -->
        <div class="col">
          <div class="card shadow-lg border-light h-100">
            <div class="card-body text-center">
              <i class="fas fa-sync-alt fs-3 mb-3"></i>
              <h5 class="card-title">Real-Time Feedback</h5>
              <p class="card-text">Instant and responsive gesture recognition for smooth control.</p>
            </div>
          </div>
        </div>
        <!-- Card 4 -->
        <div class="col">
          <div class="card shadow-lg border-light h-100">
            <div class="card-body text-center">
              <i class="fas fa-cogs fs-3 mb-3"></i>
              <h5 class="card-title">Customizable Controls</h5>
              <p class="card-text">Personalize gesture actions to suit your style or needs.</p>
            </div>
          </div>
        </div>
        <!-- Card 5 -->
        <div class="col">
          <div class="card shadow-lg border-light h-100">
            <div class="card-body text-center">
              <i class="fas fa-desktop fs-3 mb-3"></i>
              <h5 class="card-title">PC and Phone Support</h5>
              <p class="card-text">Works seamlessly on both PCs and mobile devices for on-the-go gesture control.</p>
            </div>
          </div>
        </div>
        <!-- New Card: User-Friendly Interface -->
        <div class="col">
          <div class="card shadow-lg border-light h-100">
            <div class="card-body text-center">
              <i class="fas fa-laptop fs-3 mb-3"></i>
              <h5 class="card-title">User-Friendly Interface</h5>
              <p class="card-text">Easy setup and intuitive controls ensure a smooth experience for beginners and pros alike.</p>
            </div>
          </div>
        </div>
      </div>
    </div>



    <div class="container-fluid py-5 bg-dark text-white mt-5" style="min-height: 550px;">

      <div class="stats-section" id="statsSection" class="h-100">
        <div class="row justify-content-center align-items-center text-center" style="min-height: 450px;">
          
          <!-- Heading Section -->
          <div class="col-12 mb-5">
            <h2 class="fw-bold display-7">Engagement Stats</h2>
          </div>

          <!-- Total Stats Row -->
          <div class="col-md-4 mb-5 ">
            <h3 class="fs-1"><span id="totalVisits">0</span>+</h3>
            <p class="lead fw-semibold">Total Visits</p>
          </div>

          <div class="col-md-2 mb-5">
            <h3 class="fs-1"><span id="totalPlayTime">0</span> Hrs</h3>
            <p class="lead fw-semibold">Total Play Time</p>
          </div>

          <div class="col-md-4 mb-5">
            <h3 class="fs-1"><span id="gesturesDetected">0</span></h3>
            <p class="lead fw-semibold">Gestures Detected</p>
          </div>

          <!-- Description -->
          <div class="col-12 mt-4">
            <p class="fs-6 text-white-50 px-3">
              NeoMotion tracks key metrics like visits, playtime, and gesture activity, providing real-time insights to enhance and personalize your experience.
            </p>
          </div>
        </div>
      </div>
    </div>

    
    <div class="container py-5 mt-5 mb-5">
      <div class="text-center mb-5" data-aos="fade-up" data-aos-duration="1000">
        <h2 class="fw-bold">What Our Partners Say</h2>
        <p class="text-muted">We're proud to collaborate with innovative minds who are transforming the tech world. Here’s
          what our partners have to
          say about working with Gesturo.</p>
      </div>

      <div class="row g-4">
        <div class="col-md-4" data-aos="fade-up" data-aos-duration="1000" data-aos-delay="200">
          <div class="testimonial-card h-100" >
            <img src="assets/rey_icon.jpg" alt="Rebecca Ortiz" class="testimonial-img" />
            <div class="testimonial-name">Rëy</div>
            <p class="testimonial-text">"Gesturo’s gesture control system is truly revolutionary. It's opening up new
              possibilities for both gaming and everyday
              technology. We’re excited to see what the future holds with this partnership."</p>
          </div>
        </div>

        <div class="col-md-4" data-aos="fade-up" data-aos-duration="1000" data-aos-delay="400">
          <div class="testimonial-card h-100">
            <img src="assets/XXD.jpeg" alt="Michael Berillo" class="testimonial-img" />
            <div class="testimonial-name">XXD</div>
            <p class="testimonial-text">"The seamless integration of gesture controls with our platform has transformed
              how users interact with games and
              devices. Gesturo brings accessibility and innovation together in the most intuitive way."</p>
          </div>
        </div>

        <div class="col-md-4" data-aos="fade-up" data-aos-duration="1000" data-aos-delay="600">
          <div class="testimonial-card h-100">
            <img src="assets/rey_icon.jpg" alt="John Doe" class="testimonial-img" />
            <div class="testimonial-name">-</div>
            <p class="testimonial-text">"With Gesturo, we’ve been able to offer our clients a new level of interaction.
              The precision of their gesture tracking
              makes it the perfect solution for both entertainment and professional environments."</p>
          </div>
        </div>
    </div>
</div>



    <hr style="margin-bottom:20px; border: 0; border-top: 0.1px solid black;">
      <div class="container mt-5 mb-5">
        <div class="row align-items-center g-5">
          <!-- Left Content -->
          <div class="col-md-6 left-content">
            <h2 class="mb-2">Catch <strong>Gesturo</strong> Live at  <strong>I.D.E.A FAIR</strong></h2>

            <div class="mb-4 mt-5">
              <div class="section-number"><strong>01</strong></div>
              <div class="section-title"><strong>Introduction</strong></div>
              <p class="section-text">
               Provide a brief overview of your project, the client's brand, and the main challenges you faced.
              </p>
            </div>

            <div>
              <div class="section-number"><strong>02</strong></div>
              <div class="section-title"><strong>Approach</strong></div>
              <p class="section-text">
               Detail your solution, explaining how you tackled the challenges and how your work benefited the client.
              </p>
            </div>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSeGSf9zO8C6Y3s3m4VtuNElnr18lPjj6Vd6Jcr1cXXDbsdqEQ/viewform" class="btn btn-primary btn-lg me-3 px-3 py-2 mt-4 mb-5" style="font-size: 16px;" target="_blank">Join Now</a>

          </div>

          <div class="col-md-6 image-container text-center mt-4 ">
            <div class="position-relative" style="height: 360px; overflow: hidden; border-radius: 20px;">
            
              <video autoplay muted loop playsinline style="height: 100%; width: 100%; object-fit: cover;">
                <source src="assets/idea_fair_movie.mp4" type="video/mp4">
                Your browser does not support the video tag.
              </video>
            </div>
          </div>
        </div>

        <div class="container py-5 mt-5">
          <div class="text-center mb-5 mt-5">
            <h2 class="fw-bold">Our Trusted Partners</h2>
            <p class="text-muted">We are proud to collaborate with leading companies in the tech industry.</p>
          </div>

          <div class="row justify-content-center g-4">
            <div class="col-md-4 text-center">
              <img src="assets/Idea_fair.webp" alt="Logo 1" class="img-fluid" style="max-height: 120px; object-fit: contain;" />
            </div>
            <div class="col-md-4 text-center">
              <img src="assets/usm.png" alt="Logo 2" class="img-fluid" style="max-height: 120px; object-fit: contain;" />
            </div>
            <div class="col-md-4 text-center">
              <img src="assets/apex.png" alt="Logo 3" class="img-fluid" style="max-height: 120px; object-fit: contain;" />
            </div>
          </div>
        </div>
      </div>

      <?php include('footer.php'); ?>

  </div>





  </div>

  
  



  <script src="js/particles.js"></script>
  <script src="js/app.js"></script>
  <script src="js/stats.js"></script>
 <!-- JavaScript for Counting -->
<script>
  AOS.init();
  document.addEventListener('DOMContentLoaded', function () {
    const visits = <?php echo $visits; ?>;
    const playTime = <?php echo $play_time; ?>;
    const gestures = <?php echo $gestures; ?>;

    let animated = false;

    const counter = (element, target) => {
      let count = 0;
      const increment = target / 100;
      const interval = setInterval(() => {
        count += increment;
        element.textContent = Math.floor(count);
        if (count >= target) {
          clearInterval(interval);
          element.textContent = target;
        }
      }, 20);
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !animated) {
          animated = true;
          counter(document.getElementById('totalVisits'), visits);
          counter(document.getElementById('totalPlayTime'), playTime);
          counter(document.getElementById('gesturesDetected'), gestures);
        }
      });
    }, { threshold: 0.5 });

    observer.observe(document.getElementById('statsSection'));
  });
</script>


</body>

</html>