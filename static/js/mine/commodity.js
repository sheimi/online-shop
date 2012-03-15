!function(window) {
  urls = {
    add_item: '/cart/additem'
  }
  window.add_to_cart = function(commodity_id, callback) {
    if (user.id == undefined) {
      error.top_message("Please Login First")
      return
    }
    num = $(".order-num").val()
    if (num == "" || num == "0") {
      error.top_message("Please Input The Number")
      return
    }
    $(".order-num").val("")
    var commit = {
      num: parseInt(num),
      order: order.id,
      commodity: commodity_id
    }
    var done = send_json({url: urls.add_item, method: "POST", data: commit}).done(function(data) {
      success.top_message("Item Has Add To Your Cart")
      refresh_item('cart')
    })
    if (callback)
      callback()
  }
}(window)
