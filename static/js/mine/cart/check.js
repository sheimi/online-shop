$(document).ready(function() {
    $('.order-num').change(function() {
      var num = parseInt($(this).val())
      var item_id = parseInt($(this).attr('data-id'))
      var selected = this
      order_item.update(item_id, {num:num}).done(function(data) {
        console.log(data) 
        console.log($(selected).parents('tr'))
        var price = parseInt($(selected).parents('tr').find('.total-price').text())
        var new_price = data.num * data.price
        var total = parseInt($('.all-price').text())
        $(selected).parents('tr').find('.total-price').text(new_price)
        $('.all-price').text(total + new_price - price)
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
