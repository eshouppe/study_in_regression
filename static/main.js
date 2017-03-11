$.ajax({url: "/barChartData", success: function(result){
    var data = {
        labels: result.labels,
        series: result.series
    };
    var options = {
        high: 25,
        low: 0
    };
    new Chartist.Bar('.ct-chart', data, options);
}});
