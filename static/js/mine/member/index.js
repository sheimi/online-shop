!function($) {
  url = {
    account: '/member/account',
    order: '/member/orders'
  }
  $("#member-account-pill").click(function(data) {
    if (!$(this).hasClass("active")) {
      $(this).addClass("active")
      $("#member-order-pill").removeClass("active")
      $("#member-orders").fadeOut(function() {
        $("#member-account").fadeIn()
      })
    }
  })

  $("#member-order-pill").click(function(data) {
    if (!$(this).hasClass("active")) {
      $(this).addClass("active")
      $("#member-account-pill").removeClass("active")
      $("#member-account").fadeOut(function() {
        $("#member-orders").fadeIn()
      })
    }
  })

  $("#member-orders").hide()
  $("#member-account").load(url.account)
  $("#member-orders").load(url.order)

}(jQuery)
