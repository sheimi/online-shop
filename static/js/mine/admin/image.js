$(document).ready(function() {
  /*
  $(".caption").hide()
  $(".img_wrapper").hover(function() {
    $(this).find(".caption").slideDown()
  }, function() {
    $(this).find(".caption").slideUp()
  })
  */
  $('.delete-img').live('click', function(e) {
    e.preventDefault()
    var url = $(this).attr('href')
    var id = $(this).attr('data-id')
    var wrapper = $(this).parents('.img_wrapper')
    send_json({url: url, method: 'DELETE', data: {id:id}}).done(function(data) {
      success.top_message("Delete Success")
      wrapper.fadeOut(function() {
        $(this).remove()
      })
    })
  })

  $('#img-uploader').change(function() {
    var url = $(this).attr('data-url')
    $(this).upload(url, function(data){
      console.log(data)
      window.data = data
      json = JSON.parse($(data).text())
      /*
      var img = $("#profile-img")
      var src = img.attr('src')
      src += '?' + new Date().getTime()
      img.attr('src', src)
      */
      node = '<li class="span3 img_wrapper">'
              + '<div class="thumbnail">'
              + '<a href="#">'
              +   '<img src="' + json.url + '">'
              + '</a>'
              + '<div class="caption row">'
              + '<a class="btn btn-danger delete-img span8" data-id="'+json.img_id+'" href="/admina/images/delete">'
              + '<i class="icon-trash icon-white"></i>Delete</a></div></div></li>'
      console.log(node)
      $(node).hide().appendTo(".thumbnails").fadeIn()
    }, 'html')
  })


})

