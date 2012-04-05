$(document).ready(function() {
    $('.order-num').change(function() {
      var num = parseInt($(this).val())
      var item_id = parseInt($(this).attr('data-id'))
      var selected = this
      order_item.update(item_id, {num:num}).done(function(data) {
        var price = parseInt($(selected).parents('tr').find('.total-price').text())
        var discount = parseInt($('.discount').text())
        var new_price = data.num * data.price
        var total = parseInt($('.all-price').text())
        var total_raw = parseInt($('.raw-price').text())
        $(selected).parents('tr').find('.total-price').text(new_price)
        $('.raw-price').text(total_raw + new_price - price)
        $('.all-price').text(total + parseInt((new_price - price) * discount / 100))
        success.top_message("Your Order has Successfully Changed")
      })
    })
    $('.close').click(function() {
      var oid = parseInt($(this).attr('data-id'))
      var selected = this
      var total = parseInt($('.all-price').text())
      var price = parseInt($(this).parent().find('.total-price').text())
      order_item.delete(oid).done(function() {
        $(selected).parents('tr').fadeOut()
        $(".all-price").text(total-price)
        success.top_message("Item Has Removed")
      })
    })
})
