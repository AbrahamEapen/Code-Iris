const submitDistanceButton = document.getElementById('submitDistance');
const distanceInput = document.getElementById('distanceInput');
var userDistance;

submitDistanceButton.addEventListener('click', () => {
    userDistance = distanceInput.value;
    console.log(userDistance);
});
