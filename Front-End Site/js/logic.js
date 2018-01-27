var slider = document.getElementById("myRange");
var output = document.getElementById("rangeValue");
output.innerHTML = slider.value; // Display the default slider value

    //Variable to store slider value for distance
    var userDistance = output.innerHTML;

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    userDistance = output.innerHTML = this.value;
}
    
    
    
    // Width and height
    var w = 800;
    var h = 400;
    
    // Data
    var queryURL = "https://raw.githubusercontent.com/AbrahamEapen/Code-Iris/Jeff/Front-End%20Site/NewDatas2.json"
   
    //var queryURL = "/practice/json.json"
    // Pull in the data
    d3.json(queryURL, function(error, dataset){
            console.log(dataset)
            
    //  console.log(x)
    // Create SVG element
    var svg = d3.select("#fireballCanvas")
                .append("svg")
                .attr("width", w)
                .attr("height", h);

//                  d3.select('#fireballCanvas')
//                 //  .append('svg')
//                 //  .attr({
//                 //     width: 300,
//                 //     height: 300,
//                 //     border: '1px solid #ccc'
//                 //   });
//             append('svg:image')
// .attr({
//   'xlink:href': 'ryu.png',  // can also add svg file here
//   x: 20,
//   y: 20,
//   width: 225,
//   height: 225
// }).enter();



     // create the circle
    var circles = svg.selectAll("circle")
        .data(dataset)
        .text(function(d, i) {
            return d.Velocity;
        })
        .attr("class", "label")
        .enter()
        .append("circle");

    circles.attr("cx", 400)
           .attr("cy", function(d, i) {
               try {
                   return (50)
               } 
               catch (err) {
                   console.log("you have experienced an error, sir!")
               }
           })
            .attr("r",10)// function(d, i){
        //     if (d.Result === 1) {
        //         return 20;
        //     }
        //     else{
        //         return 8;
        //     }})


           //start the animation of the circle
           d3.select("#Start")
           .on("click", function() {
               d3.selectAll("circle")
           .transition()
           .attr("cx", function(d, i) {
            if (d.Result === 1) {
                return (d.Range);
            } else {
                return (d.Range);
            }
           })

            //Color of the fireballs
            .attr("fill", function(d, i){
                console.log(userDistance);
                console.log(Math.round(d.Range));
                if ( Math.abs((Math.round(d.Range) - userDistance)) < 40 ) {
                    return "red";
                }
                else{
                    return "yellow"
                }})
            .attr("stroke", "orange")
            .attr("stroke-width", function(d) {
                 return d/2;
            })
            .attr("opacity", 0.75)
           
           .attr("cy", function(d, i) {
            if (d.Result === 1) {
                return (300 + d.Velocity);
            } else {
                return (50 + d.Angle);
            }
           })
           .attr("cy", 300)
           //.delay(100)
           .duration(function(d, i) {
               return (d.Range*20)
           })
           .attrTween('width', function() {
            return d3.interpolateNumber(0, 250);
          });

           var rect = svg.selectAll("rect")
           .data(dataset)
           .enter()
           .append("rect")
           .attr("x", (userDistance - 30))
           .attr("y", 310   )
           .attr("height", 10)
           .attr("width", 60)

           console.log(userDistance);
        })


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
    