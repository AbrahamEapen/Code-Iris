var width = 1920
  var height = 1000

  var gasMoleculeCount = 1
  var dustCount = 4
  var gasMoleculeRadius = 12
  var dustRadius = 36

  var realtimeContext = document.querySelector('#realtime')
      .getContext('2d', {alpha: true})

  realtimeContext.transform(1, 0, 0, 1, width / 2, height / 2)

  var radius = function(node) { return node.radius }

  var gasMolecules = d3.range(gasMoleculeCount).map(function() {
    return {
      radius: gasMoleculeRadius,
      x: -width / 3 + dustRadius - gasMoleculeRadius, // collide at same time
      y: height / 6,
      vx: 2,
      vy: 0
    }
  })

  var dustParticles = d3.range(dustCount).map(function(d, i) {
    return {
      radius: dustRadius,
      x: width / 3 * [-1, 0, 0, -1][i],
      y: height / 6 * [-1, 0, 1, 0][i],
      vx: [2, 0, 0, 2][i],
      vy: 0
    }})

  var nodes = dustParticles.concat(gasMolecules)

  d3.forceSimulation(nodes)
      .alphaDecay(0)
      .velocityDecay(0)
      .force("collide", d3.forceCollide()
          .radius(radius).strength(1).iterations(10))
      .on("tick", render)

  realtimeContext.lineWidth = 1
  realtimeContext.fillStyle = "red"

  function render() {

    var i
    var r
    var particle

    realtimeContext.clearRect(-width / 2, -height / 2, width, height)

    realtimeContext.beginPath()
    realtimeContext.moveTo(-dustRadius, -height / 3)
    realtimeContext.lineTo(-dustRadius, height / 3)
    realtimeContext.stroke()

    realtimeContext.beginPath()
    for(i = 0; i < gasMoleculeCount; i++) {
      particle = gasMolecules[i]
      r = particle.radius
      realtimeContext.moveTo(particle.x + r, particle.y)
      realtimeContext.arc(particle.x, particle.y, r, 0, 2 * Math.PI)
    }
    realtimeContext.stroke()

    realtimeContext.beginPath()
    for(i = 0; i < dustCount; i++) {
      particle = dustParticles[i]
      r = particle.radius
      realtimeContext.moveTo(particle.x + r, particle.y)
      realtimeContext.arc(particle.x, particle.y, r, 0, 2 * Math.PI)
    }
    realtimeContext.fill()
    realtimeContext.stroke()
  }
