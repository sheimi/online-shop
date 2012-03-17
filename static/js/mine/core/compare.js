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
