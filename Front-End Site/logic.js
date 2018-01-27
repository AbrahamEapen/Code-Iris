	// Width and height
    var w = 800;
    var h = 400;
    
    // Data
    var queryURL = "https://raw.githubusercontent.com/AbrahamEapen/Code-Iris/Jeff/Front-End%20Site/newDatas.json"
    //"https://raw.githubusercontent.com/AbrahamEapen/Code-Iris/master/Front-End%20Site/frontData.json"
    //var dataset = [ 5, 40 ];
    
    // Pull in the data
    d3.json(queryURL, function(error, dataset){
            console.log(dataset)
            
        
            //  console.log(x)
    // Create SVG element
    var svg = d3.select("body")
                .append("svg")
                .attr("width", w)
                .attr("height", h);



     // create the circle
    var circles = svg.selectAll("circle")
        .data(dataset)
        .text(function(d, i) {
            return d.Velocity;
        })
        .attr("class", "label")
        .enter()
        .append("circle");

    circles.attr("cx", 200)
           .attr("cy", function(d, i) {
               try {
                   return (50)
               } 
               catch (err) {
                   console.log("you have experienced an error, sir!")
               }
           })
           .attr("r", 8)
           .attr("fill", "yellow")
           .attr("stroke", "orange")
           .attr("stroke-width", function(d) {
                return d/2;
           })
           //start the animation of the circle
           .transition()
           .attr("cx", function(d, i) {
            if (d.Result === 1) {
                return (d.Range);
            } else {
                return (d.Range);
            }
           })
           //.attr("cx",700)
           .attr("cy", function(d, i) {
            if (d.Result === 1) {
                return (300 + d.Velocity);
            } else {
                return (50 + d.Angle);
            }
           })
           .attr("cy", 300)
           .duration(function(d, i) {
               return (d.Range*40)
           })
           .attrTween('width', function() {
            return d3.interpolateNumber(0, 250);
          });

           var rect = svg.selectAll("rect")
           .data(dataset)
           .enter()
           .append("rect")
           .attr("x", 700)
           .attr("y", 275)
           .attr("height", 50)
           .attr("width", 50);


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
    })
    