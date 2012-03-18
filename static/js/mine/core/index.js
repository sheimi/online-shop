!function($) {
  url = {
    recommend: '/core/recommend',
    get_hot: '/core/get-hot',
    get_new: '/core/get-new',
    get_result: '/core/result?q='
  }
  $("#recommend").load(url.recommend)
  $("#the-hostest").load(url.get_hot)
  $("#new-stuff").load(url.get_new)
  function start_query() {
    var query = $("#search-commodity-input").val()
    window.location.href = url.get_result + query
  }
  $("#search-commodity-input").keydown(function(e) {
    if (e.keyCode == 13) {
      start_query()
    }
  })
  $("#search-commodity-btn").click(start_query)
}(jQuery)
