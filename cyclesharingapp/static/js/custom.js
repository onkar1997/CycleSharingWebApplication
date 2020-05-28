// scroll to top
$(document).ready(function () {
  $(window).scroll(function () {
    if ($(this).scrollTop() > 150) {
      $("#scroll-to-top").fadeIn();
    } else {
      $("#scroll-to-top").fadeOut();
    }
  });

  // Adding scoll-to-top animation
  $("#scroll-to-top").click(function () {
    $("html,body").animate({ scrollTop: 0 }, 1000);
  });
});
