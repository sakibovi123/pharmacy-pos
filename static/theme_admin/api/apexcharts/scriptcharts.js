// var options = {
//     chart: {
//         type: 'bar'
//     },
//     series: [{
//         name: 'sales',
//         data: [30, 40, 45, 50, 49, 60, 70, 91, 125]
//     }],
//     xaxis: {
//         categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
//     }
// }
// var chart = new ApexCharts(document.querySelector("#chart"), options);
// chart.render();


// var options = {
//     series: [44, 55, 41, 17, 15],
//     chart: {
//         type: 'donut',
//     },
//     responsive: [{
//         breakpoint: 480,
//         options: {
//             chart: {
//                 width: 200
//             },
//             legend: {
//                 position: 'bottom'
//             }
//         }
//     }]
// };
// var chart = new ApexCharts(document.querySelector("#chart-2"), options);
// chart.render();


var options = {
    series: [{
        name: 'series1',
        data: [31, 40, 28, 51, 42, 109, 100]
    }, {
        name: 'series2',
        data: [11, 32, 45, 32, 34, 52, 41]
    }],
    chart: {
        height: 350,
        type: 'area'
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        curve: 'smooth'
    },
    xaxis: {
        type: 'datetime',
        categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z"]
    },
    tooltip: {
        x: {
            format: 'dd/MM/yy HH:mm'
        },
    },
};
var chart = new ApexCharts(document.querySelector("#chart-3"), options);
chart.render();


var options = {
      series: [{
      name: 'Users',
      data: [4, 3, 10, 9, 29, 19, 22, 9, 12, 7, 19, 5, 13, 9, 17, 2, 7, 5]
    }],
      chart: {
      height: 350,
      type: 'line',
    },
    stroke: {
      width: 7,
      curve: 'smooth'
    },
    xaxis: {
      type: 'datetime',
      categories: ['1/11/2000', '2/11/2000', '3/11/2000', '4/11/2000', '5/11/2000', '6/11/2000', '7/11/2000', '8/11/2000', '9/11/2000', '10/11/2000', '11/11/2000', '12/11/2000', '1/11/2001', '2/11/2001', '3/11/2001','4/11/2001' ,'5/11/2001' ,'6/11/2001'],
    },
    title: {
      text: 'Daily Users',
      align: 'left',
      style: {
        fontSize: "16px",
        color: '#666'
      }
    },
    fill: {
      type: 'gradient',
      gradient: {
        shade: 'dark',
        gradientToColors: [ '#FDD835'],
        shadeIntensity: 1,
        type: 'horizontal',
        opacityFrom: 1,
        opacityTo: 1,
        stops: [0, 100, 100, 100]
      },
    },
    markers: {
      size: 4,
      colors: ["#FFA41B"],
      strokeColors: "#fff",
      strokeWidth: 2,
      hover: {
        size: 7,
      }
    },
    yaxis: {
      min: -10,
      max: 40,
      title: {
        text: 'Engagement',
      },
    }
};
var chart = new ApexCharts(document.querySelector("#chart-4"), options);
chart.render();


var options = {
    series: [70],
    chart: {
    height: 350,
    type: 'radialBar',
},
plotOptions: {
    radialBar: {
    hollow: {
        size: '70%',
    }
    },
},
labels: ['Prograss'],
};
var chart = new ApexCharts(document.querySelector("#chart-5"), options);
chart.render();