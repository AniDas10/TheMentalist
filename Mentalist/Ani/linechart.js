
{% block extrajs %}

<script src="https://cdn.jsdelivr.net/npm/apexcharts"> </script>
<script type='text/javascript'>
    var options = {
        chart: {
            height: 350,
            type: 'bar',
        },
        colors:['#fd7e14'],
        plotOptions: {
            bar: {
                dataLabels: {
                    position: 'top', // top, center, bottom
                },
            }
        },
        dataLabels: {
            enabled: false,
        },
        series: [{
            name: 'Score',
            data: {{graph_data}},
        }],
        xaxis: {
            position: 'top',
            labels: {
                offsetY: -18,
                formatter: function (val) {
                    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
                    return months[val-1];
                }
            },
            axisBorder: {
                show: false
            },
            axisTicks: {
                show: false
            },
            crosshairs: {
                fill: {
                    type: 'gradient',
                    gradient: {
                        colorFrom: '#FD7E14',
                        colorTo: ' #6610f2;',
                        stops: [0, 100],
                        opacityFrom: 0.7,
                        opacityTo: 1,
                    }
                }
            },
            tooltip: {
                enabled: true,
                offsetY: -35,

            }
        },
        fill: {
            gradient: {
                shade: 'light',
                type: "horizontal",
                shadeIntensity: 0.25,
                gradientToColors: undefined,
                inverseColors: true,
                opacityFrom: 1,
                opacityTo: 1,
                stops: [50, 0, 100, 100]
            },
        },
        yaxis: {
            axisBorder: {
                show: false
            },
            axisTicks: {
                show: false,
            },
            max: 5,
            labels: {
                show: false,
                formatter: function (val) {
                    return val;
                }
            }

        },
        title: {
            text: 'Best months to visit ' + '{{city}}',
            floating: true,
            offsetY: 320,
            align: 'center',
            style: {
                color: '#444'
            }
        },
    }

    var chart = new ApexCharts(
        document.querySelector("#chart"),
        options
    );

    chart.render();

</script>

{% endblock %}