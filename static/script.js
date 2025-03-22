document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault();
        
        const data = {
            AGE: document.getElementById('age').value,
            GENDER: document.getElementById('gender').value,
            SMOKING: document.getElementById('smoking').value,
            FINGER_DISCOLORATION: document.getElementById('finger-discoloration').value,
            LEVEL: document.getElementById('level').value,
            EXPOSURE_POL: document.getElementById('exposure-pol').value,
            LONG_TERM_ILLNESS: document.getElementById('long-term-illness').value,
            ENERGY: document.getElementById('energy').value,
            IMMUNE_WEAKNESS: document.getElementById('immune-weakness').value,
            BREATHING_ISSUE: document.getElementById('breathing-issue').value,
            ALCOHOL_CONSUMPTION: document.getElementById('alcohol-consumption').value,
            THROAT_DISCOMFORT: document.getElementById('throat-discomfort').value,
            OXYGEN_SATURATION: document.getElementById('oxygen-saturation').value,
            CHEST_TIGHTNESS: document.getElementById('chest-tightness').value,
            FAMILY_HISTORY: document.getElementById('family-history').value,
            SMOKING_FAMILY_HISTORY: document.getElementById('smoking-family-history').value,
            STRESS_IMMUNE: document.getElementById('stress-immune').value
        };

        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = `Prediction: ${data.prediction}`;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('result').innerText = 'An error occurred. Please try again.';
        });
    });

    // Dark mode toggle functionality
    const toggleButton = document.getElementById('toggle-darkmode');
    if (toggleButton) {
        toggleButton.addEventListener('click', function() {
            document.body.classList.toggle('dark-mode');
        });
    }
});