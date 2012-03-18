!function($) {
  $.get('/feedback/tool').done(function(data) {
    $('body').append(data)
  })
}(jQuery)
