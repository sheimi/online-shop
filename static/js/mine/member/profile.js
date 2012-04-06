!function($) {
  $('#img-uploader').change(function() {
    $(this).upload('/profile/img', function(data){
      var img = $("#profile-img")
      var src = img.attr('src')
      src += '?' + new Date().getTime()
      img.attr('src', src)
    }, 'html')
  })

  $("#account-submit").click(function() {
    var data = {
      username : $("#account-username").val(),
      age : $("#account-age").val(),
      gender: $("#account-gender").val(),
      email: $("#account-email").val(),
      address: $("#account-address").val()
    }
    user.update(user.id, data).done(function(data){
      success.top_message("Account Information Update Success")
    }).fail(function() {
      error.top_message("Account Information Update Fail")
    })
  })

  $("#account-delete").click(function() {
    user.delete(user.id).done(function() {
      location.href="/core/logout"
    })
  })

  $("#psw-submit").click(function() {
    var p1 = $("#psw-1").val()
    var p2 = $("#psw-2").val()
    if (p1 != p2) {
      error.top_message("password not match")
      return
    }
    if (p1 == "") {
      error.top_message("password empty")
      return
    }
    var data = {
      password: p1 
    }
    user.update(user.id, data).done(function(data) {
      success.top_message("Password Information Update Success")
    }).fail(function() {
      error.top_message("Password Information Update Fail")
    })
  })
}(jQuery)

