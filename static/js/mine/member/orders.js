!function($) {
  var date = new Date
  date = date.getFullYear() + '-' + date.getMonth() + '-' + date.getDate()
        + " " + date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds()
  $(".complete-order").click(function() {
    var id = parseInt($(this).attr("data-id"))
    var select = this
    order.update(id, {is_complete:true, status: 4, complete_date: date}).done(function() {
      $(select).parents(".operations").fadeOut()
    })
  })
  $(".cancel-order").click(function() {
    var id = parseInt($(this).attr("data-id"))
    var select = this
    order.update(id, {is_complete:true, status: 5, complete_date: date}).done(function() {
      $(select).parents(".operations").fadeOut()
    })
  })
}(jQuery)
