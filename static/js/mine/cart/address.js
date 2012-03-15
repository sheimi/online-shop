$(document).ready(function() {
  $("#address-submit").click(function(e) {
    e.preventDefault()
    var nname = $("#new-name").val()
    var naddress = $("#new-address").val()
    var nzipcode = $("#new-zipcode").val()
    var nphone = $("#new-phone").val()
    if (nname == "" || naddress=="" || nzipcode=="" || nphone=="") {
      error.top_message("Please Fill The Form First")
      return
    }
    data = {
      user: user.id,
      name: nname,
      zipcode: nzipcode,
      address: naddress,
      phone: nphone
    } 
    var url = $(this).attr("href")
    address.create(data).done(function(data) {
      order.update(order.id, {address:data.id}).done(function() {
        window.location.href = url
      })
    })
  })
  $(".address-update").click(function(e) {
    e.preventDefault()
    var id = $(this).attr("data-id")
    var nname = $("#name-"+id).val()
    var naddress = $("#address-"+id).val()
    var nzipcode = $("#zipcode-"+id).val()
    var nphone = $("#phone-"+id).val()
    if (nname == "" || naddress=="" || nzipcode=="" || nphone=="") {
      error.top_message("Please Fill The Form First")
      return
    }
    data = {
      user: user.id,
      name: nname,
      zipcode: nzipcode,
      address: naddress,
      phone: nphone
    } 
    var url = $(this).attr("href")
    address.update(parseInt(id), data).done(function() {
      order.update(order.id, {address:id}).done(function() {
        window.location.href = url
      })
    })
  })
  $(".address-delete").click(function(e) {
    var id = $(this).attr("data-id")
    $("#address-item-"+id).fadeOut(function(){
      address.delete(parseInt(id))
    }).remove()
  })
})
