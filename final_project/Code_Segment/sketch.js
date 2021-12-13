// array to store note objects for visualization
let notes = [];
// array for storing original melody notes
let melody = [];

// variable to hold number of beats
let numBeats = 16;

// arrays to store extracted midi info from original melody
let originalMelody = [];
let originalStartTime = [];
let originalDuration = [];

// arrays to store extracted midi info from generated melody
let generatedMelody = [];
let generatedStartTime = [];
let generatedDuration = [];


// Identifies which notes in Note object scale array would be black keys on piano
let blackKeys = [1, 3, 5, 8, 10, 13, 15, 17, 20, 22, 25, 27, 29, 32, 34];
// Import RNN model
music_rnn = new mm.MusicRNN(
  "https://storage.googleapis.com/magentadata/js/checkpoints/music_rnn/basic_rnn"
);
music_rnn.initialize(); // initialize RNN model

// variable to store Synth object
const synth = new Tone.Synth().toDestination();

function setup() {
  createCanvas(800, 600);

  // loop to make 8 notes objects for orginal melody
  for (let i = 0; i < numBeats / 2; i++) {
    notes.push(new Note((i * width) / numBeats)); // stores note objects in array
  }

  // loop to store midi notes for each note object in a seperate array
  for (let i = 0; i < notes.length; i++) {
    melody.push(notes[i].pitch);
  }
}

let temp = document.getElementById("temp"); // variable to hold html slider
let playButton = document.getElementById("play"); // variable to hold html play button

// sets play button to start playing melody
playButton.onclick = function () {
  Tone.Transport.bpm.value = 200; // sets BPM for melody tempo
  Tone.Transport.start();
};

// Initialize variable to hold slider value
let sliderTemp = 1;
// Variable to store temp display value
let tempValue = document.getElementById("tempValue");
tempValue.innerHTML = temp.value; // initializes temp display value

// stores new slider value in variable when slider is moved
temp.oninput = () => {
  sliderTemp = temp.value;
  tempValue.innerHTML = temp.value; // changes temp display value
};

// variables to store time values to determine when original melody is played and generated melody is played
let playSectionOne = 0;
let playSectionTwo = 0;

function draw() {
  background(255); // sets background color
  // makes line to split canvas to identify original and generated melody
  stroke(0, 255, 0);
  strokeWeight(5);
  line(width / 2, 0, width / 2, height);

  // resets line colr and thickness for grid lines
  stroke(0);
  strokeWeight(1);
  // creates vertical line grid
  for (let i = 0; i < notes[0].scale.length; i++) {
    if (blackKeys.includes(i)) { // if i equals one of the notes designated as a black key...
      fill(0, 70); // .. make that line on the grid black
    } else { // if not designated a blakc key...
      fill(255, 70); //...make that line on the grid white
    }
    // rectangel to represent piano key on the grid
    rect(
      0,
      (height / notes[0].scale.length) * i,
      width,
      height / notes[0].scale.length
    );
  }
  // creates horizontal line grid
  for (let i = 0; i < numBeats; i++) {
    line((width / numBeats) * i, 0, (width / numBeats) * i, height);
  }

  // Displays red background for section that is playing
  if (Tone.now() < playSectionOne) {
    // if playing original melody section...
    fill(0, 0, 255, 100);
    rect(0, 0, width / 2, height); // ... display red background on left side of screen
  } else if (Tone.now() < playSectionTwo) {
    // if playing generated melody section...
    fill(255, 0, 0, 100);
    rect(width / 2, 0, width / 2, height); // ... display red background on right side of screen
  }

  fill(255); // set color for note blocks
  if (notes.length > 0) {
    // if original note objects have been made...
    for (let i = 0; i < notes.length; i++) {
      // ...loops through notes obj array
      if (notes[i].choose()) {
        // if mouseY is in range of specific note object
        if (i < numBeats / 2) {
          // if note obj is from original melody
          melody[i] = notes[i].move(); // changes midi note in original melody array
          if (originalMelody.length != 0) {
            // if midi info has already been extracted from original melody...
            originalMelody[i] = melody[i]; //... update midi pitch in extracted midi note array for original melody
          }
        } else if (i >= numBeats / 2) {
          // if note obj is from generated melody...
          generatedMelody[i - numBeats / 2] = notes[i].move(); //...update midi pitch in extracted midi note array for generated melody
        }
      }
      notes[i].display(); // display all note objs on canvas as rectangles
    }
  }
}

// Plays melody
Tone.Transport.schedule((time) => {
  for (let i = 0; i < originalMelody.length; i++) { // iterates through original melody array
    let midiNote = Tone.Frequency(originalMelody[i], "midi").toNote(); // converts MIDI note value to musical note value that can be played by Tone.js
    synth.triggerAttackRelease( // method to play note using synth object
      midiNote, // note value to play
      originalDuration[i], // duration of note
      time + originalStartTime[i] // start time of note.
    );
  }
  playSectionOne = time + originalStartTime[originalMelody.length - 1] + 1; // stores start time of last note for visual indicator when original melody is playing
  for (let i = 0; i < generatedMelody.length; i++) { // iterates through generated melody array
    let midiNote = Tone.Frequency(generatedMelody[i], "midi").toNote(); // converts MIDI note value to musical note value that can be played by Tone.js
    synth.triggerAttackRelease( // method to play note using synth object
      midiNote, // note value to play
      generatedDuration[i], // duration of note
      time + generatedStartTime[i] // start time of note.
    );
  }
    playSectionTwo = time + generatedStartTime[generatedMelody.length - 1] + 1; // stores start time of last note for visual indicator when generated melody is playing
  Tone.Transport.stop(); // stops time in Tone.js
}, 0);

// function to generate extension of original melody
function generateMelody() {
  let newMelody = makeMelodyObject(melody); // makes formatted melody object from current original melody

  const qns = mm.sequences.quantizeNoteSequence(newMelody, 1); // quantizes melody object into formatted structure
  extractOriginalMidiInfo(qns); // extracts midi info from original melody and stores in appropriate arrays
  music_rnn
    .continueSequence(qns, 16, int(sliderTemp)) // ML model extends original melody and returns generated melody object
    .then((sample) => extendMelody(sample)); // takes extended melody object and creates note objects for generated melody
}

// maps numeric duration values to musical subdivision values
let durMap = new Map([
  [1, "8n"],
  [2, "4n"],
  [3, "4n" + "8n"],
  [4, "2n"],
]);

// function to extract midi data (pitch, start time, duration) from original melody
function extractOriginalMidiInfo(melodyObject) {
  // clear storage arrays of previous values
  originalMelody = [];
  originalStartTime = [];
  originalDuration = [];

  // loops through notes in original melody object
  // takes formatted melody object as argument
  for (let i = 0; i < melodyObject.notes.length; i++) {
    originalMelody.push(melodyObject.notes[i].pitch); // stores midi note in melody array
    // variable to store duration value of each note
    let stepSize =
      melodyObject.notes[i].quantizedEndStep -
      melodyObject.notes[i].quantizedStartStep;
    originalDuration.push(durMap.get(stepSize)); // stores midi note duration in duration array
    originalStartTime.push(melodyObject.notes[i].quantizedStartStep / 2); // stores start time value in start time array
  }
  // prints midi info of original melody
  // console.log("melody notes = " + originalMelody);
  // console.log("Start times = " + originalStartTime);
  // console.log("Duration = " + originalDuration);
}

// function to extract midi data (pitch, start time, duration) from generated melody
// takes formatted melody object as argument
function extractGeneratedMidiInfo(melodyObject) {
  // clear storage arrays of previous values
  generatedMelody = [];
  generatedStartTime = [];
  generatedDuration = [];

  // loops through notes in generated melody object
  for (let i = 0; i < melodyObject.notes.length; i++) {
    generatedMelody.push(melodyObject.notes[i].pitch); // stores midi note in melody array
    // variable to store duration value of each note
    let stepSize =
      melodyObject.notes[i].quantizedEndStep -
      melodyObject.notes[i].quantizedStartStep;
    generatedDuration.push(durMap.get(stepSize)); // stores midi note duration in duration array
    // stores start time value in start time array
    generatedStartTime.push(
      melodyObject.notes[i].quantizedStartStep / 2 + numBeats / 2
    );
  }
  // prints midi info of generated melody
  // console.log("Generated Melody notes = " + generatedMelody);
  // console.log("Generated Start times = " + generatedStartTime);
  // console.log("Generated Duration = " + generatedDuration);
}

// function to create formatted melody object which can be processed by ML model
// Takes original melody array as argument
function makeMelodyObject(melody) {
  // creates empty formatted object
  let melodyObject = {
    notes: [],
    totalTime: 8.0,
  };
  //loops through each value in original melody array
  for (let i = 0; i < melody.length; i++) {
    melodyObject.notes.push({ pitch: melody[i], startTime: i, endTime: i + 1 }); // adds melody note to array in melody object
  }
  return melodyObject; // return formatted melody object
}

// function to turn generated melody notes into note objects
// in order to visualize generated melody
// takes formatted melody object of generated melody as argument
function extendMelody(melodyObject) {
  extractGeneratedMidiInfo(melodyObject); // extracts midi info from generated melody object

  if (notes.length > numBeats / 2) {
    // if there are already generated note objects in array...
    let addedNotes = notes.length - numBeats / 2; //...determine how many generated note objects are in array...
    notes.splice(numBeats / 2, addedNotes); // ...remove previous generated note objects from array
  }
  let x = width / (numBeats * 2); // variable to store width of note with duration value of 1
  // loops through notes in melody object
  for (let i = 0; i < melodyObject.notes.length; i++) {
    // variable to store duration value of each note to be used for visualized note width
    let duration =
      melodyObject.notes[i].quantizedEndStep -
      melodyObject.notes[i].quantizedStartStep;
    // creates new note object for each generated note and adds to note object array
    notes.push(
      new Note((melodyObject.notes[i].quantizedStartStep + numBeats) * x) // object parameter sets x axis position for each note visualized on canvas
    );
    // index value [numBeats / 2 + i] is to only loop through generated note objects which start at index 8
    notes[numBeats / 2 + i].duration = (width / numBeats) * (duration / 2); // sets visualized note object's width
    notes[numBeats / 2 + i].pitch = melodyObject.notes[i].pitch; // sets midi note for note object
    // sets visualized note location on y axis based on midi note value mapped to possible note values
    notes[numBeats / 2 + i].y =
      notes[numBeats / 2 + i].scale.indexOf(notes[numBeats / 2 + i].pitch) *
      (height / notes[0].scale.length);
  }
  // prints array of note objects
  console.log(notes);
}
