$(document).ready(function() {

  url = {
    commodies: '/admina/commodity-list'
  }

  $("#categories").jstree({
    themes : {
      theme : "apple"
      , icons : false
    }
    , dnd : {
      drag_finish: function(data) {
                     window.data = data
                      var co_id = parseInt($(data.o).attr("data-id"))
                      var p_id = parseInt(data.r.attr("data-id"))
                      commodity.update(co_id, {category: p_id}).done(function(data) {
                        success.top_message("Commodity Category Successfully Updated")
                      })
                   }
    }
    , plugins : ["ui", "themes", "crrm", "contextmenu", "html_data", "dnd"]
  }).bind("select_node.jstree", function (event, data) {
    var obj = parseInt(data.rslt.obj.attr("data-id"))
    $("#commodities").load(url.commodies+"?category=" + obj)
  }).bind("rename.jstree", function(event, data) {
    var obj = data.rslt.obj
    var id = parseInt(obj.attr("data-id"))
    var text = obj.text().trim()
    category.update(id, {name: text}).done(function() {
      success.top_message("Category Successfully Updated")
    })
  }).bind("create.jstree", function(event, data) {
    var obj = data.rslt.obj
    var p_id = parseInt(data.rslt.parent.attr("data-id"))
    var text = obj.text().trim()
    category.create({name:text, parent: p_id}).done(function(data) {
      obj.attr("data-id", data.id) 
      success.top_message("Category Successfully Created")
    })
  }).bind("remove.jstree", function(event, data) {
    var p_id = parseInt(data.rslt.obj.attr("data-id"))
    category.delete(p_id).done(function(data) {
      success.top_message("Category Successfully Deleted")
    })
  }).bind("move_node.jstree", function(event, data) {
    var np_id = parseInt(data.rslt.np.attr("data-id"))
    var o_id = parseInt(data.rslt.o.attr("data-id"))
    category.update(o_id, {parent: np_id}).done(function() {
      success.top_message("Category Successfully Updated")
    })
  })
})

