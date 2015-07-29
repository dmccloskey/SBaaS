"use strict";
// TODO flip x and y, and rotate to horizontal
d3_chart2d.prototype.set_y1y2domain_horizontalbarschart = function () {
    // set y1-domain and y1-domain for a barchart
    var series_label = this.data1keymap.serieslabel;
    var nestdatafiltered = this.data1.nestdatafiltered;
    var listdatafiltered = this.data1.listdatafiltered;
    this.y1scale.domain(nestdatafiltered.map(function (d) { return d.key; }));
    var y1scale = this.y1scale;
    var series_labels_unique = this.get_uniquelabels(listdatafiltered,series_label);
    //series_labels_unique.reverse();
    this.y2scale.domain(series_labels_unique).rangeRoundBands([0,y1scale.rangeBand()]); // orders the data from bottom to top
    //this.y2scale.domain(series_labels_unique).rangeRoundBands([y1scale.rangeBand(),0]); // orders the data from top to bottom
};
d3_chart2d.prototype.add_horizontalbarsdata1 = function () {
    //add horizontal bars to the chart

    var x_data = this.data1keymap.xdata;
    var y_data = this.data1keymap.ydata;
    var series_label = this.data1keymap.serieslabel;
    var x1scale = this.x1scale;
    var y2scale = this.y2scale;
    var y1scale = this.y1scale;
    var colorscale = this.colorscale;
    var id = this.id;
    var height = this.height;
    var margintop = this.margin.top;

    this.barlabel = this.svgg.selectAll(".labels")
        .data(this.data1.nestdatafiltered)

    this.barlabel
        .transition()
        .attr("class", "labels")
        .attr("transform", function (d) {
            //return "translate(" + "0," + (height-y1scale(d.key)) + ")"; });
            //return "translate(" + "0," + (y1scale(d.key)+margintop) + ")"; });
            return "translate(" + "0," + (y1scale(d.key)) + ")"; });

    this.barlabel
        .exit().remove();

    this.barlabelenter = this.barlabel.enter().append("g")
        .attr("class", "labels")
        .attr("transform", function (d) {
            //return "translate(" + "0," + (height-y1scale(d.key)) + ")"; });
            //return "translate(" + "0," + (y1scale(d.key)+margintop) + ")"; });
            return "translate(" + "0," + (y1scale(d.key)) + ")"; });

    this.barsrect = this.barlabel.selectAll(".bars")
        .data(function (d) { return d.values; });

    this.barsrect.exit().remove();

    this.barsrect.transition()
//         .attr("width", x2scale.rangeBand())
//         .attr("x", function (d) { return x2scale(d[series_label]); })
//         .attr("y", function (d) { return y1scale(Math.max(d[y_data], 0)); })
//         .attr("height", function (d) { return Math.abs(y1scale(d[y_data]) - y1scale(0)); })
//         .style("fill", function (d) { return colorscale(d[series_label]); });
        .attr("width", function (d) { 
                return Math.abs(x1scale(d[x_data]) - x1scale(0)); })
        .attr("y", function (d) {
            //return height-y2scale(d[series_label])-y2scale.rangeBand(); })
            //return -y2scale(d[series_label])-y2scale.rangeBand(); })
            return y2scale(d[series_label]); })
        .attr("x", function (d) {
            return x1scale(Math.min(d[x_data], 0)); })
        .attr("height", y2scale.rangeBand())
        .style("fill", function (d) { 
            return colorscale(d[series_label]); });
      
    this.barsrectenter = this.barsrect.enter()
        .append("rect")
        .attr("class", "bars");

    this.barsrectenter
        .attr("width", function (d) {
            return Math.abs(x1scale(d[x_data]) - x1scale(0)); })
        .attr("y", function (d) {
            //return height-y2scale(d[series_label])-y2scale.rangeBand(); })
            //return -y2scale(d[series_label])-y2scale.rangeBand(); })
            return y2scale(d[series_label]); })
        .attr("x", function (d) {
            return x1scale(Math.min(d[x_data], 0)); })
        .attr("height", y2scale.rangeBand())
        .style("fill", function (d) {
            return colorscale(d[series_label]); });

};
d3_chart2d.prototype.add_horizontalbarsdata1tooltipandfill = function () {
    //add a tooltip upon moving the mouse over the bar
    //add a change in color upon moving the mouse over the bar
    //NOTE: both must be within the same "on" method
    var colorscale = this.colorscale;
    var series_label = this.data1keymap.serieslabel;
    var metid = this.data1keymap.featureslabel;
    var x_data = this.data1keymap.xdata;
    var x_data_lb = this.data1keymap.xdatalb;
    var x_data_ub = this.data1keymap.xdataub;
    var id = this.id;

    // set the tooltip
    this.tooltip = d3.tip().attr('class', 'd3-tip')
        .html(function(d){
            if (typeof d[x_data_lb] !== "undefined" && typeof d[x_data_ub] !== "undefined"){
                return (d[series_label] + ': ' + "value: " + d[x_data].toFixed(2) + ', ' + "95% ci: " + d[x_data_lb].toFixed(2) + "/" + d[x_data_ub].toFixed(2));
            } else {
                return (d[series_label] + ': ' + "value: " + d[x_data].toFixed(2))
            }
        })
        .style({
           'line-height': '1',
           'font-weight': 'bold',
           'padding': '12px',
           'background': 'rgba(0, 0, 0, 0.8)',
           'color': '#fff',
           'border-radius': '2px'
        });
    //this.set_d3tooltipstyle(); //not functional
    this.svgg.call(this.tooltip);
    var tip = this.tooltip;

    this.barsrectenter.on("mouseover", function (d) {
            //change color of the bar
            d3.select(this).style('fill', 'black');
            //show the tooltip
            tip.show(d);
        })
        .on("mouseout", function (d) {
            d3.select(this).style("fill", colorscale(d[series_label]));
            tip.hide(d);
        });
};
d3_chart2d.prototype.add_horizontalbarsdata1errorbars = function () {
    //add horizontal error bars to the chart
    //TODO: need to test correct positioning of error bars
    if (typeof this.data1keymap.xdatalb !== "undefined" && typeof this.data1keymap.xdatalb !== "undefined"){
        var x_data_lb = this.data1keymap.xdatalb;
        var x_data_ub = this.data1keymap.xdataub;
    } else {
        // do not attempt to draw error bars if there are no lb/ub
        return;
    };
    var x_data = this.data1keymap.xdata;
    var y_data = this.data1keymap.ydata;
    var series_label = this.data1keymap.serieslabel;
    var x1scale = this.x1scale;
    var y2scale = this.y2scale;
    var y1scale = this.y1scale;
    var colorscale = this.colorscale;
    var id = this.id;
    var height = this.height;

    //upperbounds: the horizontal lines representing the uppoer bounds of the confidence intervals.
    this.barsublines = this.barlabel.selectAll(".ublines")
        .data(function (d) { return d.values; });

    this.barsublines.exit().remove();

    this.barsublines.transition()
//         .attr("x1", function (d) { return x2scale(d[series_label]); })
//         .attr("x2", function (d) { return x2scale(d[series_label]) + x2scale.rangeBand(); })
//         .attr("y1", function (d) { return y1scale(d[y_data_ub]); })
//         .attr("y2", function (d) { return y1scale(d[y_data_ub]); })
        .attr("y1", function (d) { return y2scale(d[series_label]); })
        .attr("y2", function (d) { return y2scale(d[series_label]) + y2scale.rangeBand(); })
//         .attr("y1", function (d) { return height-y2scale(d[series_label]); })
//         .attr("y2", function (d) { return height-y2scale(d[series_label]) - y2scale.rangeBand(); })
        .attr("x1", function (d) { return x1scale(d[x_data_ub]); })
        .attr("x2", function (d) { return x1scale(d[x_data_ub]); })
        //.style("stroke", function (d) { return colorscale(d[series_label]); });
        .style("stroke","black");
      
    this.barsublinesenter = this.barsublines.enter()
        .append("line")
        .attr("class", "ublines");

    this.barsublinesenter
        .attr("y1", function (d) { return y2scale(d[series_label]); })
        .attr("y2", function (d) { return y2scale(d[series_label]) + y2scale.rangeBand(); })
        .attr("x1", function (d) { return x1scale(d[x_data_ub]); })
        .attr("x2", function (d) { return x1scale(d[x_data_ub]); })
        //.style("stroke", function (d) { return colorscale(d[series_label]); });
        .style("stroke","black")
        .style("stroke-width", function (d) {
            if (d[x_data] == 0.0) { return 0; 
            } else { return 1; } 
        });
        
    //lowerbound: the horizontal lines representing the lowerbound of the confidence intervals.
    this.barslblines = this.barlabel.selectAll(".lblines")
        .data(function (d) { return d.values; });

    this.barslblines.exit().remove();

    this.barslblines.transition()
//         .attr("x1", function (d) { return x2scale(d[series_label]); })
//         .attr("x2", function (d) { return x2scale(d[series_label]) + x2scale.rangeBand(); })
//         .attr("y1", function (d) { return y1scale(d[y_data_lb]); })
//         .attr("y2", function (d) { return y1scale(d[y_data_lb]); })
        .attr("y1", function (d) { return y2scale(d[series_label]); })
        .attr("y2", function (d) { return y2scale(d[series_label]) + y2scale.rangeBand(); })
//         .attr("y1", function (d) { return height-y2scale(d[series_label]); })
//         .attr("y2", function (d) { return height-y2scale(d[series_label]) - y2scale.rangeBand(); })
        .attr("x1", function (d) { return x1scale(d[x_data_lb]); })
        .attr("x2", function (d) { return x1scale(d[x_data_lb]); })
        //.style("stroke", function (d) { return colorscale(d[series_label]); });
        .style("stroke","black")
        .style("stroke-width", function (d) {
            if (d[x_data] == 0.0) { return 0; 
            } else { return 1; } 
        });
      
    this.barslblinesenter = this.barslblines.enter()
        .append("line")
        .attr("class", "lblines");

    this.barslblinesenter
        .attr("y1", function (d) { return y2scale(d[series_label]); })
        .attr("y2", function (d) { return y2scale(d[series_label]) + y2scale.rangeBand(); })
        .attr("x1", function (d) { return x1scale(d[x_data_lb]); })
        .attr("x2", function (d) { return x1scale(d[x_data_lb]); })
        //.style("stroke", function (d) { return colorscale(d[series_label]); });
        .style("stroke","black")
        .style("stroke-width", function (d) {
            if (d[x_data] == 0.0) { return 0; 
            } else { return 1; } 
        });
        
    //connector: the horizontal line connecting the confidence intervals.
    this.barslbubconnector = this.barlabel.selectAll(".lbubconnector")
        .data(function (d) { return d.values; });

    this.barslbubconnector.exit().remove();

    this.barslbubconnector.transition()
//         .attr("x1", function (d) { return x2scale(d[series_label]) + x2scale.rangeBand()*0.5; })
//         .attr("x2", function (d) { return x2scale(d[series_label]) + x2scale.rangeBand()*0.5; })
//         .attr("y1", function (d) { return y1scale(d[y_data_lb]); })
//         .attr("y2", function (d) { return y1scale(d[y_data_ub]); })
        .attr("y1", function (d) { return y2scale(d[series_label]) + y2scale.rangeBand()*0.5; })
        .attr("y2", function (d) { return y2scale(d[series_label]) + y2scale.rangeBand()*0.5; })
//         .attr("y1", function (d) { return height-y2scale(d[series_label]) - y2scale.rangeBand()*0.5; })
//         .attr("y2", function (d) { return height-y2scale(d[series_label]) - y2scale.rangeBand()*0.5; })
        .attr("x1", function (d) { return x1scale(d[x_data_lb]); })
        .attr("x2", function (d) { return x1scale(d[x_data_ub]); })
        //.style("stroke", function (d) { return colorscale(d[series_label]); });
        .style("stroke","black")
        .style("stroke-width", function (d) {
            if (d[x_data] == 0.0) { return 0; 
            } else { return 1; } 
        });
      
    this.barslbubconnectorenter = this.barslbubconnector.enter()
        .append("line")
        .attr("class", "lbubconnector");

    this.barslbubconnectorenter
        .attr("y1", function (d) { return y2scale(d[series_label]) + y2scale.rangeBand()*0.5; })
        .attr("y2", function (d) { return y2scale(d[series_label]) + y2scale.rangeBand()*0.5; })
        .attr("x1", function (d) { return x1scale(d[x_data_lb]); })
        .attr("x2", function (d) { return x1scale(d[x_data_ub]); })
        //.style("stroke", function (d) { return colorscale(d[series_label]); });
        .style("stroke","black")
        .style("stroke-width", function (d) {
            if (d[x_data] == 0.0) { return 0; 
            } else { return 1; } 
        });

};
d3_chart2d.prototype.set_x1andy1axesstyle_horizontalbarschart = function () {
    // predefined css style for x1 and y1 axis
    var x1axisselector = '#' + this.id + 'x1axis' + ' path';
    var y1axisselector = '#' + this.id + 'y1axis' + ' path';
    var y1axisstyle = {
        'fill': 'none', 'display':'none'
    };
    var x1axisstyle = {
        'fill': 'none', 'stroke': '#000',
        'shape-rendering': 'crispEdges',
        'stroke-width': '1.5px'
    };
    var selectorstyle = [{ 'selection': x1axisselector, 'style': x1axisstyle },
                     { 'selection': y1axisselector, 'style': y1axisstyle }]
    this.set_svggcss(selectorstyle);
};