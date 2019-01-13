(function($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top - 56)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#mainNav',
    offset: 57
  });

  // Collapse Navbar
  var navbarCollapse = function() {
    if ($("#mainNav").offset().top > 100) {
      $("#mainNav").addClass("navbar-shrink");
    } else {
      $("#mainNav").removeClass("navbar-shrink");
    }
  };
  // Collapse now if page is not at top
  navbarCollapse();
  // Collapse the navbar when page is scrolled
  $(window).scroll(navbarCollapse);

  // Scroll reveal calls
  window.sr = ScrollReveal();

  sr.reveal('.sr-icon-1', {
    delay: 200,
    scale: 0
  });
  sr.reveal('.sr-icon-2', {
    delay: 400,
    scale: 0
  });
  sr.reveal('.sr-icon-3', {
    delay: 600,
    scale: 0
  });
  sr.reveal('.sr-icon-4', {
    delay: 800,
    scale: 0
  });
  sr.reveal('.sr-button', {
    delay: 200,
    distance: '15px',
    origin: 'bottom',
    scale: 0.8
  });
  sr.reveal('.sr-contact-1', {
    delay: 200,
    scale: 0
  });
  sr.reveal('.sr-contact-2', {
    delay: 400,
    scale: 0
  });

  // Magnific popup calls
  $('.popup-gallery').magnificPopup({
    delegate: 'a',
    type: 'image',
    tLoading: 'Loading image #%curr%...',
    mainClass: 'mfp-img-mobile',
    gallery: {
      enabled: true,
      navigateByImgClick: true,
      preload: [0, 1]
    },
    image: {
      tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
    }
  });

  //$('#myimg').attr("src", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Liliumbulbiferumflowertop.jpg/220px-Liliumbulbiferumflowertop.jpg");

  
  // Set the configuration for your app
  // TODO: Replace with your project's config object
  var config = {
    apiKey: "AIzaSyDCxMSf8FRT-x0ZwftciFZmtyvdi0hFCTQ",
    authDomain: "artkit-d6193.firebaseapp.com",
    databaseURL: "https://artkit-d6193.firebaseio.com",
    projectId: "artkit-d6193",
    storageBucket: "artkit-d6193.appspot.com",
    messagingSenderId: "912497536628"
  };
  firebase.initializeApp(config);

  // Get a reference to the database service
  var database = firebase.database();
  var storage = firebase.storage();
  var storageRef = storage.ref();
  var numPicture = 18;

  var imagesRef;
  var fileName;
  var spaceRef;

  var pathReference;
  var gsReference;

  for (var current = 1; current <= numPicture; current++) {
    

    imagesRef = storageRef.child('images');
    fileName = current + '.jpg';
    spaceRef = imagesRef.child(fileName);

    pathReference = storage.ref(fileName);
    gsReference = storage.refFromURL('gs://bucket/images/' + current + '.jpg');

    // download data via url
    storageRef.child('images/' + current + '.jpg').getDownloadURL().then((function(current, url) {
      console.log(current, url);
      var img = document.getElementById('myimg' + current); //id is myimg
      img.src = url;
    }).bind(this, current)).catch(function(error) {
      // Handle any errors
    });
  }
})(jQuery); // End of use strict