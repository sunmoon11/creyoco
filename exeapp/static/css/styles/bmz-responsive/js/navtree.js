// Generated by CoffeeScript 1.4.0
(function() {

  $(function() {
    var active, hide, lastTimeout, left, narrow, show, update, wide;
    show = function(el) {
      return el.addClass("navshown").removeClass("navhidden");
    };
    hide = function(el) {
      return el.removeClass("navshown").addClass("navhidden");
    };
    lastTimeout = void 0;
    update = function() {
      clearTimeout(lastTimeout);
      return lastTimeout = setTimeout((function() {
        $(".navshown").slideDown();
        return $(".navhidden:not(.neverhide)").slideUp();
      }), 200);
    };
    left = $("aside.left > nav");
    hide(left.find("ul > li > ul").hide());
    active = left.find(".active").parent();
    active.show().addClass("neverhide");
    active.find("> li, > ul").show().addClass("neverhide");
    active.parents("ul").show().addClass("neverhide");
    narrow = function() {
      var a_list, menu_toggle;
      left.find("li").off();
      left.find();
      a_list = $(".left").find("ul").not(".neverhide").parent().children("a");
      a_list.each(function() {
        var a, url_text;
        a = $(this);
        url_text = a.html();
        if (url_text.indexOf("</span>") === -1) {
          a.html(url_text + '<span class=\'glyphicon glyphicon-chevron-down\'></span>');
        }
      });
      $('.left .glyphicon').off('click');
      $('.left .glyphicon').on('click', function(e) {
        var parent;
        e.preventDefault();
        if ($(this).hasClass('glyphicon-chevron-down')) {
          $(this).removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
          parent = $(this).parent().parent();
          show(parent.find("> ul"));
          show(parent.parents("ul"));
          return update();
        } else if ($(this).hasClass('glyphicon-chevron-up')) {
          $(this).removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
          parent = $(this).parent().parent();
          hide(parent.find("> ul"));
          return update();
        }
      });
      menu_toggle = $('#menu-toggle');
      menu_toggle.off();
      return menu_toggle.click(function(e) {
        e.preventDefault();
        $('body').toggleClass('active');
      });
    };
    wide = function() {
      left.find("span.glyphicon").remove();
      left.find("li").on("mouseover", function(ev) {
        show($(this).find("> ul"));
        show($(this).parents("ul"));
        return update();
      });
      return left.find("li").on("mouseout", function(ev) {
        hide($(this).find("> ul"));
        return update();
      });
    };
    $(window).on('resize', function() {
      if ($(this).width() > 1200) {
        return wide();
      } else {
        return narrow();
      }
    });
    if ($(window).width() > 1200) {
      wide();
    } else {
      narrow();
    }
    window.scrollTo(0, 0);
    $('header').affix();
    $(window).on('scroll', function() {
      $('header').affix('checkPosition');
      $('.left').affix('checkPosition');
      $('.rightimages').affix('checkPosition');
    });
    $('header')
      .on('affixed.bs.affix', function() {
        $('header').data('affixed', true);
        $('.middle').addClass('withAffix');
      })
      .on('affix.bs.affix affix-top.bs.affix', function(evt) {
        if (evt.type === 'affix') {

          $(this).addClass('affix');
        } else {
          $(this).removeClass('affix');
        }
        if ($(window).height() >= $(document).height()) {
          $(this)
              .addClass('affix-static')
              .removeClass('affix');
        }
        evt.preventDefault();
        evt.stopPropagation();
      });

    $('.left').affix();
    $('.rightimages').affix();

  });

}).call();
