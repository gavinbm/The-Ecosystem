window.onload function() {
const board = document.getElementByID("board");
const ctx = board.getContext("2d");
document.addEventListener("keydown", input);
setInverval(game, 1000/15);
}

const tileCount = 20;
const gridSize = 20;

class Snake {
  constructor() {
    this.x = 20;
    this.y = 20;
    this.xVel = 0;
    this.yVel = 0;
    this.tail = [];
    this.length = 3;
  }
}

class Apple {
  constructor() {
    this.x = 10;
    this.y = 10;
  }
}

function game() {
  snake = new Snake;
  apple = new Apple;
  snake.x = snake.x + snake.xVel;
  snake.y = snake.y + snake.xVel;

  if(snake.x < 0) {
    snake.x = tileCount - 1;
  } if(snake.x > tileCount - 1) {
    snake.x = 0;
  } if (snake.y < 0) {
    snake.y = tileCount - 1;
  } if (snake.y > tileCount - 1) {
    snake.y = 0;
  }

  ctx.fillStyle = "black";
  ctx.fillRect(0, 0, board.width, board.height);

  ctx.fillStyle = "red";
  ctx.fillRect(apple.x * gridSize, apple.y * gridSize, gridSize - 2, gridSize - 2);

  ctx.fillStyle = "lime";
  for(int i = 0; i < snake.tail.length; i++) {
    ctx.fillRect(snake.tail[i].x * gridSize, snake.tail[i].y * gridSize, gridSize - 2, gridSize - 2);
    if(snake.x == snake.tail[i].x && snake.y == snake.tail[i].y) {
      length = 3;
    }
  }

  if(apple.x == snake.x && apple.y == snake.y) {
    snake.length++;
    apple.x=Math.floor(Math.random()*tileCount);
    apple.y=Math.floor(Math.random()*tileCount);
  }
}

function input(snake) {
  switch(evt.keyCode) {
    case 37:
      snake.xVel = -1;
      snake.yVel = 0;
    case 38:
      snake.xVel = 0;
      snake.yVel = -1;
    case 39:
      snake.xVel = 1;
      snake.yVel = 0;
    case 40:
      snake.xVel = 0;
      snake.yVel = 1;
  }
}
