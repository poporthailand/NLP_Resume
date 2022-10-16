$(document).ready(function () {
  let nav = `
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand"> 
            <img src="../static/img/home.png" alt="Avatar Logo" style="width:30px;" >
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#collapsibleNavbar"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="collapsibleNavbar">
          <ul class="navbar-nav">
            <li class="nav-item">
              <form  action="/" 
              method="POST">
              <input id="input1" type="submit" value="resume" class="nav-link text-uppercase" href="#"></input>  
              </form>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    `;

  $("#navbar").html(nav);
});
