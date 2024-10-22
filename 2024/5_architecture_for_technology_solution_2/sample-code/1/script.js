const boardSize = 8;
let board = [];
let currentPlayer = "black";

// ゲームボードを初期化する
function initBoard() {
  board = Array.from({ length: boardSize }, () => Array(boardSize).fill(null));
  board[3][3] = "white";
  board[3][4] = "black";
  board[4][3] = "black";
  board[4][4] = "white";
  updateCurrentPlayerDisplay();
  renderBoard();
}

// ゲームボードをレンダリングする
function renderBoard() {
  const gameBoard = document.getElementById("game-board");
  gameBoard.innerHTML = "";

  for (let row = 0; row < boardSize; row++) {
    for (let col = 0; col < boardSize; col++) {
      const cell = document.createElement("div");
      cell.classList.add("cell");

      if (board[row][col] === "black") {
        cell.classList.add("black");
      } else if (board[row][col] === "white") {
        cell.classList.add("white");
      }

      cell.addEventListener("click", () => handleCellClick(row, col));
      gameBoard.appendChild(cell);
    }
  }
}

// 現在のプレイヤーを表示する
function updateCurrentPlayerDisplay() {
  const playerDisplay = document.getElementById("player-display");
  playerDisplay.textContent = currentPlayer === "black" ? "黒" : "白";
  playerDisplay.style.color = currentPlayer === "black" ? "#000" : "#fff";
  playerDisplay.style.backgroundColor =
    currentPlayer === "black" ? "#000" : "#fff";
  playerDisplay.style.padding = "5px";
  playerDisplay.style.borderRadius = "5px";
}

// セルがクリックされたときの処理
function handleCellClick(row, col) {
  if (board[row][col] !== null) return;

  const directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1],
  ];

  let validMove = false;
  directions.forEach(([dx, dy]) => {
    if (flipDiscs(row, col, dx, dy, false)) {
      validMove = true;
    }
  });

  if (validMove) {
    board[row][col] = currentPlayer;
    directions.forEach(([dx, dy]) => {
      flipDiscs(row, col, dx, dy, true);
    });
    currentPlayer = currentPlayer === "black" ? "white" : "black";
    updateCurrentPlayerDisplay();
    renderBoard();
  }
}

// 指定方向にディスクをひっくり返す
function flipDiscs(row, col, dx, dy, flip) {
  let x = row + dx;
  let y = col + dy;
  let discsToFlip = [];

  while (
    x >= 0 &&
    x < boardSize &&
    y >= 0 &&
    y < boardSize &&
    board[x][y] !== null &&
    board[x][y] !== currentPlayer
  ) {
    discsToFlip.push([x, y]);
    x += dx;
    y += dy;
  }

  if (
    x >= 0 &&
    x < boardSize &&
    y >= 0 &&
    y < boardSize &&
    board[x][y] === currentPlayer &&
    discsToFlip.length > 0
  ) {
    if (flip) {
      discsToFlip.forEach(([fx, fy]) => {
        board[fx][fy] = currentPlayer;
      });
    }
    return true;
  }
  return false;
}

// ゲームの状態をリセットする
document.getElementById("reset-button").addEventListener("click", () => {
  initBoard();
});

// 初期化処理
initBoard();
