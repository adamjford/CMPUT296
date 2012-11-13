CMPUT296 Project: Checkers

Team Members:
Curnow, Thomas (curnow@ualberta.ca)
Ford, Adam
Lee, Austin

Proposal:
We would like to create a playable implementation of the board game Checkers, using two Arduinos talking to each other, each with an LCD display with the board displayed upon on it and a joystick to control the game.

One player will have the red pieces, and the other will have the white pieces. The white player's pieces start at the top of the board, and the red player's pieces start at the bottom of the board. The program, both deployed to each Arduino, will randomize which player will use the white pieces (and thus go first).

Control then alternates between each player. First, the active player can use the joystick to move between each of their pieces then can press the button to select it. Then, if that piece has no legal moves, the player is made aware of this and is allowed to pick a different piece.

If the selected piece does have legal moves, the player can then use the joystick to move between legal moves for the piece, of which there are two kinds:
* A simple move to an empty adjacent square diagonally forward.
* A jump over an opposing piece in an adjacent square diagonally forward to an empty square immediately and directly on the opposite side of the opposing piece to remove the opposing piece from the board. If a jump is available to at least one of the active player's piece, a jump must be performed that turn. If a piece that just jumped has at least one legal jump available to it, that player takes another turn and must immediately perform one of those jumps with that piece.

If a piece lands in the last row from their starting position (the first row of their opponent's starting position), that piece becomes a King, which allow the piece to take simple moves and jumps backwards. A piece cannot make any more additional jumps after becoming a King until the next turn.

A player immediately wins if the opponent has no more pieces remaining. The winner will be displayed to both players, then a new game will begin.

A pushbutton will be available to open a menu that will allow the players to reset the game to its original state
