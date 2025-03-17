/*!
 * Main web js
 */

// import { ar } from 'date-fns/locale';

// variables
const web = window.web || {};
// const dataLayer = window.dataLayer || [];
// const ar = window.ar || {};
// window.bootstrap = bootstrap;
// const bootstrap = window.bootstrap || {};

// functions

function scrollToSection($, id) {
  var targetSec = $('.block-item[data-section="' + id + '"]');
  if (targetSec.length) {
    var offset = targetSec.offset();
    $("html,body").animate(
      {
        scrollTop:
          offset.top - ($(".main-nav").length ? $(".main-nav").height() : 0),
      },
      800,
      function () {
        //
      }
    );
  }
}

function highlightCurrentMenuItem() {
  const menu = document.getElementById("main-nav-menu");
  const menuItems = menu.querySelectorAll(".nav-item");
  const currentMenuItem =
    (window.location.hash &&
      menu.querySelector(`.nav-link[href="/${window.location.hash}"]`)) ||
    menu.querySelector(`.nav-link[href="${window.location.pathname}"]`);
  for (let i = 0; i < menuItems.length; i++) {
    menuItems[i].classList.remove("current");
  }
  if (currentMenuItem) {
    currentMenuItem.closest(".nav-item").classList.add("current");
  }
}

// function getnavposition($) {
//   var pagePositionUrl;
//   var scrollp = $(window).scrollTop();
//   $(".block-item").each(function (index) {
//     var offset = $(this).offset();
//     var blockStart = offset.top - 200;
//     var blockEnd = blockStart + $(this).height();

//     var elemID = $(this).attr("data-section");
//     if (typeof elemID !== "undefined") {
//       var menuelem = $('#main-nav-menu .nav-link[href$="#' + elemID + '"]');
//       if (scrollp >= blockStart && scrollp < blockEnd) {
//         menuelem.closest(".nav-item").addClass("current");
//         if (pagePositionUrl !== elemID) {
//           pagePositionUrl = elemID;
//         }
//       } else {
//         menuelem.closest(".nav-item").removeClass("current");
//       }
//     }
//   });
//   if (pagePositionUrl && document.location == "/") {
//     document.location.hash = pagePositionUrl;
//   }
// }

function mainNavigationPosition() {
  var html = $("html");
  var windowScroll = html[0].scrollTop;
  var navigationSticky = $("#top-navigation-wrapper.sticky");

  if (windowScroll > 0) {
    html.addClass("top-navigation-sticked");
    navigationSticky.addClass("sticked");
  } else {
    html.removeClass("top-navigation-sticked");
    navigationSticky.removeClass("sticked");
  }
}

function testValidEmail(email) {
  return /^[a-z_0-9.+-]+?@[a-z_0-9.-]+?\.[a-z_0-9.-]+?$/i.test(email);
}

function testIfEmpty(s) {
  return /^\s*$/i.test(s) || s === "";
}

// lazyload
function lazyloadImages() {
  var lazyloadImagesList = $("img[data-src]");
  if (lazyloadImagesList.length) {
    var scrollTop = $(document).scrollTop();
    var viewPortH = window.innerHeight;
    lazyloadImagesList.each(function (i) {
      var t = $(this);
      var tTop = t.offset().top;
      if (tTop < scrollTop + viewPortH + 50) {
        t.attr("src", t.attr("data-src")).attr("data-src", null);
      }
    });
  }
}

// document ready
$(function () {
  highlightCurrentMenuItem();

  // variables
  web.pageRollUp = $(".page-roll-up");

  // functions
  web.pageRollUpToggle = function () {
    if ($(window).scrollTop() > 500) {
      this.pageRollUp.addClass("show");
    } else {
      this.pageRollUp.removeClass("show");
    }
  }; /**/

  mainNavigationPosition();
  lazyloadImages();

  // $(".main-navbar .nav-link, .nav-link").click(function (e) {
  //   $("#main-nav-menu").collapse("hide");
  //   $("#main-nav-menu-drawer .btn-close").click();

  //   var t = $(this);
  //   var href = t.attr("href");
  //   var tUrl = new URL(href, window.location);
  //   var hrefUrl = tUrl.origin + tUrl.pathname;

  //   setTimeout(function () {
  //     var pageUrl = window.location.origin + window.location.pathname;

  //     if (hrefUrl === pageUrl && window.location.hash !== "") {
  //       var blockId = window.location.hash.slice(1);
  //       scrollToSection($, blockId);
  //     }
  //   }, 200);
  // });

  // $(window).scroll(function () {
  //   getnavposition($);
  // });

  // if (window.location.hash !== "") {
  //   var blockId = window.location.hash.slice(1);
  //   setTimeout(function () {
  //     scrollToSection($, blockId);
  //   }, 1000);
  // }

  web.pageRollUp.click(function () {
    $("html, body").stop().animate(
      {
        scrollTop: 0,
      },
      800
    );
  });

  web.windowResize = function () {
    // $('.contact-map').height($(window).height() - $('.page-navigation').height());
  };

  $(".block-gallery a, .lightbox").simpleLightbox({
    overlay: true,
    overlayOpacity: 0.8,
    spinner: true,
    nav: true,
  });

  $('[data-bs-toggle="tooltip"]').tooltip();

  $(window).scroll(); // initial scroll call

  window.addEventListener("hashchange", function () {
    highlightCurrentMenuItem();
  });

  // on scroll actions
  $(window).scroll(function () {
    // web.pageRollUpToggle();
    lazyloadImages();

    mainNavigationPosition();
  });

  // on resize actions
  web.windowResize();
  $(window).resize(function () {
    web.windowResize();
  });

  $("body").on("click", ".infotoggle-list .infotoggle-list-item", function () {
    let that = $(this);
    // console.log(that.data('toggleinfo-target'));

    const toggleList = $(".infotoggle-list");
    const toggleListItems = $(".infotoggle-list .infotoggle-list-item");
    const toggleListItemActive = toggleList.find(
      ".infotoggle-list-item.active, .infotoggle-list-item.initialActive"
    );
    const contentInfo = $(".infotoggle-content");
    const contentItems = contentInfo.find(".infotoggle-content-item");
    // const contetnItemsInfo = contentItems.find(".infotoggle-list-item-info");
    const contentItemActivating = contentInfo.find(
      ".infotoggle-content-item.activating"
    );
    const contetnItemActive = contentInfo.find(
      ".infotoggle-content-item.active"
    );
    const contentItemToggle = contentItems[that.data("toggleinfo-target")];

    if (
      !contentItemToggle ||
      !!contentItemActivating.length ||
      that[0] === toggleListItemActive[0] ||
      (!contentItems.length &&
        contentItems[that.data("toggleinfo-target")] &&
        contetnItemActive[0] === contentItemToggle)
    ) {
      return;
    }

    toggleListItems.removeClass("active");
    contentItems.removeClass("active");
    toggleListItems.find(".infotoggle-list-item-info").slideUp(500);
    $(contentItemToggle).addClass("activating");

    that.find(".infotoggle-list-item-info").slideDown(500);

    $(contentItemToggle).fadeIn(500, function () {
      toggleListItems.removeClass("initialActive");
      $(contentItemToggle).addClass("active");
      contentItems.removeClass("activating");
      contentItems.attr("style", null);
    });

    that.addClass("active");
  });
});

// // cookies consent management --------------
// ar.docReady(function () {
//   ar.cookiesConsent();
// });
