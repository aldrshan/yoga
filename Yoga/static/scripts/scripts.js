const yogaPoses = {
    day1: [
        { name: "Child's Pose", image: "static/img/childs_pose.jpg" },
        { name: "Cat-Cow Pose", image: "static/img/cat_cow.jpg" },
        { name: "Downward-Facing Dog", image: "static/img/down_dog.jpg" },
        { name: "Three-Legged Dog (Right)", image: "static/img/three_leg_dog.jpg" },
        { name: "Low Lunge (Right)", image: "static/img/low_lunge.jpg" },
        { name: "Three-Legged Dog (Left)", image: "static/img/three_leg_dog.jpg" },
        { name: "Low Lunge (Left)", image: "static/img/low_lunge.jpg" },
        { name: "Mountain Pose", image: "static/img/mountain.jpg" },
        { name: "Standing Forward Bend", image: "static/img/standing_forward_bend.jpg" },
        { name: "Halfway Lift", image: "static/img/halfway_lift.jpg" },

    ],
    day2: [
        { name: "Easy Pose", image: "static/img/easy_pose.jpg" },
        { name: "Twist (Right)", image: "static/img/seated_twist.jpg" },
        { name: "Twist (Left)", image: "static/img/seated_twist.jpg" },
        { name: "Tabletop Pose", image: "static/img/tabletop_pose.jpg" },
        { name: "Thread the Needle (Right)", image: "static/img/thread_the_needle.jpg" },
        { name: "Thread the Needle (Left)", image: "static/img/thread_the_needle.jpg" },
        { name: "Puppy Pose", image: "static/img/puppy_pose.jpg" },
        { name: "Cobra Pose", image: "static/img/cobra_pose.jpg" },
        { name: "Child's Pose", image: "static/img/childs.jpg" },
        { name: "Corpse Pose", image: "static/img/corpse_pose.jpg" },
    ],
    day3: [
        { name: "Seated Forward Bend", image: "static/img/seated_forward_bend.jpg" },
        { name: "Seated Wide-Legged Forward Bend", image: "static/img/seated_wide_forward_bend.jpg" },
        { name: "Bound Angle Pose", image: "static/img/bound_angle.jpg" },
        { name: "Bridge Pose", image: "static/img/bridge_pose.jpg" },
        { name: "Happy Baby", image: "static/img/happy_baby.jpg" },
        { name: "Supine Twist (Right)", image: "static/img/supine_twist.jpg" },
        { name: "Supine Twist (Left)", image: "static/img/supine_twist.jpg" },
        { name: "Reclined Butterfly", image: "static/img/reclined_butterfly.jpg" },
        { name: "Corpse Pose", image: "static/img/corpse_pose.jpg" },
    ],
    day4: [
        { name: "Mountain Pose", image: "static/img/mountain.jpg" },
        { name: "Chair Pose", image: "static/img/chair_pose.jpg" },
        { name: "Standing Forward Bend", image: "static/img/standing_forward_bend.jpg" },
        { name: "Halfway Lift", image: "static/img/halfway_lift.jpg" },
        { name: "High Plank", image: "static/img/high_plank.jpg" },
        { name: "Low Plank", image: "static/img/low_plank.jpg" },
        { name: "Upward-Facing Dog", image: "static/img/up_dog.jpg" },
        { name: "Downward-Facing Dog", image: "static/img/down_dog.jpg" },
        { name: "Warrior I (Right)", image: "static/img/warrior_one.jpg" },
        { name: "Warrior I (Left)", image: "static/img/warrior_one.jpg" },
    ],
    day5: [
        { name: "Warrior II (Right)", image: "static/img/warrior_two.jpg" },
        { name: "Warrior II (Left)", image: "static/img/warrior_two.jpg" },
        { name: "Extended Side Angle (Right)", image: "static/img/extended_side_angle.jpg" },
        { name: "Extended Side Angle (Left)", image: "static/img/extended_side_angle.jpg" },
        { name: "Reverse Warrior (Right)", image: "static/img/reverse_warrior.jpg" },
        { name: "Reverse Warrior (Left)", image: "static/img/reverse_warrior.jpg" },
        { name: "Triangle Pose (Right)", image: "static/img/triangle_pose.jpg" },
        { name: "Triangle Pose (Left)", image: "static/img/triangle_pose.jpg" },
        { name: "Wide-Legged Forward Bend", image: "static/img/wide_forward_bend.jpg" },
        { name: "Pyramid Pose (Right)", image: "static/img/pyramid_pose.jpg" },
        { name: "Pyramid Pose (Left)", image: "static/img/pyramid_pose.jpg" },

    ],
    day6: [
        { name: "Tree Pose (Right)", image: "static/img/tree_pose.jpg" },
        { name: "Tree Pose (Left)", image: "static/img/tree_pose.jpg" },
        { name: "Eagle Pose (Right)", image: "static/img/eagle_pose.jpg" },
        { name: "Eagle Pose (Left)", image: "static/img/eagle_pose.jpg" },
        { name: "Dancer Pose (Right)", image: "static/img/dancer_pose.jpg" },
        { name: "Dancer Pose (Left)", image: "static/img/dancer_pose.jpg" },
        { name: "Half Camel Pose (Right)", image: "static/img/half_camel.jpg" },
        { name: "Half Camel Pose (Left)", image: "static/img/half_camel.jpg" },
        { name: "Child's Pose", image: "static/img/child.jpg" },
    ],
    day7: [
        { name: "Cat-Cow Pose", image: "static/img/cat_cow.jpg" },
        { name: "Downward-Facing Dog", image: "static/img/down_dog.jpg" },
        { name: "Pigeon Pose (Right)", image: "static/img/pigeon_pose.jpg" },
        { name: "Pigeon Pose (Left)", image: "static/img/pigeon_pose.jpg" },
        { name: "Seated Forward Bend", image: "static/img/seated_forward_bend.jpg" },
        { name: "Seated Twist (Right)", image: "static/img/seated_twist.jpg" },
        { name: "Seated Twist (Left)", image: "static/img/seated_twist.jpg" },
        { name: "Boat Pose", image: "static/img/boat_pose.jpg" },
        { name: "Plow Pose", image: "static/img/plow_pose.jpg" },
        { name: "Corpse Pose", image: "static/img/corpse_pose.jpg" },
    ],
    //add more workouts as needed and update index.html
};

const startPauseButton = document.getElementById('start-button');
const workoutSelect = document.getElementById('workout-select');
const timerElement = document.getElementById('time');
const yogaImage = document.getElementById('yoga-image');

let currentPose = -1;
let timer;
let timerRunning = false;

// 1. Add a new variable to hold the audio element reference
let gong;

// 2. Create an Audio object and set its src to the path of the audio file
function loadAudio() {
    gong = new Audio("static/mp3/gong.mp3");
}
loadAudio();

// 3. Add a new function, playTone(), to play the audio
function playTone() {
    gong.currentTime = 0;
    gong.play();
}

function startTimer(duration, display) {
    let minutes, seconds;
    duration--;

    timer = setInterval(() => {
        minutes = parseInt(duration / 60, 10);
        seconds = parseInt(duration % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--duration < 0) {
            clearInterval(timer);
            nextPose();

            // 4. Call playTone() function each time the pose changes.
            playTone();

            // Wait for 10 seconds before starting the timer again
            setTimeout(() => {
                startTimer(60, display);
            }, 10000);
        }
    }, 1000);
}

function pauseTimer() {
    clearInterval(timer);
    timerRunning = false;
}

function startPause() {
    if (!timerRunning) {
        if (currentPose === -1) {
            nextPose();
            startTimer(60, timerElement);
        } else {
            let timeLeft = timerElement.textContent.split(':').reduce((acc, val, i) => acc * 60 + parseInt(val, 10));
            startTimer(timeLeft, timerElement);
        }
        timerRunning = true;
        startPauseButton.textContent = 'Pause';
    } else {
        pauseTimer();
        startPauseButton.textContent = 'Resume';
    }
}

function nextPose() {
    const selectedWorkout = workoutSelect.value;
    const poses = yogaPoses['day' + selectedWorkout.slice(-1)];

    if (currentPose < poses.length - 1) {
        currentPose++;
    } else {
        currentPose = 0;
    }
    yogaImage.src = poses[currentPose].image;
    yogaImage.alt = poses[currentPose].name;
    document.getElementById('pose-title').textContent = poses[currentPose].name;
    if (!timerRunning) {
        timerElement.textContent = "01:00";
    }
}

workoutSelect.addEventListener('change', () => {
    currentPose = -1;
    nextPose();
});

startPauseButton.addEventListener('click', startPause);