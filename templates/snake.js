var canvas = document.getElementById("board");
var ctx = canvas.getContext("2d");
canvas.addEventListener("keypress", move)
ctx.fillStyle = "black";
ctx.fillRect(0, 0, canvas.width, canvas.height);

px=py=20;
ax=ay=15;
xVel=yVel=0;



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
