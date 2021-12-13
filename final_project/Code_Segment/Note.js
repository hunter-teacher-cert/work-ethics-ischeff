// Constructor function for individual note blocks
class Note {
  constructor(x) {
    this.x = x; // x position on canvas
    this.y = height / 2; // y position on canvas
    this.div = 8; // used to determine how wide each block should be based on how many notes you want
    this.scale = [83,82,81,80,79,78,77,76,75,74,73,72,71, 70, 69,68, 67,66,65,64,63,62,61,60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48]; // Possible note values a block could have
    this.duration = (width / this.div)/2; // width of note block
    this.size = (height / this.scale.length); // height of note block - divides canvas by numbers of possible notes
    this.chosen = false; // boolean variable to use when note is selected to move
    this.pitch = 65; // default note value
    this.fill = "#0000ff" // color of note block
    this.strokeWeight = 4; // outline thickness of note block
  }

  // method to display note blocks
  display() {
    fill(this.fill);
    rect(this.x, this.y, this.duration, this.size);
  }

 // method to determine if note block has been selected via the mouse
  choose() {
    if(mouseIsPressed) {
      if (
        mouseX > this.x &&
        mouseX < this.x + this.duration &&
        mouseY > 0 &&
        mouseY < height
      ) {
        return true
      }
    }
  }

  // method to relocate the note block when moved by mouse
  // also updates the note that would be played based on its location on the y axis
  move() {
    let y = map(mouseY, 0, height, 0, this.scale.length);
    this.y = (height / this.scale.length) * floor(y);
    this.pitch = this.scale[floor(y)];
    return this.pitch;
  }
}
