$(document).ready(function() {
    var chart = new Highcharts.Chart({
      chart: {
        renderTo: 'chart-container',
        defaultSeriersType: 'line',
        backgroundColor: null,
        marginRight: 130,
        marginBottom: 25
        },
      title: {
        text: 'General Chart',
        x: -20
        },
      xAxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        },
      yAxis: {
        title: { text: 'income'},
        plotLines: [{
          value: 0,
          width: 1,
          color: '#808080'
        }]
         },
      legend: {
          layout: 'vertical',
          align: 'right',
          verticalAlign: 'top',
          x: -10,
          y: 100,
          borderWidth: 0
              },
      tooltip: {
          formatter: function() {
              return '<b>'+ this.series.name +'</b><br/>'+
                          this.x +':  $'+ this.y;
            }
          },
    series: [{
              name: 'General',
              data: [100, 200, 200 ,100, 49, 100, 100,20, 100, 100, 19, 487],
              marker: {symbol: 'square'}
            }]
  })
})
