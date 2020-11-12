window.onload = function() {
  var canvas = document.getElementById("board");
  var ctx = canvas.getContext("2d");
  ctx.fillStyle = "blue";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}


function move(e) {
  switch (e.keyCode) {
    case 37:
      xVel = -1; yVel = 0;
      break;
    case 38:
      xVel = 0; yVel = 1;
      break;
    case 39:
      xVel = 1; yVel = 0;
      break;
    case 40:
      xVel = 0; yVel = -1;
      break;
  }
}
