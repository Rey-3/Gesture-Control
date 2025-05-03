<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <style>
    /* ====== Base Navbar Styles ====== */
    .navbar-custom {
      position: fixed;
      background-color: black;
      height: 80px;
      padding: 0;
    }

    .navbar-brand {
      font-weight: bold;
      color: #fff !important;
      margin: 0 50px 0 20px;
    }

    .navbar-brand.custom-brand {
      font-size: 18px;
      margin-right: 60px;
    }

    .navbar-brand .bi-app-indicator {
      font-size: 1.8rem;

    }

    .nav-link {
      color: #c9c9c9 !important;
      margin-right: 30px;
      font-size: 16px;
      transition: color 0.3s, text-shadow 0.3s;
    }

    .nav-link:hover {
      color: #fff !important;
      text-shadow: 0 0 10px rgba(255, 255, 255, 0.7);
    }

    /* ====== Scrolled Navbar Styles ====== */
    .navbar-scrolled {
      background-color: white !important;
      box-shadow: 0 3px 12px rgba(0, 0, 0, 0.05);
      transition: background-color 0.3s, box-shadow 0.3s;
    }

    .navbar-scrolled .navbar-brand,
    .navbar-scrolled .nav-link,
    .navbar-scrolled .navbar-toggler {
      color: #000 !important;
    }

    .navbar-scrolled .nav-link {
      color: #464646 !important;
    }

    .navbar-scrolled .nav-link:hover {
      color: #000 !important;
    }

    .navbar-scrolled .navbar-toggler-icon {
      background-color: #fff;
    }

    .navbar-toggler-icon.scrolled {
      background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%23000' viewBox='0 0 30 30'%3e%3cpath stroke='rgba(0,0,0,1)' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
    }



    /* ====== Utility Classes ====== */
    .no-scroll {
      overflow: hidden;
    }



    /* ====== Responsive Styles (Mobile) ====== */
    @media (max-width: 900px) {
      .navbar-custom {
        height: 90px;
      }

      .navbar-collapse {
        position: fixed;
        top: 0px;
        left: 0;
        width: 100%;
        height: 100vh;
        background: rgba(255, 255, 255, 0.9);
        z-index: 1050;
        overflow-y: auto;
        transform: translateY(-100%);
        transition: transform 0.3s ease;
        display: flex !important;
        flex-direction: column;
      }

      .navbar-collapse.show {
        transform: translateY(0);
      }

      .navbar-collapse .navbar-nav {
        flex: 1;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 0;
      }

      .navbar-collapse .nav-item {
        margin: 15px 0;
      }

      .navbar-collapse .nav-link {
        font-size: 1.25rem;
        color: #000 !important;
        margin-left: 30px;
      }

      .navbar-toggler {
        position: relative;
        z-index: 1060;
        border: none;
        font-size: 1.5rem;
        color: black;
      }

      .navbar-toggler:focus {
        outline: none;
        box-shadow: none;
      }
    }
  </style>
</head>

<body>

  <div>
    <div>
      <nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
        <div class="container-fluid d-flex justify-content-between justify-content-lg-center align-items-center">
          <a class="navbar-brand custom-brand" href="#">
            <i class="bi bi-app-indicator me-2"></i> GESTURO
          </a>


          <button class="navbar-toggler me-3 d-lg-none" type="button" data-bs-toggle="collapse"
            data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse flex-grow-0 justify-content-center" id="navbarNav">
            <ul class="navbar-nav ">
              <li class="nav-item me-3"><a class="nav-link fw-bold " href="#">Home</a></li>
              <li class="nav-item me-3"><a class="nav-link fw-bold" href="game.php">Game</a></li>
              <li class="nav-item me-3"><a class="nav-link fw-bold" href="#">About</a></li>
              <li class="nav-item me-3"><a class="nav-link fw-bold" href="#">Contact</a></li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </div>



  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function () {
      const navbar = document.querySelector('.navbar');
      const collapseEl = document.getElementById('navbarNav');
      const toggler = document.querySelector('.navbar-toggler');

      // Ensure toggler icon reference remains accurate
      const updateTogglerIconColor = () => {
        const togglerIcon = toggler.querySelector('.navbar-toggler-icon');
        if (!togglerIcon) return;

        if (window.scrollY > 50) {
          togglerIcon.classList.add('scrolled');
        } else {
          togglerIcon.classList.remove('scrolled');
        }
      };

      // Change navbar on scroll
      window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
          navbar.classList.add('navbar-scrolled');
        } else {
          navbar.classList.remove('navbar-scrolled');
        }
        updateTogglerIconColor();
      });

      // Toggle icon when collapsing
      collapseEl.addEventListener('show.bs.collapse', () => {
        toggler.innerHTML = '<span style="font-size: 3rem; color: black;">&times;</span>';
        document.body.classList.add('no-scroll');
      });

      // When menu is closed
      collapseEl.addEventListener('hide.bs.collapse', () => {
        toggler.innerHTML = '<span class="navbar-toggler-icon"></span>';
        document.body.classList.remove('no-scroll');
        updateTogglerIconColor();
      });

      // Apply correct color on initial load
      updateTogglerIconColor();
    });
  </script>




</body>

</html>