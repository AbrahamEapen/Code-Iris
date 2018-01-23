	//Width and height
    var w = 800;
    var h = 500;
    
    //Data
    var dataset = [ 5, 40 ];
    
    //Create SVG element
    var svg = d3.select("body")
                .append("svg")
                .attr("width", w)
                .attr("height", h);
//create the circle
    var circles = svg.selectAll("circle")
        .data(dataset)
        .enter()
        .append("circle");

    circles.attr("cx", 50)
           .attr("cy", 300)
           .attr("r", function(d) {
                return d;
           })
           .attr("fill", "yellow")
           .attr("stroke", "orange")
           .attr("stroke-width", function(d) {
                return d/2;
           })
           //start the animation of the circle
           .transition()
           .attr("cx",700)
           
           .attr("cy", 300)
           .duration(2000).attrTween('width', function() {
            return d3.interpolateNumber(0, 250);
          });

           var rect = svg.selectAll("rect")
           .data(dataset)
           .enter()
           .append("rect")
           .attr("x", 700)
           .attr("y", 300)
           .attr("height", 100)
           .attr("width", 100);


           //path
           // Create an arc generator with configuration
var arcGenerator = d3.arc();

// Generate the path string
var pathData = arcGenerator({
  startAngle: 0,
  endAngle: 0.25 * Math.PI,
  innerRadius: 50,
  outerRadius: 100
});

// Create a path element and set its d attribute
d3.select('g')
	.append('path')
	.attr('d', pathData);

    