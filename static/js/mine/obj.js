/*
 * dependency: core.js
 */
!function(window) {

/*
 * para need:
 * url
 * data
 * method
 */
function send_json(para) {
  return $.ajax({
    url: para.url,
    contentType: 'application/json',
    data: JSON.stringify(para.data),
    dataType: 'json',
    type: para.method
  })
}

function rest_creator(obj) {
  return function() {
    var url = '/api/'+ obj + '/'
    this.get = function(obj_id) {
      var t = send_json({
        url: url + obj_id + '/' ,
        method: 'GET'
      })
      return t
    }
    this.update = function(obj_id, data) {
      var t = send_json({
        url: url + obj_id + '/' ,
        method: 'PUT',
        data: data
      })
      return t
    }
    this.delete = function(obj_id) {
      var t = send_json({
        url: url + obj_id + '/' ,
        method: 'DELETE'
      })
      return t
    }
    this.create = function(data) {
      var t = send_json({
        url: url,
        method: 'POST',
        data: data
      })
      return t
    }
  }
}

var user = new (rest_creator('user'))()
var order = new (rest_creator('userorder'))()
var order_item = new (rest_creator('orderitem'))()
var commodity = new (rest_creator('commodity'))()
var category = new (rest_creator('category'))()
var member = new (rest_creator('member'))()
var comment = new (rest_creator('commoditycomment'))()


window.send_json = send_json
window.user = user
window.order = order
window.comment = comment
window.order_item = order_item

}(window);
