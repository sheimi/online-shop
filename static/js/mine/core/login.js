$(document).ready(function() {
  var login_url = '/core/login' 
  var account_url = '/core/account'
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
      url: login_url,
      method: 'POST',
      data : {
        username : username,
        password : password
      }
    }).done(function(data) {
      if (data.success) {
        $('ul#top-account-info').load(account_url)
      } else {
        error.top_message(data.msg)
      }
    })
  })
})
