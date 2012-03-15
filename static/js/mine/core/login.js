$(document).ready(function() {
  var url = {
    login: '/core/login',
    account: '/core/account',
    admin: '/admin'
  }
  !function($) {
    var out = true;
    $('#login-toggle').click(function() {
      if (out) {
        $('#login-dropdown').fadeIn();
      } else {
        $('#login-dropdown').fadeOut();
      }
      out = !out  
    })
  }($)
  $('#login-submit').click(function() {
    var username = $("#id_username").val()
    var password = $("#id_password").val()
    if (username == "") { 
      return
    } 
    if (password == "") {
      return
    }
    send_json({
      url: url.login,
      method: 'POST',
      data : {
        username : username,
        password : password
      }
    }).done(function(data) {
      if (data.success) {
        if (data.is_admin) {
          window.location.href = url.admin
        } else {
          $('ul#top-account-info').load(url.account)
        }
      } else {
        error.top_message(data.msg)
      }
    })
  })
})
