!function(window, $) {
  var ids = [true, true]
  var compare_items = [] 
  var compare = {
    add_item: function(item) {
      var checked;
      if (ids[0]) {
        checked = 0
      } else if (ids[1]) {
        checked = 1
      }
      if (checked == undefined) {
        error.top_message("You can't choose any more")
        return false
      }
      compare_items[checked] = $(item)
      $(item).attr("data-compare", checked) 
      $(item).addClass("choosed")
      ids[checked] = false
      return true
    }
    , remove_item:  function(item) {
      var id =  parseInt($(item).attr("data-compare"))
      if (id != 0 && id != 1)
        return
      $(item).attr("data-compare", "")
      $(item).removeClass("choosed")
      ids[id] = true
    }
    , cancel_all: function() {
      if (!ids[0]) {
        compare.remove_item(compare_items[0])
        var item = compare_items[0]
        $(item).find(".i-choose").removeClass("choosed").find(".text").text("Choose Me")
      }
      if (!ids[1]) {
        compare.remove_item(compare_items[1])
        var item = compare_items[1]
        $(item).find(".i-choose").removeClass("choosed").find(".text").text("Choose Me")
      }
    }
    , compare: function() {
      if (ids[0] || ids[1]) {
        error.top_message("Please choose two items to compare")
        return
      }
      window.data = compare_items
      url = "/core/compare-box?c1=" + $(compare_items[0]).attr("data-id")
      url += "&c2=" + $(compare_items[1]).attr("data-id")
      $.get(url).done(function(data){
        $('body').append(data)
      })
    }
  }
  window.compare = compare
  
}(window, jQuery)

!function($) {
  function mark_item(item) {
    var has = $(item).hasClass("choosed")
    var item_wrapper = $(item).parents(".thumbnail")
    if (has) {
      compare.remove_item(item_wrapper)
      $(item).removeClass("choosed")
      $(item).find('a span.text').text("Choose Me")
    } else {
      if (compare.add_item(item_wrapper)) {
        $(item).addClass("choosed")
        $(item).find('a span.text').text("Choosed")
      }
    }
  }

  $(".thumbnail .img-link").live('click', function(e) {
    e.preventDefault()
    mark_item($(this).parents(".thumbnail").find(".i-choose"))
  })
  
  
  $(".thumbnail .i-choose").live('click', function(e) {
    e.preventDefault()
    mark_item(this)
  })

  $("#compare-item").click(function(e) {
    e.preventDefault()
    compare.compare()
  })
  $("#cancel-all").click(function(e) {
    e.preventDefault()
    compare.cancel_all()
  })
}(jQuery)

!function($, window) {
  function set_scroll_event(mtop, item) {
    $(document).scroll(function() {
      var s_top = $(this).scrollTop()
      var target = $(item)
      if (s_top > mtop) {
        if (!target.hasClass("fixed")) {
          target.addClass("fixed")
        }
      } else {
        if (target.hasClass("fixed")) {
          target.removeClass("fixed")
        }
      }
    })
  }
  window.set_scroll_event = set_scroll_event
}(jQuery, window)
